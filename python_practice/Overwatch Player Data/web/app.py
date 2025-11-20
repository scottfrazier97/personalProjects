from flask import Flask, render_template, request, jsonify
from data_loader import load_data

app = Flask(__name__)
df = load_data()

@app.route("/")
def home():
    heroes = ["All Heroes"] + sorted(df["Hero"].unique().tolist())
    seasons = ["All Seasons"] + sorted(df["Season"].unique().tolist())
    roles = ["All Roles"] + sorted(df["Role"].unique().tolist())

    stats = [col for col in df.columns if col not in ["Hero", "Season", "Role"]]
    return render_template("index.html", heroes=heroes, seasons=seasons, stats=stats, roles=roles)

@app.route("/predictions")
def predictions():
    # If you need dropdowns later, you can pass them here
    heroes = ["All Heroes"] + sorted(df["Hero"].unique().tolist())
    stats = [col for col in df.columns if col not in ["Hero", "Season", "Role"]]
    return render_template("predictions.html", heroes=heroes, stats=stats)



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

    # Only apply filters on dimensions NOT currently being updated
    # We'll return valid options for all dropdowns independently

    # Hero options depend on Role and Season only (not Hero itself)
    hero_filtered = filtered.copy()
    
    if role and role != "All Roles":
        hero_filtered = hero_filtered[hero_filtered["Role"] == role]

    if season and season != "All Seasons":
        hero_filtered = hero_filtered[hero_filtered["Season"] == season]
        
    heroes_valid = sorted(hero_filtered["Hero"].dropna().unique().tolist())
    heroes_all = ["All Heroes"] + sorted(df["Hero"].unique().tolist())

    # Role options depend on Hero and Season only

    role_filtered = filtered.copy()

    if hero and hero != "All Heroes":
        role_filtered = role_filtered[role_filtered["Hero"] == hero]

    if season and season != "All Seasons":
        role_filtered = role_filtered[role_filtered["Season"] == season]

    roles_valid = sorted(role_filtered["Role"].dropna().unique().tolist())
    roles_all = ["All Roles"] + sorted(df["Role"].unique().tolist())

    # Season options depend on Hero and Role only
    season_filtered = filtered.copy()

    if hero and hero != "All Heroes":
        season_filtered = season_filtered[season_filtered["Hero"] == hero]

    if role and role != "All Roles":
        season_filtered = season_filtered[season_filtered["Role"] == role]

    seasons_valid = sorted(season_filtered["Season"].dropna().unique().tolist())
    seasons_all = ["All Seasons"] + sorted(df["Season"].unique().tolist())

    # Stats always fully available
    stats = [col for col in df.columns if col not in ["Hero", "Season", "Role"] and filtered[col].notna().any()]

    return jsonify({
        "heroes": {"all": heroes_all, "valid": heroes_valid},
        "roles": {"all": roles_all, "valid": roles_valid},
        "seasons": {"all": seasons_all, "valid": seasons_valid},
        "stats": stats
    })

@app.route("/chart_data")
def chart_data():
    hero = request.args.get("hero", "All Heroes")
    role = request.args.get("role", "All Roles")
    stat = request.args.get("stat")
    season = request.args.get("season", "All Seasons")

    if not stat:
        return jsonify({"error": "Missing filters"}), 400

    # --- Apply ALL filters first (same logic as /filter) ---
    filtered = df.copy()

    if hero != "All Heroes":
        filtered = filtered[filtered["Hero"] == hero]

    if role != "All Roles":
        filtered = filtered[filtered["Role"] == role]

    if season != "All Seasons":
        filtered = filtered[filtered["Season"] == season]

    if filtered.empty:
        return jsonify({"labels": [], "datasets": []})

    # --- CASE 1: User chose a specific hero ---
    if hero != "All Heroes":
        grouped = filtered.groupby("Season")[stat].sum().reset_index()
        grouped = grouped.sort_values("Season")

        return jsonify({
            "labels": grouped["Season"].tolist(),
            "datasets": [{
                "label": hero,
                "data": grouped[stat].astype(float).tolist()
            }]
        })

    # --- CASE 2: All heroes, but specific role ---
    if role != "All Roles":
        grouped = filtered.groupby("Season")[stat].sum().reset_index()
        grouped = grouped.sort_values("Season")

        return jsonify({
            "labels": grouped["Season"].tolist(),
            "datasets": [{
                "label": role,
                "data": grouped[stat].astype(float).tolist()
            }]
        })

    # --- CASE 3: All heroes + all roles → break down by Role ---
    grouped = filtered.groupby(["Season", "Role"])[stat].sum().reset_index()
    labels = sorted(filtered["Season"].unique())
    datasets = []

    for role_name in grouped["Role"].unique():
        role_data = grouped[grouped["Role"] == role_name]
        role_data = role_data.set_index("Season")

        datasets.append({
            "label": role_name,
            "data": [
                float(role_data.loc[s, stat]) if s in role_data.index else 0
                for s in labels
            ]
        })

    return jsonify({
        "labels": labels,
        "datasets": datasets
    })


# TABLE
@app.route("/table")
def table_page():
    return render_template("table.html")  # HTML PAGE

# Convert DF to list of dicts for fast JSON API use
hero_stats_data = df.to_dict(orient="records")

@app.route("/hero_stats")
def hero_stats():
    return jsonify(hero_stats_data)  # JSON API

if __name__ == "__main__":
    app.run(debug=True)