from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import firebase_admin
from firebase_admin import credentials, storage
from datetime import timedelta

from django.urls import reverse
from django.shortcuts import render, redirect
from firebase_admin import storage


def welcome(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def Resume(request):
    return render(request, "Resume.html")


def Signup(request):
    return render(request, "sign_up.html")


def upload_resume(request):
    if request.method == "POST" and "uploadresume" in request.FILES:
        upload_resume = request.FILES["uploadresume"]
        # if request.method == "POST" and request.FILES["uploadresume"]:
        # upload_resume = request.FILES["uploadresume"]
        bucket = storage.bucket(settings.FIREBASE_STORAGE_BUCKET)
        # Store user's resume in Firebase Storage
        filename = upload_resume.name
        blob = bucket.blob(f"userresume/{filename}")
        blob.upload_from_file(upload_resume)

        context = {"resume_uploaded": True}
    else:
        context = {"resume_uploaded": False}

    return render(request, "Resume.html", context)


def list_resumes(request):
    # Assuming resumes are stored in a folder named 'templateresume' in Firebase Storage
    # Access Firebase Storage
    bucket = storage.bucket("resumedjango.appspot.com")

    # List all resume files in Firebase Storage
    blobs = bucket.list_blobs(
        prefix="templateresume/"
    )  # Assuming resumes are stored in a 'templateresume' folder
    resume_files = [blob.name for blob in blobs if blob.name.endswith(".pdf")]

    # Base URL for resume files
    base_url = "https://storage.googleapis.com/resumedjango.appspot.com/"

    # Generate URLs for resume files
    resume_urls = [base_url + file_name for file_name in resume_files]

    # Render a template with links to all resume files
    context = {"resume_files": zip(resume_files, resume_urls)}
    return render(request, "resume_list.html", context)
