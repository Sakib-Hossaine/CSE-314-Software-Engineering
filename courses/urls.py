from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.courses, name="courses"),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/update/', views.update_course, name='update_course'),
    path('courses/<int:pk>/delete/', views.delete_course, name='delete_course'),
    path('add/', views.add_course, name='add_course'),
   
]
