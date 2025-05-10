from django.shortcuts import render,redirect
from .models import Reviews
from accounts.models import User 
from movies.models import Movies
# Create your views here.

def add_review(request,slug):
    user = User.objects.get(username=request.user)
    movie = Movies.objects.get(slug=slug)
    if request.method == 'POST':
        rating = request.POST['rating']
        review_text = request.POST['review_text']
        Reviews.objects.create(user=user,movie=movie,
                               rating=rating,review_text=review_text)
        return redirect(f'/movie/{slug}/')
    context = {
        'user':user,
        'movie' : movie
    }
    return render(request,'reviews/add_review.html',context)