from django.urls import path
from . import views
from .models import Food,Choice

app_name='vote'
urlpatterns=[
    path('', views.index,name='index'),
    path('<int:Qid>/details/', views.detail ,name='detail'),
    path('<int:Qid>/result', views.result,name='result'),
    path('<int:Qid>/vote/', views.vote, name='vote'),

]