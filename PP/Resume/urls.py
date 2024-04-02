from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.welcome, name="home"),
    path("landingpage", views.landingpage, name="landingpage"),
    path("resumepage/", views.Resume, name="resumepage"),
    path("placementprediction/", views.placementprediction, name="placementprediction"),
    path("learning", views.learning, name="learning"),
    path("links", views.links, name="links"),
    path("roadmap", views.roadmap, name="roadmap"),
    path("webdevelopment", views.webdevelopment, name="webdevelopment"),
    path("machinelearning", views.machinelearning, name="machinelearning"),
    path("datascience", views.datascience, name="datascience"),
    path("mobileapplication", views.mobileapplication, name="mobileapplication"),
    path("programinglanguage", views.programinglanguage, name="programinglanguage"),
    path("index/", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.Login_process, name="login"),
    path("resumepage/upload_resume/", views.upload_resume, name="upload_resume"),
    # path("list_resumes", views.list_resumes, name="list_resumes"),
    path("resume_download", views.list_resumes, name="resume_download"),
    path("interview", views.interview, name="interview"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
