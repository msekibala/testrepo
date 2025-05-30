from core.abstract.serializers import AbstractSerializer
from core.user.models import User

class UserSerializer(AbstractSerializer):
    
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','is_active','is_superuser','is_staff','created','updated']
        
        read_only_field = ['is_active']