from rest_framework import serializers 
from .models import OvertimePost, Users, Signup
# this allows for converting your database data to JSON (API data) which is seen by the frontend 
class OvertimePostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = OvertimePost
        fields = '__all__'