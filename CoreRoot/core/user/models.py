import uuid
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist

from django.db import models
from django.http import Http404

# Create your models here.
class UserManager (BaseUserManager):
    
    def get_object_by_public_id(self, public_id):
          """
    Retrieves a user object by its public ID.

    Args:
        public_id (str): The public ID of the user to retrieve.

    Returns:
        User: The user object associated with the given public ID.

    Raises:
        Http404: If the user is not found.
    """
          try:
              return self.get(public_id = public_id)
              
          
          except (ObjectDoesNotExist, ValueError, TypeError) as exc:
              raise Http404 from exc
    
    def create_user(self, username, email, password=None,**kwargs):
        """Create and return a `User` with an email, phone
        number, username and password. """
        
        if username is None:
            raise TypeError('Users must have a username. ')
        
        if email is None:
            raise TypeError('Users must have an email.')
        
        if password is None:
            raise TypeError('User must have an password.')
        
        user = self.model(username=username,email=self.normalize_email(email), **kwargs)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self,username,email,password, **kwargs):
        
        """Create and return a `User` with superuser(admin)
        permissions
        """
        if password is None:
            raise TypeError('Superusers must have a password. ')
        
        if email is None:
            raise TypeError('Superusers must have an email.')
        
        if username is None:
            raise TypeError('Superusers must have an username.')
        
        user = self.create_user(username, email, password, **kwargs)
        
        user.is_superuser = True
        user.is_staff =True
        user.save(using=self._db)
        
        return user
    
        

class User(AbstractBaseUser,PermissionsMixin):
    public_id = models.UUIDField(db_index=True,unique=True,
                                 default=uuid.uuid4,editable=False)
    
    username = models.CharField(db_index=True,max_length=255,unique=True)
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True,null=True)
    email = models.EmailField(db_index = True, unique = True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        default='avatar/default.png')
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.email}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    

        
