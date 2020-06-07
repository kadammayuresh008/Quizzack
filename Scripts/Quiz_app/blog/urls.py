from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='blog.home'),
    path('about/',views.about, name='blog.about'),
    path('quiz_catalog/quiz_page',views.quiz_page, name='blog.quiz_page'),
    path('quiz_catalog/result',views.quiz_page_result, name='blog.quiz_page_result'),
    path('quiz_catalog/',views.catogaries, name='blog.quiz_catlog'),
]

