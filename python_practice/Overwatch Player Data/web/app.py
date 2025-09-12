from flask import Flask, render_template, request, jsonify
from data_loader import load_data
import pandas as pd
import numpy as np

app = Flask(__name__)
df = load_data()

@app.route("/")
def home():
    heroes = ["All Heroes"] + sorted(df["Hero"].unique().tolist())
    seasons = ["All Seasons"] + sorted(df["Season"].unique().tolist())
    roles = ["All Roles"] + sorted(df["Role"].unique().tolist())

    stats = [col for col in df.columns if col not in ["Hero", "Season", "Role"]]
    return render_template("index.html", heroes=heroes, seasons=seasons, stats=stats, roles=roles)

@app.route("/filter")
def filter_data():
    hero = request.args.get("hero", "All Heroes")
    season = request.args.get("season", "All Seasons")
    role = request.args.get("role", "All Roles")
    stat = request.args.get("stat")

    if not stat:
        return "Missing filter values!"

    filtered = df.copy()

    if hero != "All Heroes":
        filtered = filtered[filtered["Hero"] == hero]
    if season != "All Seasons":
        filtered = filtered[filtered["Season"] == season]
    if role != "All Roles":
        filtered = filtered[filtered["Role"] == role]

    if filtered.empty:
        return "No data found!"

    total = filtered[stat].sum()
    if hasattr(total, "item"):
        total = total.item()
    if isinstance(total, (int, float)):
        total = f"{total:,}"

    # Build label dynamically based on filters
    labels = []
    if hero != "All Heroes":
        labels.append(hero)
    if season != "All Seasons":
        labels.append(season)
    if role != "All Roles":
        labels.append(role)

    label_str = " - ".join(labels) if labels else "All Data"
    return f"{label_str} - {stat}: {total}"

@app.route("/options")
def get_options():
    hero = request.args.get("hero")
    season = request.args.get("season")
    role = request.args.get("role")
    
    filtered = df.copy()
    
    # Apply filters if provided
    if hero and hero != "All Heroes":
        filtered = filtered[filtered["Hero"] == hero]
    if season and season != "All Seasons":
        filtered = filtered[filtered["Season"] == season]
    if role and role != "All Roles":
        filtered = filtered[filtered["Role"] == role]

    seasons = sorted(filtered["Season"].dropna().unique().tolist())
    roles = sorted(filtered["Role"].dropna().unique().tolist())
    stats = [col for col in filtered.columns if col not in ["Hero", "Season", "Role"] and filtered[col].notna().any()]

    return jsonify({"seasons": seasons, "roles": roles, "stats": stats})

@app.route("/chart_data")
def chart_data():
    hero = request.args.get("hero", "All Heroes")
    role = request.args.get("role", "All Roles")
    stat = request.args.get("stat")

    if not stat:
        return jsonify({"error": "Missing filters"}), 400

    filtered = df.copy()
    if hero != "All Heroes":
        filtered = filtered[filtered["Hero"] == hero]
    if role != "All Roles":
        filtered = filtered[filtered["Role"] == role]

    grouped = filtered.groupby("Season")[stat].sum().reset_index()
    grouped = grouped.sort_values("Season")

    return jsonify({
        "labels": grouped["Season"].tolist(),
        "values": grouped[stat].tolist()
    })

@app.route('/summary')
def summary():
    hero = request.args.get("hero", "All Heroes")
    season = request.args.get("season", "All Seasons")
    role = request.args.get("role", "All Roles")
    stat = request.args.get("stat")

    if not stat:
        return jsonify({"error": "Missing filter values!"}), 400

    # Filter the dataframe
    df_filtered = df.copy()
    if hero != "All Heroes":
        df_filtered = df_filtered[df_filtered["Hero"] == hero]
    if season != "All Seasons":
        df_filtered = df_filtered[df_filtered["Season"] == season]
    if role != "All Roles":
        df_filtered = df_filtered[df_filtered["Role"] == role]

    if df_filtered.empty or df_filtered[stat].dropna().empty:
        return jsonify({"error": "No data"})

    # Use pandas describe to get summary stats
    desc = df_filtered[stat].describe()  # returns a Series

    # Format the stats: round to 2 decimals and add commas for large numbers
    def format_number(x):
        if pd.isna(x):
            return None
        if isinstance(x, (int, float)):
            return f"{x:,.2f}"
        return x

    summary_stats = {
        "count": int(desc["count"]),
        "mean": format_number(desc["mean"]),
        "std": format_number(desc["std"]),
        "min": int(desc["min"]),
        "q1": int(desc["25%"]),
        "median": int(desc["50%"]),
        "q3": int(desc["75%"]),
        "max": int(desc["max"])
    }

    return jsonify(summary_stats)

if __name__ == "__main__":
    app.run(debug=True)
