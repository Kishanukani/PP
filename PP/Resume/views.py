from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from firebase_admin import storage

from django.urls import reverse
from django.shortcuts import render, redirect
from firebase_admin import storage

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def welcome(request):
    return render(request, "index2.html")


def index(request):
    return render(request, "index.html")


def Resume(request):
    return render(request, "Resume.html")


def placementprediction(request):
    return render(request, "placementprediction.html")


def learning(request):
    return render(request, "learning.html")


def links(request):
    return render(request, "links.html")


def Signup(request):
    return render(request, "sign_up.html")

def webdevelopment(request):
    return render(request, "Web_Development.html")


# def upload_resume(request):
#     if request.method == "POST" and "uploadresume" in request.FILES:
#         upload_resume = request.FILES["uploadresume"]
#         # if request.method == "POST" and request.FILES["uploadresume"]:
#         # upload_resume = request.FILES["uploadresume"]
#         bucket = storage.bucket(settings.FIREBASE_STORAGE_BUCKET)
#         # Store user's resume in Firebase Storage
#         filename = upload_resume.name
#         blob = bucket.blob(f"userresume/{filename}")
#         blob.upload_from_file(upload_resume)

#         context = {"resume_uploaded": True}
#     else:
#         context = {"resume_uploaded": False}

#     return render(request, "Resume.html", context)


from firebase_admin import storage


def upload_resume(request):
    error_message = None  # Initialize error message variable

    if request.method == "POST":
        # Check if the file is not uploaded
        if "uploadresume" not in request.FILES:
            error_message = "Please select a file to upload."
            context = {"error_message": error_message}
            return render(request, "Resume.html", context)

        # Get the uploaded resume file
        upload_resume = request.FILES["uploadresume"]

        # Check if the file is a PDF
        if not upload_resume.name.endswith(".pdf"):
            # If the file is not a PDF, set the error message
            error_message = "Only PDF files are allowed for upload."
            context = {"resume_uploaded": False, "error_message": error_message}
            return render(request, "Resume.html", context)

        # Get the selected job role from the form
        try:
            job_role = request.POST["job_role"]
        except KeyError:
            # If no job role is selected, set the error message
            error_message = "Please select a job role."
            context = {"resume_uploaded": False, "error_message": error_message}
            return render(request, "Resume.html", context)

        # Define the filename with extension
        filename = f"{job_role}_{upload_resume.name}.pdf"

        # Upload the resume to Firebase Storage with metadata
        bucket = storage.bucket(settings.FIREBASE_STORAGE_BUCKET)
        blob = bucket.blob(f"templateresume/{filename}")

        # Set content type metadata
        blob.content_type = "application/pdf"

        # Upload the file
        blob.upload_from_file(upload_resume)

        # Set context for template rendering
        context = {"resume_uploaded": True}
    else:
        # If it's not a POST request, set context accordingly
        context = {"resume_uploaded": False}

    return render(request, "Resume.html", context)


def list_resumes(request):
    # Assuming resumes are stored in a folder named 'templateresume' in Firebase Storage
    # Access Firebase Storage
    bucket = storage.bucket("resumedjango.appspot.com")

    # List all resume files in Firebase Storage
    blobs = list(
        bucket.list_blobs(prefix="templateresume/")
    )  # Convert iterator to a list

    # Extract file paths and names
    resume_files_with_paths = [
        blob.name for blob in blobs if blob.name.endswith(".pdf")
    ]
    resume_files = [file.split("/")[-1] for file in resume_files_with_paths]

    # Base URL for resume files
    base_url = "https://storage.googleapis.com/resumedjango.appspot.com/"

    # Generate URLs for resume files
    resume_urls = [base_url + file_path for file_path in resume_files_with_paths]

    # Render a template with links to all resume files
    context = {"resume_files": zip(resume_files, resume_urls)}
    return render(request, "Resume_download.html", context)


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 != pass2:
            return HttpResponse(
                "Your password is incorrect and confirm password are not same"
            )
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            return redirect("login")
    return render(request, "signup.html")


def Login_process(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            return HttpResponse("Username and Password are incorrect")
    return render(request, "signup.html")
