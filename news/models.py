from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.title
    

# Rasm yuklash uchun klass
#class Photo(models.Model):
#    photo = models.ImageField()
#
#    def __repr__(self):
#        return self.photo