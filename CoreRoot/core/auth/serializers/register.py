from rest_framework import serializers

from core.user.serializer import UserSerializer
from core.user.models import User

class RegisterSerializer(UserSerializer):
    """
    Registration serializer for requests and user creation

    _
    """
    # Making sure the password is at least 8 characters long, and no longer than 128
    
    password = serializers.CharField(max_length=128, min_length=8, 
                                     write_only=True, required=True)
    
    class Meta:
        model = User
        
        #list of all fields that can be included in a request or a response
        fields = ['id','bio', 'avatar','email',
                  'username','first_name','last_name','password']
        
    def create(self, validated_data):
        #Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)
    
    
    
    