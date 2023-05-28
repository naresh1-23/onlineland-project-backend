from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    landpic = models.ImageField(upload_to = 'uploads/')
    created_date = models.DateField(default = datetime.now)
    
