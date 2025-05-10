from django.shortcuts import render
from .models import Movies
from reviews.models import Reviews
from django.db.models import Avg
from datetime import datetime 
# Create your views here.


def movieview(request,slug):
    if Movies.objects.filter(slug=slug).exists():
        today = datetime.today().date()
        movie = Movies.objects.get(slug=slug)
        reviews=None
        no_users=None
        rating=None
        if Reviews.objects.filter(movie=movie).exists():
            reviews = Reviews.objects.filter(movie=movie)
            no_users = reviews.count()
            rating = reviews.aggregate(avg_rating= Avg('rating'))
        
        context = {
            'movie' : movie,
            'rating':rating['avg_rating'] if rating else None,
            'no_users' : no_users,
            'reviews' : reviews[0:3] if reviews else None,
            'today':today
            }
        return render(request,'movies/movie.html',context)
    return render(request, 'movies/404.html', status=404)