from django.db import models

class DetectionImage(models.Model):
    """تصویر آپلود شده برای تشخیص"""
    image = models.ImageField(upload_to='uploads/', verbose_name="تصویر")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ آپلود")
    
    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"
        ordering = ['-uploaded_at']  # جدیدترین اول
    
    def __str__(self):
        return f"تصویر {self.id}"


class DetectedObject(models.Model):
    """شیء شناسایی‌شده در تصویر"""
    image = models.ForeignKey(
        DetectionImage, 
        on_delete=models.CASCADE, 
        related_name='detected_objects',
        verbose_name="تصویر"
    )
    name = models.CharField(max_length=100, verbose_name="نام شیء")
    confidence = models.FloatField(verbose_name="دقت")
    x1 = models.FloatField(verbose_name="x1")
    y1 = models.FloatField(verbose_name="y1")
    x2 = models.FloatField(verbose_name="x2")
    y2 = models.FloatField(verbose_name="y2")
    
    class Meta:
        verbose_name = "شیء شناسایی‌شده"
        verbose_name_plural = "اشیاء شناسایی‌شده"
    
    def __str__(self):
        return f"{self.name} ({self.confidence:.2f})"

# Create your models here.
