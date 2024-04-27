from django.db import models

# Create your models here.


class Phtoto_gallery:
    name = models.CharField(max_length=100)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    photo = models.ImageField(default="default.jpg", upload_to="media")
