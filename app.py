@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form

        # get user input
        odor = data.get("odor", "")
        cap_color = data.get("cap_color", "")
        population = data.get("population", "")

        # simple deterministic "ML-like" scoring
        score = 50

        if odor == "foul":
            score += 40
        if cap_color == "green":
            score += 10
        if population == "several":
            score += 5

        # clamp score
        if score > 99:
            score = 99
        if score < 5:
            score = 5

        # result logic
        if score >= 50:
            result = "☠️ Poisonous Mushroom"
        else:
            result = "🍄 Edible Mushroom"

        return render_template(
            "index.html",
            prediction=result,
            probability=f"{score:.2f}%"
        )

    except Exception as e:
        return f"ERROR: {str(e)}"
