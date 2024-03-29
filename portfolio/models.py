from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image= models.ImageField( upload_to='portfolio/images')
    urls=models.URLField(blank=True)

    def __str__(self):
        return self.title