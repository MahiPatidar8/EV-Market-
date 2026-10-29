import json
import os
from flask import Flask, render_template

app = Flask(__name__)

DEFAULTS = {
    "title": "EV Market Analysis",
    "tagline": "What 300,000 electric vehicles say about range, price and charging.",
    "github_url": "https://github.com/MahiPatidar8/EV-Market-",
    # Paste your Tableau Public links in config.json (or set env vars below).
    "dashboard_url": "",
    "story_url": "",
}


def load_config():
    cfg = dict(DEFAULTS)
    path = os.path.join(os.path.dirname(__file__), "config.json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            cfg.update({k: v for k, v in json.load(f).items() if v})
    for key in ("github_url", "dashboard_url", "story_url"):
        env = os.environ.get(key.upper())
        if env:
            cfg[key] = env
    return cfg


@app.route("/")
def index():
    return render_template("index.html", c=load_config())


if __name__ == "__main__":
    app.run(debug=True)
