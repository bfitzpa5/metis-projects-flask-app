# api/views.py
from flask import render_template, abort, request, Blueprint, send_from_directory
from flask.json import jsonify
from metis_app.api.nhl_game_results_scrape import nhl_scrape
from flask import jsonify
import datetime as dt
import os
from metis_app.api.yield_curve import get_yield_curve
from metis_app.api.sp_500_weighting import scrape_sp_500_weighting_data
from metis_app.ml_models.pickle_imports import aws_download
import json

ALLOWED_EXCEL_FILENAME = [
    'S&P 500 Time Horizon Analysis.xlsx',
    'S&P 500 Visualizations.xlsx',
    'Workout_Log.xlsx',
]
EXCEL_DIRECTORY = os.path.join('static', 'excels')

api = Blueprint('api', __name__)

@api.route('/nhl_results')
def nhl_results():
    basedir = os.path.join('metis_app', 'api', 'static', 'api', 'data')
    season_end = dt.date(2020, 4, 4)

    if dt.date.today() > season_end:
        filename = f"nhl_results_{season_end}.json"
        if not os.path.isfile(filename):
            aws_download(filename, bucket_directory=None, local_directory=basedir)

        filename = os.path.join(basedir, filename)
        with open(filename, 'r') as f:
            data = json.load(f)
    else:
        today = dt.datetime.today().strftime('%Y%m%d')
        filename = os.path.join(basedir, f"nhl_results_{today}.json")

        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                print(filename)
                data = json.load(f)
        else:
            if not os.path.isdir(basedir):
                os.makedirs(basedir)

            data = nhl_scrape()

            with open(filename, 'w') as f:
                json.dump(data, f)

    return jsonify(data)

@api.route('/yield_curve/<year>')
def yield_curve(year):
    data = get_yield_curve(year)
    return jsonify(data)


@api.route('/excels/<filename>')
def excel_downloads(filename):
    if filename not in ALLOWED_EXCEL_FILENAME:
        abort(404)
    return send_from_directory(EXCEL_DIRECTORY, filename, as_attachment=True)

@api.route('/s&p500_weighting')
def sp_500_weighting_view():
    data = scrape_sp_500_weighting_data()
    return jsonify(data)
