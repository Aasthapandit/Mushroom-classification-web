from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # TEMP TEST ONLY (no ML)
        probability = 95.0

        if probability >= 50:
            result = "☠️ Poisonous Mushroom"
        else:
            result = "🍄 Edible Mushroom"

        return render_template(
            "index.html",
            prediction=result,
            probability=f"{probability:.2f}%"
        )

    except Exception as e:
        return f"ERROR: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
