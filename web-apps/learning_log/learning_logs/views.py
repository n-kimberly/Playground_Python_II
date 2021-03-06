from django.shortcuts import render
from .models import Topic

def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """List all topics from Learning Log"""
    topics = Topic.objects.order_by('date_added')
    # Store queryset in topics
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
