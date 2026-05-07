import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

# ====================================================
# LOAD DATASET
# ====================================================

df = pd.read_csv(
    "datasets/merged_dataset.csv"
)

# ====================================================
# INPUT FEATURES
# ====================================================

X = df[[

    "Attendance",

    "AssignmentCompletion",

    "ExamScore",

    "StudyHours",

    "Motivation",

    "StressLevel"
]]

# ====================================================
# TARGET
# ====================================================

y = df["FinalGrade"]

# ====================================================
# TRAIN TEST SPLIT
# ====================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42
)

# ====================================================
# TRAIN MODEL
# ====================================================

model = RandomForestClassifier()

model.fit(
    X_train,
    y_train
)

# ====================================================
# PREDICTION FUNCTION
# ====================================================

def predict_student(

    attendance,

    assignment,

    exam_score,

    study_hours,

    motivation,

    stress
):

    prediction = model.predict([[
        attendance,
        assignment,
        exam_score,
        study_hours,
        motivation,
        stress
    ]])

    grade = int(prediction[0])

    # ============================================
    # AI INSIGHTS
    # ============================================

    insight = "Good academic performance."

    risk = "Low"

    if grade >= 3:

        risk = "High"

        insight = (
            "Student requires academic attention."
        )

    elif grade == 2:

        risk = "Medium"

        insight = (
            "Performance is average."
        )

    return {

        "predicted_grade":
            grade,

        "risk":
            risk,

        "insight":
            insight
    }