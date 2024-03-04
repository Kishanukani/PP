from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("upload/", views.resume_analysis, name="resume_upload"),
    path("resumepage/analyzereume", views.resume_analysis, name="analyzereume"),
]
