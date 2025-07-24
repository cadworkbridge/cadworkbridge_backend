from rest_framework import serializers

class AssignGroupSerializer(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()


class ElementIdListSerializer(serializers.Serializer):
    element_ids = serializers.ListField(
        child=serializers.IntegerField()
    )
