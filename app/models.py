from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Profile model (extra user information ke liye)
class Profile(models.Model):

    # Django default user se connect
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Signup form ka Full Name
    full_name = models.CharField(max_length=100)

    # Email (optional because already User me hota hai, but safe)
    email = models.EmailField()

    # Account create date
    created_at = models.DateTimeField(auto_now_add=True)


    # Admin panel me name show hoga
    def __str__(self):
        return self.full_name