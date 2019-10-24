from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),   
    path('login/', views.login, name='login'),
    path('investment/', views.investment, name='investment'),
    path('investmentSubmit/', views.investmentSubmit, name='investmentSubmit'),
    path('returnedSubmit/', views.returnedSubmit, name='returnedSubmit'),
    path('final/', views.final, name='final'),
    path('returning/', views.returned, name='returned'),
    path('compare/', views.compare, name='compare'),
    path('question0/', views.question0, name='question0'),
    path('question0_store/', views.question0_store, name='question0_store'),
    path('question1/', views.question1, name='question1'),
    path('question1_store/', views.question1_store, name='question1_store'),
    path('question2/', views.question2, name='question2'),
    path('question2_store/', views.question2_store, name='question2_store'),
    path('finish/', views.finish, name='finish')

    # path('', views.p, name='welcome'),    
]
