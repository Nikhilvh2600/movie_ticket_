from django.db import models
from accounts.models import User
from movies.models import Movies
# Create your models here.


class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3,decimal_places=1)
    review_text = models.TextField()
    created_at = models.DateField(auto_now_add=True)