# -*- coding: utf-8 -*-
"""
Weather App
======

"""

from config import Config
from flask import Flask

app = Flask(__name__)

# load the default config object. The object is configured to load default or
# load os.environ.get()
app.config.from_object(Config)

# this try block allows local development settings to be set
try:
    app.config.from_pyfile('local_settings.cfg')
except (RuntimeError, IOError):
    # local settings are not found, we can pass
    pass

from . import views