from flask import Flask, render_template, request

app = Flask(__name__)

# -----------------------------
# HOME PAGE
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# PREDICT ROUTE (RESUME SAFE VERSION)
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # read form data (just to show input works)
        data = request.form

        # simple demo logic (safe + stable)
        odor = data.get("odor", "")

        # fake ML behavior (resume demo)
        if odor == "foul":
            result = "☠️ Poisonous Mushroom"
            probability = 97.5
        else:
            result = "🍄 Edible Mushroom"
            probability = 92.3

        return render_template(
            "index.html",
            prediction=result,
            probability=f"{probability:.2f}%"
        )

    except Exception as e:
        return f"ERROR: {str(e)}"


# -----------------------------
# RUN APP (IMPORTANT FOR RENDER)
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
