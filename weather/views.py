import requests
import when

from flask import abort, jsonify, make_response

from . import app

@app.route("/")
def root():
    """ Renders the default index page """
    return make_response(open('weather/templates/index.html').read())

@app.route("/api/forecast/")
@app.route("/api/forecast/<lat>/<lng>/")
def forecast(lat=None, lng=None):
    """ Returns the weather for a specific location"""

    if not lat or not lng:
        abort(400)

    root = app.config.get('FORECASTIO_ROOT')
    key = app.config.get('FORECASTIO_API_KEY')
    timestamp = when.format(when.now(), '%Y-%m-%dT%H:%M:%S')

    url = root + key + "/" + lat + ", " + lng + ", " + timestamp

    r = requests.get(url)

    if r.ok:
        return jsonify(r.json())
    else:
        return jsonify({})

# Errors
@app.errorhandler(400)
def bad_request(e):
    """ Returns a 400 Bad Request """
    return jsonify(
        {
            "status": "400",
            "error": e.name,
            "description": e.description,
        }
    ), 400

@app.errorhandler(404)
def page_not_found(e):
    """ Returns a 404 Page not found """
    return jsonify(
        {
            "status": "404",
            "error": e.name,
            "description": e.description,
        }
    ), 404 