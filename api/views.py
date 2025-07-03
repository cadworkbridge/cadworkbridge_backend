from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

    def post(self, request):
        data = request.data
        return Response({"received": data}, status=status.HTTP_201_CREATED)

