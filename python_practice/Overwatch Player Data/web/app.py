from flask import Flask, render_template, request, jsonify
from data_loader import load_data
import pandas as pd

app = Flask(__name__)
df = load_data()

@app.route("/")
def home():
    heroes = ["All Heroes"] + sorted(df["Hero"].unique().tolist())
    seasons = ["All Seasons"] + sorted(df["Season"].unique().tolist())
    stats = [col for col in df.columns if col not in ["Hero", "Season", "Role"]]
    return render_template("index.html", heroes=heroes, seasons=seasons, stats=stats)

@app.route("/filter")
def filter_data():
    hero = request.args.get("hero")
    season = request.args.get("season")
    stat = request.args.get("stat")

    if hero and season and stat:
        # Start with full dataset
        filtered = df.copy()

        # Apply filters only if not "All"
        if hero != "All Heroes":
            filtered = filtered[filtered["Hero"] == hero]
        if season != "All Seasons":
            filtered = filtered[filtered["Season"] == season]

        if not filtered.empty:
            # Sum across remaining rows
            total = filtered[stat].sum()

            # Convert numpy scalar to Python type
            if hasattr(total, "item"):
                total = total.item()

            # Format with commas if numeric
            if isinstance(total, (int, float)):
                total = f"{total:,}"

            # Label depends on scope
            hero_label = hero if hero != "All Heroes" else "All Heroes"
            season_label = season if season != "All Seasons" else "All Seasons"

            return f"{hero_label} ({season_label}) - {stat}: {total}"

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

@app.route("/chart_data")
def chart_data():
    hero = request.args.get("hero")
    stat = request.args.get("stat")

    if not hero or not stat:
        return jsonify({"error": "Missing filters"}), 400

    filtered = df.copy()

    if hero != "All Heroes":
        # Single hero selected
        filtered = filtered[filtered["Hero"] == hero]

    # Always group by Season
    grouped = filtered.groupby("Season")[stat].sum().reset_index()

    # Sort by Season (optional, if your seasons are numeric or ordered labels)
    grouped = grouped.sort_values("Season")

    labels = grouped["Season"].tolist()
    values = grouped[stat].tolist()

    return jsonify({"labels": labels, "values": values})



if __name__ == "__main__":
    app.run(debug=True)
