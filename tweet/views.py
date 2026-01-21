from django.shortcuts import render
from .models import Tweet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tweet
from .forms import TweetForm
from django.db.models import Q
# Create your views here.
def feed(request):
    query = request.GET.get('q', '')  # get search query from input
    if query:
        # search in tweet text or username
        tweets = Tweet.objects.filter(
            Q(text__icontains=query) | Q(user__username__icontains=query)
        ).order_by('-created_at')
    else:
        tweets = Tweet.objects.all().order_by('-created_at')
    
    context = {
        'tweets': tweets,
        'search_query': query,  # pass to template so input can retain value
    }
    return render(request, 'tweet/feed.html', context)
# Create your views here.
def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)  # bind POST + FILES
        if form.is_valid():
            tweet = form.save(commit=False)  # don't save yet
            tweet.user = request.user        # assign the logged-in user
            tweet.save()                     # now save
            messages.success(request, "Chai posted successfully!")
            return redirect("tweet:feed")   # or wherever you want
        else:
            messages.error(request, "Something went wrong. Check the form.")
    else:
        form = TweetForm()  # empty form for GET request

    return render(request, "tweet/create_tweet.html", {"form": form})

@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)

    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            messages.success(request, "Chai updated successfully!")
            return redirect("tweet:feed")
        else:
            messages.error(request, "Failed to update your chai.")
    else:
        form = TweetForm(instance=tweet)

    return render(request, "tweet/create_tweet.html", {"form": form, "tweet": tweet})

@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        messages.success(request, "Chai deleted!")
    return redirect("tweet:feed")

def view_tweet(request, tweet_id):
    # tweet = get_object_or_404(Tweet, id=tweet_id)
    return render(request, "tweet/view.html")
