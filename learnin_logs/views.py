from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """The home page for learnin log"""
    return render(request, 'learnin_logs/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learnin_logs/topics.html', context)

def topic(request, topic_id):
    """Show all topics"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_adedd')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learnin_logs/topic.html', context)