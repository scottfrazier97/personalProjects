from flask import Flask, render_template, request, jsonify
from data_loader import load_data
import pandas as pd

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

    return f"{stat}: {total}"

@app.route("/options")
def get_options():
    hero = request.args.get("hero")
    season = request.args.get("season")
    role = request.args.get("role")
    
    filtered = df.copy()
    
    # Filter by Hero and Role, but **not by Season** when generating seasons
    if hero and hero != "All Heroes":
        filtered_for_seasons = filtered[filtered["Hero"] == hero]
    else:
        filtered_for_seasons = filtered.copy()
    if role and role != "All Roles":
        filtered_for_seasons = filtered_for_seasons[filtered_for_seasons["Role"] == role]
    
    # Filter by Hero and Season, but not by Role when generating roles
    if hero and hero != "All Heroes":
        filtered_for_roles = filtered[filtered["Hero"] == hero]
    else:
        filtered_for_roles = filtered.copy()
    if season and season != "All Seasons":
        filtered_for_roles = filtered_for_roles[filtered_for_roles["Season"] == season]
    
    # Filter by Role and Season, but not by Hero when generating heroes
    if role and role != "All Roles":
        filtered_for_heroes = filtered[filtered["Role"] == role]
    else:
        filtered_for_heroes = filtered.copy()
    if season and season != "All Seasons":
        filtered_for_heroes = filtered_for_heroes[filtered_for_heroes["Season"] == season]

    heroes = ["All Heroes"] + sorted(filtered_for_heroes["Hero"].dropna().unique().tolist())
    roles = ["All Roles"] + sorted(filtered_for_roles["Role"].dropna().unique().tolist())
    seasons = ["All Seasons"] + sorted(filtered_for_seasons["Season"].dropna().unique().tolist())

    stats = [col for col in filtered.columns if col not in ["Hero", "Season", "Role"] and filtered[col].notna().any()]

    return jsonify({"heroes": heroes, "roles": roles, "seasons": seasons, "stats": stats})


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

if __name__ == "__main__":
    app.run(debug=True)
