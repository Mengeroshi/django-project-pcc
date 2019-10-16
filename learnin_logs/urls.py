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
    path ('topics/<int:topic_id>/', views.topic, name='topic')
]
