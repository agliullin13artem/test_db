from django.shortcuts import render
from rest_framework import generics
from .models import Product, Lesson
from .serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
