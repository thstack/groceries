#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: SimonLuo <simonluo@thstack.com>


"""
Note:
    g_type: include 'file'/'dir'
    g_key: format is "<Type>:<Name>"
"""
# from groceries.profiles import python as profile_python
# from groceries.profiles import linuxbash as profile_linuxbash
# from groceries.profiles import webfront as profile_webfront
# from groceries.profiles import webserver as profile_webserver


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
    "linuxbash": {
        "simple_bash": {
            "g_key": "linuxbash:simple_bash",
            "alias": "Simple Bash Template",
            "g_type": "file",
            "g_dirname": "linuxbash/",
            "files": {
                "filename": "simple-bash.sh",
                "is_text": True
            }
        }
    },
    "python": {
        "simple_python": {
            "alias": "Simple Python Temlate(Python 2.7)",
            "g_key": "python:simple_python",
            "g_type": "file",
            "g_dirname": "python/",
            "files": {
                "filename": "simple.py",
                "is_text": True
            }
        }
    },
    "django": {
        "1.8.4": {
            "alias": "Django Template(1.8.4)",
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

# def get_template_init_cmds(pm_root, pm_me, vm_root, vm_me, learn_root, **kwargs): 
#     """
#     Worflow:
#         1. Move db.sqlite3 to user data directory;
#         2. Rewrite django setttings with new database config
#     """
#     target_dir = pm_root + learn_root
#     data_dir = pm_me + '.data/learn/' + learn_root
#     db_dir = mv_me + '.data/learn/' + learn_root
# 
#     res = [
#         'mv -f %smyproject/db.sqlite3 %s' % (target_dir, data_dir),
#         'sed -i "81 s/BASE_DIR/\'%s\'/g" %smyproject/myproject/settings.py' % (data_dir_vm.replace('/', '\/'), target_dir)]
#     return (0, 'Success!', res)
# 
# INIT_CMDS = {
#     # <g_key>: []
#     'django:1.8.4': {
#         'params': {},
#         'func': init_django,
#     }
# }

TOPIC_INCLUDES = {
    # <Topic Name>: [<Template Type>, ]
    "webfront": ["web"],
    "webserver": ["django"],
    "coding": ["linuxbash", "python"]
}
