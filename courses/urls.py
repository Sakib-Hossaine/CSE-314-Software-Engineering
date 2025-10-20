from django.urls import path, include
from . import views
# in this page all url paths
urlpatterns = [
    path("courses/", views.courses, name="courses"),
    path("courses/<int:pk>/", views.course_detail, name="course_detail"),
    path("courses/<int:pk>/buy/", views.start_payment, name="start_payment"),
    path("payment/success/", views.payment_success, name="payment_success"),
    path("payment/fail/", views.payment_fail, name="payment_fail"),
    path("payment/cancel/", views.payment_cancel, name="payment_cancel"),
    path("payment/ipn/", views.payment_ipn, name="payment_ipn"),
    path("courses/<int:pk>/update/", views.update_course, name="update_course"),
    path("courses/<int:pk>/delete/", views.delete_course, name="delete_course"),
    path("add/", views.add_course, name="add_course"),
    path("", include("courses.urls_class")),
]
