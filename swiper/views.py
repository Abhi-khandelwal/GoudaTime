from django.shortcuts import render
from .models import Restaurant
from django.contrib.auth import login, authenticate, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.template import RequestContext

from swiper.forms import MatchRestaurantForm, SignUpForm
from swiper.models import Match, MatchManager

@login_required
def index(request):
    """
    View function for home page of site.
    """

    if request.method == 'POST':
        form = MatchRestaurantForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('index')
    else:
        form = MatchRestaurantForm()
        if Restaurant.objects.all():
            current_restaurant = Restaurant.objects.all()[0]
        else:
            current_restaurant = None

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'restaurant': current_restaurant},
    )

@login_required
def add_restaurant(request, restaurant):
    """ function to add the restaurant to current user"""
    user.matches.add()
    pass

@login_required
def show_restaurant(request, restaurant_id):
    """ display specific restaurant from uuid """
    try:
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        # Render the HTML template index.html with the data in the context variable
        return render(
            request,
            'restaurant.html',
            context={'restaurant': restaurant},
        )
    except ValueError:
        raise Http404

def signup(request):
    """ the page for registration on GoudaTime """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    """
    View function for profile page of each user.
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'profile.html',
        context={},
    )

@login_required
def matches(request):
    """
    View function for matches page of each user to display matched restaurants
    """
    user_pk = request.user.pk
    matches = MatchManager.get_matches(user=user_pk)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'matches.html',
                              {'matches': matches},)


@login_required
def add_match(request):
    """
    View function for adding a match to a user
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'add_match.html',
        context={},
    )

def about(request):
    """
    View function for about page of GoudaTime.
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'about.html',
        context={},
    )

def thank_you(request):
    """
    View function for thank you page of GoudaTime.
    """

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'registration/thank_you.html',
        context={},
    )
