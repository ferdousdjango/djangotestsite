from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    urls=models.URLField(blank=True)
    image= models.ImageField( upload_to='portfolio/images')

    def __str__(self):
        return self.title