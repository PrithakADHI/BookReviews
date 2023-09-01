from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from datetime import datetime

from . import models
from . import forms

# Create your views here.

def home(request):
    return render(request, "home.html", {'reviews': models.Review.objects.all()})

def logout_view(request):
    logout(request)
    return redirect('/')

def review_detail(request, review_slug):
    review = get_object_or_404(models.Review, slug=review_slug)
    return render(request, 'review_details.html', {'review': review})

def review_add(request):
    if request.method == "POST":
        form = forms.MakePost(request.POST)
        if form.is_valid():
            form_title = form.cleaned_data["title"]
            form_content = form.cleaned_data["content"]
            current_user = request.user
            current_time = datetime.now()
            models.Review(user=current_user, published_time=current_time, title=form_title, content=form_content).save()
            return redirect('home')
    else:
        form = forms.MakePost()
        
    return render(request, 'review_add.html', {'form': form})

def user_info(request):
    return render(request, 'user_details.html', {'reviews': models.Review.objects.all()})

def delete_review(request, pk):
    review = get_object_or_404(models.Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('home')
    
    return render(request, 'delete_review.html', {'review': review})