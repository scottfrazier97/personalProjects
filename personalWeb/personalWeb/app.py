from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from modelHelper import ModelHelper
import pickle

#init app and class
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

#endpoint
# Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')
                          
# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")


# Route to render index.html template
@app.route("/about")
def about():
    # Return template and data
    return render_template("about.html")

# Route to render index.html template
@app.route("/glossary")
def glossary():
    # Return template and data
    return render_template("glossary.html")

# Route to render index.html template
@app.route("/prediction")
def machine():
    # Return template and data
    return render_template("mLearning.html")

# Route to render index.html template
@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tabDash.html")

#main
if __name__ == "__main__":
    app.run(debug=True)
