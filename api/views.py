from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from .models import OvertimePost, Users, Signup
from .serializers import OvertimePostSerializer, UserSerializer, SignupSerializer



class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny] 

    @action(detail=False, methods=['post'])
    def login(self, request):
        badge_num = request.data.get('badge_num')
        pin = request.data.get('pin')
        if not badge_num or not pin:
            return Response(
                {'error': 'Badge number and PIN are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        
        try:
            user = Users.objects.get(badge_num=badge_num, pin=pin)
        except Users.DoesNotExist:
            return Response(
                {'error': 'Invalid badge number or PIN'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })
    
    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logged out successfully'})
        except Exception:
            return Response(
                {'error': 'Invalid token'},
                status=status.HTTP_400_BAD_REQUEST
            )

class OvertimePostViewSet(viewsets.ModelViewSet):
    queryset = OvertimePost.objects.all()
    serializer_class = OvertimePostSerializer

    def get_queryset(self):
        queryset = OvertimePost.objects.all()
        status_filter = self.request.query_params.get('status')
        shift_filter = self.request.query_params.get('shift')
        date_filter = self.request.query_params.get('date')

        if status_filter:
            queryset = queryset.filter(status=status_filter)
        if shift_filter:
            queryset = queryset.filter(shift=shift_filter)
        if date_filter:
            queryset = queryset.filter(date=date_filter)

        return queryset

    @action(detail=True, methods=['get'])
    def signups(self, request, pk=None):
        post = self.get_object()
        signups = Signup.objects.filter(overtime=post)
        serializer = SignupSerializer(signups, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = Users.objects.all()
        role_filter = self.request.query_params.get('role')
        shift_filter = self.request.query_params.get('shift')
        eligible_filter = self.request.query_params.get('is_eligible')

        if role_filter:
            queryset = queryset.filter(role=role_filter)
        if shift_filter:
            queryset = queryset.filter(shift=shift_filter)
        if eligible_filter is not None:
            queryset = queryset.filter(is_eligible=eligible_filter.lower() == 'true')

        return queryset

    @action(detail=True, methods=['get'])
    def signups(self, request, pk=None):
        user = self.get_object()
        signups = Signup.objects.filter(user=user)
        serializer = SignupSerializer(signups, many=True)
        return Response(serializer.data)


class SignupViewSet(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer

    @action(detail=True, methods=['patch'])
    def confirm(self, request, pk=None):
        signup = self.get_object()
        signup.confirmed = True
        signup.confirmed_at = timezone.now()
        signup.status = 'confirmed'
        signup.save()
        return Response(SignupSerializer(signup).data)

    @action(detail=True, methods=['patch'])
    def notify(self, request, pk=None):
        signup = self.get_object()
        signup.notification_sent = True
        signup.notification_sent_at = timezone.now()
        signup.save()
        return Response(SignupSerializer(signup).data)