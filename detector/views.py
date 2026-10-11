from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import DetectionImage, DetectedObject
from ultralytics import YOLO
import os

# مدل رو یک بار load کن (نه هر بار!)
model = YOLO('yolov8n.pt')


def upload_image(request):
    """آپلود تصویر و تشخیص اشیا"""
    if request.method == 'POST' and request.FILES.get('image'):
        # ۱. ذخیره تصویر
        img_obj = DetectionImage.objects.create(image=request.FILES['image'])
        
        # ۲. مسیر فایل
        img_path = os.path.join(settings.MEDIA_ROOT, img_obj.image.name)
        
        # ۳. تشخیص با YOLO
        results = model(img_path)
        
        # ۴. ذخیره نتایج
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                
                DetectedObject.objects.create(
                    image=img_obj,
                    name=model.names[cls],
                    confidence=conf,
                    x1=x1, y1=y1, x2=x2, y2=y2
                )
        
        return redirect('result', img_id=img_obj.id)
    
    return render(request, 'detector/upload.html')


def result(request, img_id):
    """نمایش نتیجه‌ی تشخیص"""
    img_obj = get_object_or_404(DetectionImage, id=img_id)
    objects = img_obj.detected_objects.all()
    
    return render(request, 'detector/result.html', {
        'image': img_obj,
        'objects': objects
    })

# Create your views here.
