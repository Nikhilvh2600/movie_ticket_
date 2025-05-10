from django.db import models

# Create your models here.

genres = [
    ['action','Action'],
    ['comedy','Comedy'],
    ['drama','Drama'],
    ['fantasy','Fantasy'],['horror','Horror'],['thriler','Thriler'],
    ['romance','Romance']]

languages = [ ['kannada','Kannada'],['english','English'],['hindi','Hindi'],
             ['telugu','Telugu'],['tamil','Tamil'] ]

class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255,choices=genres)
    language = models.CharField(max_length=255,choices=languages)
    synopsis = models.TextField()
    cast = models.TextField()
    movie_image = models.ImageField(upload_to='movie_image/',null=True,blank=True)
    duration_minutes = models.IntegerField()
    release_date = models.DateField()
    triler_url = models.CharField(max_length=2000,null=True,blank=True)
    status = models.CharField(max_length=255,null=True,blank=True)
    slug = models.CharField(max_length=1000,null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = self.title.replace(' ','-')
        super().save(*args,*kwargs)

    def __str__(self):
        return self.title