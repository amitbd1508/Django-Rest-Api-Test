# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Stock
from .serializer import serializers, StockSerializer


# Create your views here.
class StockList(APIView):
    def get(self,request):
        stocks=Stock.objects.all()
        serializer=StockSerializer(stocks,many=True)
        return Response(serializer.data)

    def __pos__(self):
        pass
