from django.shortcuts import render
from joblib import load
import numpy as np

# Load the machine learning model
# model = load("./savedmodels/model.joblib")
model = load("./savedmodels/rf.joblib")


def prediction(request):
    if request.method == "POST":
        # Retrieve input data from the POST request
        Age = float(request.POST["Age"])
        Gender = request.POST["Gender"]  # Assuming 'male' or 'female'
        Stream = int(request.POST["Stream"])  # Convert 'Stream' directly to integer
        Internships = float(request.POST["Internships"])
        CGPA = float(request.POST["CGPA"])

        # Convert 'Hostel' to integer (0 for 'No', 1 for 'Yes')
        Hostel = 1 if request.POST["Hostel"] == "Yes" else 0

        HistoryOfBacklogs = float(request.POST["HistoryOfBacklogs"])

        # Map gender to numerical value
        gender_map = {"male": 1, "female": 0}
        Gender = gender_map.get(
            Gender.lower(), -1
        )  # Default to -1 if gender not recognized

        # Make prediction
        input_data = np.array(
            [[Age, Gender, Stream, Internships, CGPA, Hostel, HistoryOfBacklogs]]
        )
        y_pred = model.predict(input_data)

        # Perform logic based on prediction
        if y_pred >= 1 and HistoryOfBacklogs == 0 and Internships >= 2:
            result = "Placed"
        elif 0.6 < y_pred < 1 and HistoryOfBacklogs == 0 and Internships > 0:
            result = "Maybe Placed"
        else:
            result = "Not Placed"

        if HistoryOfBacklogs > 0:
            backans = "WE recommend you to clear all the backlogs "
        else:
            backans = ""

        if Internships < 2:
            Internshipsans = "WE recommend you to increase number of internships"
        else:
            Internshipsans = ""

        if CGPA < 7:
            cgpaans = (
                "WE recommend you to try increase your CGPA for campus opportunities "
            )
        else:
            cgpaans = ""

        return render(
            request,
            "predictions.html",
            {
                "result": result,
                "ans": y_pred,
                "backans": backans,
                "internshipsans": Internshipsans,
                "cgpaans": cgpaans,
            },
        )

    return render(request, "predictions.html")
