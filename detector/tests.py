from django.test import TestCase, Client
from django.urls import reverse
from .models import DetectionImage, DetectedObject


class DetectorTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    def test_upload_page_loads(self):
        """صفحه‌ی آپلود لود می‌شه"""
        response = self.client.get(reverse('upload'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'تشخیص شیء')
    
    def test_result_404(self):
        """تصویر نامعتبر 404 می‌ده"""
        response = self.client.get(reverse('result', args=[999]))
        self.assertEqual(response.status_code, 404)
    
    def test_model_creation(self):
        """مدل درست ساخته می‌شه"""
        img = DetectionImage.objects.create(image='uploads/test.jpg')
        self.assertEqual(str(img), f"تصویر {img.id}")
        
        obj = DetectedObject.objects.create(
            image=img, name='person', confidence=0.95,
            x1=0, y1=0, x2=100, y2=100
        )
        self.assertEqual(str(obj), "person (0.95)")
        self.assertEqual(img.detected_objects.count(), 1)
    
    def test_cascade_delete(self):
        """CASCADE کار می‌کنه"""
        img = DetectionImage.objects.create(image='uploads/test.jpg')
        DetectedObject.objects.create(
            image=img, name='person', confidence=0.95,
            x1=0, y1=0, x2=100, y2=100
        )
        img.delete()
        self.assertEqual(DetectedObject.objects.count(), 0)

# Create your tests here.
