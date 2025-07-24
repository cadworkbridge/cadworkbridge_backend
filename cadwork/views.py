from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .serializers import AssignGroupSerializer, ElementIdListSerializer
import element_controller as ec
import attribute_controller as ac



class Addition(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(name='a', required=True, type=int, location=OpenApiParameter.QUERY),
            OpenApiParameter(name='b', required=True, type=int, location=OpenApiParameter.QUERY),
        ],
        responses={200: AssignGroupSerializer}
    )
    def get(self, request):
        serializer = AssignGroupSerializer(data=request.query_params)
        if serializer.is_valid():
            total = serializer.validated_data['a'] + serializer.validated_data['b']
            return Response({'sum': total})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=AssignGroupSerializer,
        responses={200: AssignGroupSerializer}
    )
    def post(self, request):
        serializer = AssignGroupSerializer(data=request.data)
        if serializer.is_valid():
            total = serializer.validated_data['a'] + serializer.validated_data['b']
            return Response({'sum': total})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CadworkTestApi(APIView):
    def post(self, request):
        serializer = ElementIdListSerializer(data=request.data)
        if serializer.is_valid():
            element_ids = serializer.validated_data['element_ids']
            return Response({'received': element_ids}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

