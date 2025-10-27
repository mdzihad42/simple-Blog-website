from django.db import models
from django.contrib.auth.models import AbstractUser
class UserInfoModel(AbstractUser):
    user=[
        ('Author','Author' ),
        ('Admin','Admin'),

    ]
    full_name=models.CharField(max_length=100,null=True)
    user_type=models.CharField(choices=user , max_length=30,null=True)
    
    def __str__(self):
        return self.username

class PostModel(models.Model):
    cat=[
        ('Technology','Technology'),
        ('Lifestyle','Lifestyle'),
        ('Business','Business'),
    ]
    status=[
        ('Pending','Pending'),
        ('Publish','Publish'),
        ('Reject','Reject'),
    ]
    title=models.CharField(max_length=100,null=True)
    content=models.CharField(max_length=300,null=True)
    category=models.CharField(choices=cat, max_length=30,null=True)
    status=models.CharField(choices=cat,default='Pending', max_length=30,null=True)
    image=models.ImageField(null=True,upload_to='media/image')
    published_date=models.DateField(null=True)
    updated_at=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(UserInfoModel, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title


