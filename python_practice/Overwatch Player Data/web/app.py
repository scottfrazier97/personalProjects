# app.py
from flask import Flask, render_template, request
from data_loader import load_data

app = Flask(__name__)
df = load_data()

@app.route("/")
def home():
    heroes = sorted(df["Hero"].unique())
    seasons = sorted(df["Season"].unique())
    stats = [col for col in df.columns if col not in ["Hero", "Season"]]
    return render_template("index.html", heroes=heroes, seasons=seasons, stats=stats)

@app.route("/filter")
def filter_data():
    hero = request.args.get("Hero")
    season = request.args.get("Season")
    stat = request.args.get("stats")

    if hero and season and stat:
        row = df[(df["Hero"] == hero) & (df["Season"] == season)]
        if not row.empty:
            value = row.iloc[0][stat]
            return f"{hero} ({season}) - {stat}: {value}"
        else:
            return "No data found!"
    else:
        return "Missing filter values!"

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)