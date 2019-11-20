from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=100, verbose_name='First name')
    lastname  = models.CharField(max_length=100, verbose_name='Last name')
    email  = models.EmailField(max_length=60)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    ads  = models.BooleanField(default=True)
    username = models.CharField(max_length=80)

    def get_absolute_url(self):
    	return reverse("", kwargs={"username": self.username})

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pic')

	def __str__(self):
		return f"{self.user.username} Profile"