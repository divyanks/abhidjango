from django.db import models

# Create your models here.
class user(models.Model):
    fname    = models.CharField(max_length=30)
    lname    = models.CharField(max_length=30)
    email    = models.CharField(max_length=50)
    pnumber  = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email
    def isLoggedIn( email, password):
        check = user.objects.filter(email=email,password=password)
        user1 = check.first().__dict__
        return user1, check.count()
