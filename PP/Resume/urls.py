from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.welcome, name="home"),
    path("resumepage/", views.Resume, name="resumepage"),
    path("placementprediction/", views.placementprediction, name="placementprediction"),
    path("learning", views.learning, name="learning"),
    path("links", views.links, name="links"),
    path("webdevelopment", views.webdevelopment, name="webdevelopment"),
    path("index/", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.Login_process, name="login"),
    path("resumepage/upload_resume/", views.upload_resume, name="upload_resume"),
    # path("list_resumes", views.list_resumes, name="list_resumes"),
    path("resume_download", views.list_resumes, name="resume_download"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
