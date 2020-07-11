from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
   
    path('',views.index,name='index'),
    path('about/',TemplateView.as_view(template_name="about.html")),
    path('contact/',TemplateView.as_view(template_name="contact.html")),
    path('blog/',TemplateView.as_view(template_name="blog.html")),
    path('blogSingle/',TemplateView.as_view(template_name="blogSingle.html")),
    path('courses/',TemplateView.as_view(template_name="courses.html")),    
    path('pricing/',TemplateView.as_view(template_name="pricing.html")),
    path('teacher/',TemplateView.as_view(template_name="teacher.html")),
]