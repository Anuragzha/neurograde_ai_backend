from flask import Flask
from flask import request
from flask import jsonify

from model import predict_student

app = Flask(__name__)

# ====================================================
# HOME ROUTE
# ====================================================

@app.route("/")

def home():

    return "NeuroGrade AI Backend Running"

# ====================================================
# AI PREDICTION ROUTE
# ====================================================

@app.route("/predict", methods=["POST"])

def predict():

    data = request.json

    result = predict_student(

        data["attendance"],

        data["assignment"],

        data["exam_score"],

        data["study_hours"],

        data["motivation"],

        data["stress"]
    )

    return jsonify(result)

# ====================================================
# RUN SERVER
# ====================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )