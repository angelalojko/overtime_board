from rest_framework.permissions import BasePermission

class IsCommandStaff(BasePermission):
    def has_permission(self, request, view): 
        return request.user.is_authenticated and request.user.role == 'Cmd' 
    
class IsLtOrAbove(BasePermission):
    def has_permission(self, request, view): 
        return request.user.is_authenticated and request.user.role in ['Lt', 'Cmd']  
    
class IsSgtOrAbove(BasePermission):
    def has_permission(self, request, view): 
        return request.user.is_authenticated and request.user.role in ['Sgt', 'Lt', 'Cmd']  
    
class IsPatrolOrAbove(BasePermission):
    def has_permission(self, request, view): 
        return request.user.is_authenticated and request.user.role in ['Pat', 'Sgt', 'Lt', 'Cmd']  
    
     