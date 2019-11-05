from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=100, verbose_name='First name')
    lastname  = models.CharField(max_length=100, verbose_name='Last name')
    username  = models.EmailField()
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    ads  = models.BooleanField(default=True)

    def get_absolute_url(self):
    	return reverse("", kwargs={"username": self.username})
