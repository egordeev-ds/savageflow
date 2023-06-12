from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from forum import views

urlpatterns = [

    #главная
    path('', views.main_view, name='main'),

    #меню
    path('about.html', views.about_view, name='about'),
    path('contact.html', views.contact_view, name='contact'),

    #questions
    path('questions.html', views.questions_view, name='questions'),
    path('questions/<int:post_id>/', views.question_detail, name='question_detail'),
    path('delete_answer/<int:answer_id>/', views.delete_answer, name='delete_answer'),
    path('questions/<int:question_id>/edit/<int:answer_id>/', views.edit, name='edit'),
    path('answer/<int:post_id>/', views.answer_view, name='answer'),

    #add question
    path('post.html', views.post_view, name='post'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)