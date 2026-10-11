from django.contrib import admin
from .models import DetectionImage, DetectedObject

@admin.register(DetectionImage)
class DetectionImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at')
    list_filter = ('uploaded_at',)


@admin.register(DetectedObject)
class DetectedObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'confidence', 'image')
    list_filter = ('name',)
    search_fields = ('name',)
# Register your models here.
