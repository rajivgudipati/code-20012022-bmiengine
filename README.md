BMI Engine API
BMI Engine API, developed in programming language, Flask Framework and used Pandas, Numpy & PyYml .

Project Entry Point & Main Module:
bmi_controller.py

Command to run BMIEngine:
>>python bmi_controller.py

Current Endpoint Features

Endpoint	HTTP Method	Method	Result
/api/v1/bmiengine/calculatebmi	POST	calculate and populate bmi catg and health risk of each patient and returns in response
/api/v1/bmiengine/calculatestats	POST	Gives back summary of the patients info that was feed into the api

Example:

Endpoint:
POST http://127.0.0.1:8090/api/v1/bmiengine/calculatestats

Input:
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 40 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

Output:
{
    "Very severely obese": 4,
    "Normal weight": 1,
    "Severely obese": 1,
    "Very high risk": 4,
    "Low risk": 1,
    "High risk": 1
}

Endpoint:
POST http://127.0.0.1:8090/api/v1/bmiengine/calculatebmi

Input:
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 40 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

Output:
[
    {
        "Gender": "Male",
        "HeightCm": 171,
        "WeightKg": 96,
        "bmi": 56.14,
        "bmi_catg": "Very severely obese",
        "health_risk": "Very high risk"
    },
    {
        "Gender": "Male",
        "HeightCm": 161,
        "WeightKg": 40,
        "bmi": 24.84,
        "bmi_catg": "Normal weight",
        "health_risk": "Low risk"
    },
    {
        "Gender": "Male",
        "HeightCm": 180,
        "WeightKg": 77,
        "bmi": 42.78,
        "bmi_catg": "Very severely obese",
        "health_risk": "Very high risk"
    },
    {
        "Gender": "Female",
        "HeightCm": 166,
        "WeightKg": 62,
        "bmi": 37.35,
        "bmi_catg": "Severely obese",
        "health_risk": "High risk"
    },
    {
        "Gender": "Female",
        "HeightCm": 150,
        "WeightKg": 70,
        "bmi": 46.67,
        "bmi_catg": "Very severely obese",
        "health_risk": "Very high risk"
    },
    {
        "Gender": "Female",
        "HeightCm": 167,
        "WeightKg": 82,
        "bmi": 49.1,
        "bmi_catg": "Very severely obese",
        "health_risk": "Very high risk"
    }
]
