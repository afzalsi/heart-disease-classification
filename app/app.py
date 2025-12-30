from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("../model/heart_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        data = {
            "Age": int(request.form["Age"]),
            "Sex": request.form["Sex"],
            "ChestPainType": request.form["ChestPainType"],
            "RestingBP": int(request.form["RestingBP"]),
            "Cholesterol": int(request.form["Cholesterol"]),
            "FastingBS": int(request.form["FastingBS"]),
            "RestingECG": request.form["RestingECG"],
            "MaxHR": int(request.form["MaxHR"]),
            "ExerciseAngina": request.form["ExerciseAngina"],
            "Oldpeak": float(request.form["Oldpeak"]),
            "ST_Slope": request.form["ST_Slope"]
        }

        df = pd.DataFrame([data])
        result = model.predict(df)[0]
        prediction = "YES (Heart Disease)" if result == 1 else "NO (Healthy)"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
