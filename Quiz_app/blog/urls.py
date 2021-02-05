from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='blog.home'),
    path('quiz_catalog/quiz_page/<str:cat>',views.quiz_page, name='blog.quiz_page'),
    path('quiz_catalog/result',views.quiz_page_result, name='blog.quiz_page_result'),
    path('quiz_catalog/',views.catogaries, name='blog.quiz_catlog'),
    path('questionUpload/',views.questionUpload, name='blog.questionUpload'),
    path('questionUpload/Uploaded',views.Uploaded, name='blog.Uploaded'),
    path('quiz_upload_cat/',views.quiz_upload_cat, name='blog.quiz_upload_cat'),
    path('quiz_upload_cat/Upload',views.quiz_upload, name='blog.quiz_upload'),
    path('quiz_upload_cat/Uploaded',views.add_quiz_question, name='blog.add_quiz_question'),
    path('quiz_upload_cat/add_cover_photo',views.add_cover_photo, name='blog.add_cover_photo'),
]

