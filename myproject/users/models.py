from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio= models.CharField(max_length=200)

    def __str__(self):
        return self.user.name
    

