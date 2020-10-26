from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.deletion import CASCADE

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=CASCADE, related_name='userProfile')
    photo = CloudinaryField("photo")
    name = models.CharField(max_length=20)
    userName = models.CharField(max_length=10, blank=True)
    contact = models.EmailField(max_length=254)
    country = models.CharField(max_length=20, null=True)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ["name"]

    def saveProfile(self):
        self.save()

    @classmethod
    def getProfileById(cls, pk):
        try:
            profileObject = cls.objects.get(id=pk)
            return profileObject
        except ObjectDoesNotExist:
            message = "Profile does not exist"
            return message
