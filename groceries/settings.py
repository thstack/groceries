#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: SimonLuo <simonluo@thstack.com>


"""

type: file/dir
"""


TEMPLATES = {
    "web": {                # Type
        "simple_html": {    # Name
            "g_key": "t:web:simple_html",
            "alias": "Simple Html Temlate",
            "type": "file",
            "dirname": "web/",
            "filename": ["simple.html"]
        },
        "simple_css": {
            "g_key": "web:simple_css",
            "alias": "Simple Css",
            "type": "file",
            "dirname": "web/",
            "filename": ["simple.css"]
        },
        "simple_js": {
            "g_key": "web:simple_js",
            "alias": "",
            "type": "file",
            "dirname": "web/",
            "filename": ["simple.js"]
        },
        "simple_web": {
            "name": "",
            "g_key": "web:simple_web",
            "type": "dir",
            "dirname": "web/simple-web/",
            "filename": ["index.html", "main.js", "style.css"]
        }
    },
    "shell": {
        "simple_bash": {
            "name": "",
            "g_key": "shell:simple_bash",
            "type": "file",
            "dirname": "shell/",
            "filename": ["simple-bash.sh"]
        }
    },
    "python": {
        "simple_python": {
            "name": "",
            "g_key": "python:simple_python",
            "type": "file",
            "dirname": "python/",
            "filename": ["simple.py"]
        }
    },
    "django": {
        "1.8.4": {
            "name": "",
            "g_key": "django:1.8.4",
            "type": "dir",
            "dirname": "django/1.8.4/myproject/",
            "run_command": "python manage.py runserver 0.0.0.0:8000",
            "filename": [
                "db.sqlite3",
                "manage.py",
                "myapp/__init__.py",
                "myapp/admin.py",
                "myapp/migrations/__init__.py",
                "myapp/models.py",
                "myapp/tests.py",
                "myapp/views.py",
                "myapp/templates/index.html",
                "myproject/__init__.py",
                "myproject/settings.py",
                "myproject/urls.py",
                "myproject/wsgi.py"
            ]
        }
    }
}

Template_TYPES = {
}

TOPIC_INCLUDES = {
    # <Topic Name>: [<Template Type>, ]
    "web": ["web"],
    "django": ["django"],
    "coding": ["shell", "python"]
}
