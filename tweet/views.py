from django.shortcuts import render

# Create your views here.
def tweet (request):
    return render(request,'tweet/tweet.html')
# Create your views here.
def create_tweet (request):
   return render(request,'tweet/tweet.html')

# Create your views here.
def edit_tweet (request):
    return render(request,'tweet/tweet.html')