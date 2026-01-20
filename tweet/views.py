from django.shortcuts import render

# Create your views here.
def feed (request):
    return render(request,'tweet/feed.html')
# Create your views here.
def create_tweet (request):
   return render(request,'tweet/tweet.html')

# Create your views here.
def edit_tweet (request):
    return render(request,'tweet/tweet.html')

def view_tweet(request, tweet_id):
    # tweet = get_object_or_404(Tweet, id=tweet_id)
    return render(request, "tweet/view.html")
