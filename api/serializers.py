from rest_framework import serializers
from students.models import student

class studentSerializer (serializers.ModelSerializer):

    class Meta:

        model = student
        fields = "__all__"
