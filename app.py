from flask import Flask, render_template, request

# -----------------------------
# APP INIT (MUST BE FIRST)
# -----------------------------
app = Flask(__name__)


# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# PREDICT ROUTE (SAFE DEMO)
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        odor = request.form.get("odor", "")

        # simple working logic
        if odor == "foul":
            result = "☠️ Poisonous Mushroom"
            probability = 97.0
        else:
            result = "🍄 Edible Mushroom"
            probability = 90.0

        return render_template(
            "index.html",
            prediction=result,
            probability=f"{probability:.2f}%"
        )

    except Exception as e:
        return f"ERROR: {str(e)}"


# -----------------------------
# RUN (RENDER SAFE)
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
