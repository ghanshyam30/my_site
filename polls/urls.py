from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex :  /polls/
    # path('',views.index,name='index'), #Converting to generic view form
    path('',views.IndexView.as_view(),name='index'),
    # ex : /polls/5
    # path('<int:question_id>/',views.detail,name='detail'), #Replaced question_id with pk to make it generic
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    # ex : /polls/5/results
    # path('<int:question_id>/results/',views.results,name='results'), #Replaced question_id with pk to make it generic
    path('<int:pk>/results/',views.ResultsVeiw.as_view(),name='results'),
    # ex : /polls/5/vote
    path('<int:question_id>/votes/',views.votes,name='votes')
]
