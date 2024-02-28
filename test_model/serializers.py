from rest_framework import serializers
from .models import Product, Lesson



class ProductSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializeMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'start_date', 'price', 'lesson_count']

        
        def get_lessons_count(self, obj):
            return Lesson.objects.filter(product=obj).count()