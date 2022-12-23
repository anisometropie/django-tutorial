from django.urls import path

from . import views

# we add namespace so that django knows which app view to create
# for an url when using the {% url %} template tag
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('new-poll/', views.newPoll, name='new-poll'),
    path('new-poll/submit', views.newPollSubmit, name='new-poll-submit'),
]
