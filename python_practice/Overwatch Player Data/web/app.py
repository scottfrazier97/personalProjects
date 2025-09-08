from flask import Flask, render_template, request, jsonify
from data_loader import load_data

app = Flask(__name__)
df = load_data()

@app.route("/")
def home():
    heroes = sorted(df["Hero"].unique())
    seasons = sorted(df["Season"].unique())
    stats = [col for col in df.columns if col not in ["Hero", "Season", "Role"]]
    return render_template("index.html", heroes=heroes, seasons=seasons, stats=stats)

@app.route("/filter")
def filter_data():
    hero = request.args.get("hero")
    season = request.args.get("season")
    stat = request.args.get("stat")

    if hero and season and stat:
        row = df[(df["Hero"] == hero) & (df["Season"] == season)]
        if not row.empty:
            value = row.iloc[0][stat]

            # Convert numpy scalar to Python type
            if hasattr(value, "item"):
                value = value.item()

            # Add thousands separator if numeric
            if isinstance(value, (int, float)):
                value = f"{value:,}"

            return f"{hero} ({season}) - {stat}: {value}"
        else:
            return "No data found!"
    else:
        return "Missing filter values!"

@app.route("/options")
def get_options():
    hero = request.args.get("hero")
    season = request.args.get("season")

    filtered = df.copy()

    # Only filter down by one dimension if provided
    if hero and not season:
        filtered = df[df["Hero"] == hero]
    elif season and not hero:
        filtered = df[df["Season"] == season]
    elif hero and season:
        # Keep all data for that hero, but note the chosen season
        filtered = df[df["Hero"] == hero]

    # Build dropdowns
    seasons = sorted(filtered["Season"].dropna().unique().tolist())
    stats = [
        col for col in filtered.columns
        if col not in ["Hero", "Season", "Role"] and filtered[col].notna().any()
    ]

    return jsonify({"seasons": seasons, "stats": stats})



if __name__ == "__main__":
    app.run(debug=True)
