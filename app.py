from flask import Flask, render_template, request, redirect, url_for, session
from luhn import generate_card_number
import random

app = Flask(__name__)
app.secret_key = "any_secret_string"  # cần thiết cho session

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        bin_input = request.form.get("bin", "")[:12]
        count = int(request.form.get("count", 10))
        include_cvv = request.form.get("cvv") == "on"
        include_exp = request.form.get("exp") == "on"

        cards = []
        for _ in range(count):
            card_number = generate_card_number(bin_input)
            exp_month = str(random.randint(1, 12)).zfill(2)
            exp_year = str(random.randint(24, 30))
            cvv = str(random.randint(100, 999))

            parts = [card_number]
            if include_exp:
                parts.extend([exp_month, exp_year])
            if include_cvv:
                parts.append(cvv)
            cards.append("|".join(parts))

        session['cards'] = cards
        return redirect(url_for("index"))

    cards = session.pop('cards', [])
    return render_template("index.html", cards=cards)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
