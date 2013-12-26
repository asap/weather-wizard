# -*- coding: utf-8 -*-
"""
Application Config
------------------
Application config houses settings needed by the application. This module
uses os.environ() function to first look for these value from os ENV and
if not available may (or may not!) default to a value. This module is a
good place to place all global variables.

"""


from os import environ


class Config(object):
    """ config """

    # Flask will suppress any server error with a generic error page unless
    # it is in debug mode. As such to enable just the interactive debugger
    # without the code reloading, you have to invoke run() with debug=True
    # and use_reloader=False. Setting use_debugger to True without being in
    # debug mode won’t catch any exceptions because there won’t be any to
    # catch.
    USE_RELOADER = environ.get('USE_RELOADER', False)
    DEBUG = environ.get('DEBUG', False)
    TESTING = environ.get('TESTING', False)

    FORECASTIO_API_KEY = environ.get('FORECASTIO_API_KEY')
    FORECASTIO_ROOT = environ.get('FORECASTIO_ROOT')