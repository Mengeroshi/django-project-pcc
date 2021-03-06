from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http  import Http404

# Create your views here.
def index(request):
    """The home page for learnin log"""
    return render(request, 'learnin_logs/index.html')

@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learnin_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show all topics"""
    topic = get_object_or_404(Topic, id=topic_id)
    #Make sure the topic belongs to the current user
    check_topic_owner(topic, request)

    entries = topic.entry_set.order_by('-date_adedd')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learnin_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        #NO DATA SUBMMITED; CREATE A BLANK FORM
        form = TopicForm()
    else:
        #POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learnin_logs:topics')
    
    #Display a blank or invalid form.
    context = {'form': form }
    return render(request, 'learnin_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)
    
    check_topic_owner(topic, request)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learnin_logs:topic', topic_id=topic_id)
    
    context = {'topic': topic, 'form': form}
    return render(request, 'learnin_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edit an existing entry """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_topic_owner(topic, request)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learnin_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learnin_logs/edit_entry.html', context)

def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404