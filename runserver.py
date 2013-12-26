#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Runserver
---------
This module is used to run the application with Flasks built in WSGI server.
Should NOT be used in production.

"""

from weather import app

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)