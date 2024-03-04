from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import views
from pyresparser import ResumeParser
from pdfminer.high_level import extract_text
from pyresparser import ResumeParser
import base64, random
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import random
from datetime import datetime
from .Courses import (
    ds_course,
    uiux_course,
    web_course,
    android_course,
    ios_course,
    resume_videos,
    interview_videos,
)


# import pafy


# def fetch_yt_video(link):
#     video = pafy.new(link)
#     return video.title


def course_recommender(course_list):
    recommendations = []
    no_of_reco = 5  # Default number of recommendations
    random.shuffle(course_list)

    for c_name, c_link in course_list[:no_of_reco]:
        recommendations.append({"name": c_name, "link": c_link})

    return recommendations


def pdf_reader(file_path):
    with open(file_path, "rb") as fh:
        text = extract_text(fh, laparams=LAParams())
    return text


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_data = f"data:application/pdf;base64,{base64_pdf}"
    return pdf_data


# def determine_candidate_level(no_of_pages):
#     if no_of_pages == 1:
#         return "Fresher"
#     elif no_of_pages == 2:
#         return "Intermediate"
#     elif no_of_pages >= 3:
#         return "Experienced"


# def experiences(total_experience):
#     return total_experience


def resume_analysis(request):
    if request.method == "POST":
        pdf_file = request.FILES["pdf_file"]
        save_image_path = "/PP/PP/resumeanalysis/Uploded_resume/" + pdf_file.name
        with open(save_image_path, "wb") as f:
            f.write(pdf_file.read())
        pdf_data = show_pdf(save_image_path)

        resume_data = ResumeParser(save_image_path).get_extracted_data()

        if resume_data:
            resume_text = pdf_reader(save_image_path)
            # cand_level = determine_candidate_level(resume_data["no_of_pages"])
            exp = resume_data["total_experience"]
            template = loader.get_template("resume_analysis.html")
            context = {
                "resume_data": resume_data,
            }
            ds_keyword = [
                "tensorflow",
                "keras",
                "pytorch",
                "machine learning",
                "deep Learning",
                "flask",
                "streamlit",
                "python",
                "django",
                "flask",
                "numpy",
                "matplotlib",
                "seaborn",
                "pandas",
            ]
            web_keyword = [
                "react",
                "django",
                "node jS",
                "react js",
                "php",
                "Front End Coding",
                "Database",
                "Website",
                "laravel",
                "magento",
                "wordpress",
                "javascript",
                "angular js",
                "c#",
                "flask",
                "webDesign",
                "wireframe",
                "laravel",
                "problem-solving",
            ]
            android_keyword = [
                "android",
                "android development",
                "flutter",
                "kotlin",
                "xml",
                "kivy",
            ]
            ios_keyword = [
                "ios",
                "ios development",
                "swift",
                "cocoa",
                "cocoa touch",
                "xcode",
            ]
            uiux_keyword = [
                "ux",
                "adobe xd",
                "figma",
                "zeplin",
                "balsamiq",
                "ui",
                "prototyping",
                "wireframes",
                "storyframes",
                "adobe photoshop",
                "photoshop",
                "editing",
                "adobe illustrator",
                "illustrator",
                "adobe after effects",
                "after effects",
                "adobe premier pro",
                "premier pro",
                "adobe indesign",
                "indesign",
                "wireframe",
                "solid",
                "grasp",
                "user research",
                "user experience",
            ]
            # recommended_skills = []
            reco_field = ""
            rec_course = ""
            recommended_skills = []

            for i in resume_data["skills"]:
                if i.lower() in ds_keyword:
                    reco_field = "Data Science"
                    recommended_skills = [
                        "Data Visualization",
                        "Predictive Analysis",
                        "Statistical Modeling",
                        "Data Mining",
                        "Clustering & Classification",
                        "Data Analytics",
                        "Quantitative Analysis",
                        "Web Scraping",
                        "ML Algorithms",
                        "Keras",
                        "Pytorch",
                        "Probability",
                        "Scikit-learn",
                        "Tensorflow",
                        "Flask",
                        "Streamlit",
                    ]
                    rec_course = course_recommender(
                        ds_course
                    )  # Pass the field to the course_recommender function
                    break
                elif i.lower() in web_keyword:
                    reco_field = "Web Development"
                    recommended_skills = [
                        "React",
                        "Django",
                        "Node JS",
                        "React JS",
                        "php",
                        "Magento",
                        "wordpress",
                        "Javascript",
                        "Angular JS",
                        "c#",
                        "Flask",
                        "SDK",
                    ]
                    rec_course = course_recommender(web_course)
                    break

                elif i.lower() in android_keyword:
                    reco_field = "Android Development"
                    recommended_skills = [
                        "Android",
                        "Android development",
                        "Flutter",
                        "Kotlin",
                        "XML",
                        "Java",
                        "Kivy",
                        "GIT",
                        "SDK",
                        "SQLite",
                    ]
                    rec_course = course_recommender(android_course)
                    break
                elif i.lower() in ios_keyword:
                    reco_field = "IOS Development"
                    recommended_skills = [
                        "IOS",
                        "IOS Development",
                        "Swift",
                        "Cocoa",
                        "Cocoa Touch",
                        "Xcode",
                        "Objective-C",
                        "SQLite",
                        "Plist",
                        "StoreKit",
                        "UI-Kit",
                        "AV Foundation",
                        "Auto-Layout",
                    ]
                    rec_course = course_recommender(ios_course)
                    break
                    ## Ui-UX Recommendation
                elif i.lower() in uiux_keyword:
                    reco_field = "UI-UX Development"
                    recommended_skills = [
                        "UI",
                        "User Experience",
                        "Adobe XD",
                        "Figma",
                        "Zeplin",
                        "Balsamiq",
                        "Prototyping",
                        "Wireframes",
                        "Storyframes",
                        "Adobe Photoshop",
                        "Editing",
                        "Illustrator",
                        "After Effects",
                        "Premier Pro",
                        "Indesign",
                        "Wireframe",
                        "Solid",
                        "Grasp",
                        "User Research",
                    ]
                    rec_course = course_recommender(uiux_course)
                    break
            # resume_text = "Sample resume text"  # Placeholder for resume text

            resume_tips = []
            resume_score = 0

            if "Objective" in resume_text:
                resume_score += 20
                resume_tips.append(
                    {
                        "message": "[+] Awesome! You have added Objective",
                        "color": "#1ed760",
                    }
                )
            else:
                resume_tips.append(
                    {
                        "message": "[-] Please add your career objective, it will give your career intention to the Recruiters.",
                        "color": "##FF0000",
                    }
                )
            if "Declaration" in resume_text:
                resume_score += 20
                resume_tips.append(
                    {
                        "message": "[+] Awesome! You have added Declaration",
                        "color": "#1ed760",
                    }
                )
            else:
                resume_tips.append(
                    {
                        "message": "[-] Please add Declaration. It will give the assurance that everything written on your resume is true and fully acknowledged by you",
                        "color": "##FF0000",
                    }
                )

            if "Hobbies" in resume_text or "Interests" in resume_text:
                resume_score += 20
                resume_tips.append(
                    {
                        "message": "[+] Awesome! You have added your Hobbies",
                        "color": "#1ed760",
                    }
                )
            else:
                resume_tips.append(
                    {
                        "message": "[-] Please add Hobbies. It will show your personality to the Recruiters and give the assurance that you are fit for this role or not.",
                        "color": "##FF0000",
                    }
                )

            if "Achievements" in resume_text:
                resume_score += 20
                resume_tips.append(
                    {
                        "message": "[+] Awesome! You have added your Achievements",
                        "color": "#1ed760",
                    }
                )
            else:
                resume_tips.append(
                    {
                        "message": "[-] Please add Achievements. It will show that you are capable for the required position.",
                        "color": "##FF0000",
                    }
                )

            if "Projects" in resume_text:
                resume_score += 20
                resume_tips.append(
                    {
                        "message": "[+] Awesome! You have added your Projects",
                        "color": "#1ed760",
                    }
                )
            else:
                resume_tips.append(
                    {
                        "message": "[-] Please add Projects. It will show that you have done work related the required position or not.",
                        "color": "##FF0000",
                    }
                )
            resume_vid = random.choice(resume_videos)
            # res_vid_title = fetch_yt_video(resume_vid)

            interview_vid = random.choice(interview_videos)
            # int_vid_title = fetch_yt_video(interview_vid)
            context = {
                "resume_data": resume_data,
                "ds_keyword": ds_keyword,
                "web_keyword": web_keyword,
                "android_keyword": android_keyword,
                "ios_keyword": ios_keyword,
                "uiux_keyword": uiux_keyword,
                "reco_field": reco_field,
                "recommended_skills": recommended_skills,
                "rec_course": rec_course,
                "resume_tips": resume_tips,
                "resume_score": resume_score,
                "pdf_data": pdf_data,
                # "cand_level": cand_level,
                # "total_experience": total_experience,
                "exp": exp,
                # "exp_user": exp_us/er,
                "resume_vid": resume_vid,
                "interview_vid": interview_vid,
            }
            return HttpResponse(template.render(context, request))

        # Render the HTML template initially
        template = loader.get_template("resume_upload.html")
        return HttpResponse(template.render({}, request))
    else:
        # Handle GET request
        # Render the initial HTML template for uploading resume
        return render(request, "resume_upload.html")
