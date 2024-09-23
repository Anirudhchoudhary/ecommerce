import uuid

from django.db import models
from thumbnails.fields import ImageField
 
# Create your models here.


class Image(models.Model):
    image = ImageField(pregenerated_sizes=["small", "large"], upload_to="images")
    name = models.CharField(max_length=256, default="")
    uuid = models.UUIDField(auto_created=True, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} |  {self.id}"
    
    def save(self, *args, **kwargs):
        created = not self.pk

        if created:
            self.uuid = uuid.uuid4()
    
        return super(Image, self).save(args, kwargs)
