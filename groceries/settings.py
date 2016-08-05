#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: SimonLuo <simonluo@thstack.com>


"""
Note:
    g_type: include 'file'/'dir'
    g_key: format is "<Type>:<Name>"
"""


try:
    from groceries.local.local_settings import *
except ImportError:
    raise Exception("No local_settings file found in groceries/local/local_settings.py")
    exit()


TEMPLATES = {
    "web": {                # Type
        "simple_html": {    # Name
            "g_key": "web:simple_html",
            "alias": "Simple HTML Temlate",
            "g_type": "file",
            "g_dirname": "web/",
            "files": {
                "filename": "simple.html",
                "is_text": True
            }
        },
        "simple_css": {
            "g_key": "web:simple_css",
            "alias": "Simple CSS Template",
            "g_type": "file",
            "g_dirname": "web/",
            "files": {
                "filename": "simple.css",
                "is_text": True
            }
        },
        "simple_js": {
            "g_key": "web:simple_js",
            "alias": "Simple JS Template",
            "g_type": "file",
            "is_text": True,
            "g_dirname": "web/",
            "files": {
                "filename": "simple.js",
                "is_text": True
            }
        },
        "simple_web": {
            "g_key": "web:simple_web",
            "alias": "Simple Web Template",
            "g_type": "dir",
            "g_dirname": "web/",
            "files": {
                "simple-web/index.html": {"is_text": True},
                "simple-web/main.js": {"is_text": True},
                "simple-web/style.css": {"is_text": True}
            }
        }
    },
    "shell": {
        "simple_bash": {
            "g_key": "shell:simple_bash",
            "alias": "Simple Bash Template",
            "g_type": "file",
            "g_dirname": "shell/",
            "files": {
                "simple-bash.sh": {"is_text": True},
                "is_text": True
            }
        }
    },
    "python": {
        "simple_python": {
            "name": "",
            "g_key": "python:simple_python",
            "g_type": "file",
            "g_dirname": "python/",
            "files": {
                "simple.py": {"is_text": True},
                "is_text": True
            }
        }
    },
    "django": {
        "1.8.4": {
            "name": "Django Template(1.8.4)",
            "g_key": "django:1.8.4",
            "g_type": "dir",
            "g_dirname": "django/1.8.4/",
            "run_command": "python manage.py runserver 0.0.0.0:8000",
            "files": {
                "myproject/db.sqlite3": {"is_text": False},
                "myproject/manage.py": {"is_text": True},
                "myproject/myapp/__init__.py": {"is_text": True},
                "myproject/myapp/admin.py": {"is_text": True},
                "myproject/myapp/migrations/__init__.py": {"is_text": True},
                "myproject/myapp/models.py": {"is_text": True},
                "myproject/myapp/tests.py": {"is_text": True},
                "myproject/myapp/views.py": {"is_text": True},
                "myproject/myapp/templates/index.html": {"is_text": True},
                "myproject/myproject/__init__.py": {"is_text": True},
                "myproject/myproject/settings.py": {"is_text": True},
                "myproject/myproject/urls.py": {"is_text": True},
                "myproject/myproject/wsgi.py": {"is_text": True}
            }
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
