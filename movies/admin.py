from django.contrib import admin
from .models import Movies 
# Register your models here.

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['movie_id','title','genre','language',
                    'slug',
                    'duration_minutes','release_date',
                    'synopsis','cast','triler_url','status']