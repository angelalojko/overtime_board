from rest_framework import serializers 
from .models import OvertimePost, Users, Signup
# this allows for converting your database data to JSON (API data) which is seen by the frontend 
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta: 
        model = Users

        fields = [ 
            'badge_num', 
            'first_name', 
            'last_name', 
            'full_name',
            'hours', 
            'pin',
            'email', 
            'phone',
            'contact_method', 
            'role'
        ]
        extra_kwargs = {
            'pin': {'write_only': True}
        }

    def get_full_name(self, obj): 
        return f"{obj.first_name} {obj.last_name}"






class OvertimePostSerializer(serializers.ModelSerializer):
    slots_filled = serializers.SerializerMethodField()

    class Meta: 
        model = OvertimePost
        fields = '__all__'
    
    def get_slots_filled(self, obj):
        return obj.signup_set.filter(status='confirmed').count()
    
class SignupSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)
    overtime_detail = OvertimePostSerializer(source='overtime', read_only=True)
    assigned_by_detail = UserSerializer(source='assigned_by', read_only=True)

    class Meta:
        model = Signup
        fields = [
            'id',
            'overtime',
            'overtime_detail',
            'user',
            'user_detail',
            'assigned_by',
            'assigned_by_detail',
            'status',
            'assignment_type',
            'notification_sent',
            'notification_sent_at',
            'confirmed',
            'confirmed_at',
            'assigned_at',
        ]
        extra_kwargs = {
            'overtime': {'write_only': True},
            'user': {'write_only': True},
            'assigned_by': {'write_only': True},
        }