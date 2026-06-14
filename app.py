from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # SAFE TEST RESPONSE
        return render_template(
            "index.html",
            prediction="🍄 App Working (No ML yet)",
            probability="95.00%"
        )

    except Exception as e:
        return f"ERROR: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
