"""
Define  URL pattern for learning_logs
"""

from django.urls import path
from . import views

app_name = 'learnin_logs'

urlpatterns = [
    path('', views.index, name='index'),
    #Page that show all the topics
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry')
]
