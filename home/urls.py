from django.contrib import admin
from django.urls import path,include
from home import views


admin.site.site_header="My Portfolio"
admin.site.site_title=" Welcome Divyansh"
admin.site.index_title="This is Divyansh Portfolio"
urlpatterns = [
    path('',views.home, name='home'),
    path('projects',views.projects, name='projects'),
    path('contact',views.contact, name='contact')
]
