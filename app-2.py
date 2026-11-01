"""
EV Market Performance Insights - Flask web app

Run locally:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000
"""
import os
from flask import Flask, render_template, redirect, jsonify

app = Flask(__name__)

REPO_URL = "https://github.com/MahiPatidar8/EV-Market-"
DASHBOARD_URL = (
    "https://public.tableau.com/app/profile/mahi.patidar/viz/"
    "EV_Market_Performance_Market_Story_2026-10-25_17935546350500/EVExecutiveDashboard?publish=yes"
)
STORY_URL = (
    "https://public.tableau.com/app/profile/mahi.patidar/viz/"
    "Electric_vehicle_market_12-dark_17935545109530/SalesGeography?publish=yes"
)


@app.route("/")
def home():
    """Project showcase page (templates/index.html)."""
    return render_template("index.html")


@app.route("/github")
def github():
    return redirect(REPO_URL)


@app.route("/dashboard")
def dashboard():
    return redirect(DASHBOARD_URL)


@app.route("/story")
def story():
    return redirect(STORY_URL)


@app.route("/health")
def health():
    return jsonify(status="ok", project="EV Market Performance Insights")


@app.errorhandler(404)
def not_found(_):
    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
