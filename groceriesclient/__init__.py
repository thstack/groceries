#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: SimonLuo <simonluo@thstack.com>
from groceries import config as g_config


def get_topic_templates(topic=None):
    """Get topic templates

    {
        <TYPE> : {
            'g_key': '',
            'type': '',
            'dirname': '',
            'filename': []}
    }
    """
    if topic and topic not in g_config.TOPIC_INCLUDES.keys():
        return (-1, 'Topic does not have templates!', None)

    res = {}
    if topic:
        for tname in g_config.TOPIC_INCLUDES[topic]:
            res[tname] = g_config.TEMPLATES[tname]
    else:
        res = g_config.TOPIC_INCLUDES
    return (0, 'Success!', res)


def get_template_file(filename):
    g_key = filename
    filename = g_key.replace('program:', '').replace(':', '/')

    try:
        content = open('/opt/git/groceries/' + filename).read()
        content = content[0:-1] if content and content[-1] == '\n' else content
    except Exception as e:
        return (-1, str(e), None)
    return (0, 'Success!', content)


# def get_g_config(g_key, filename=None):
#     """Get groceries's config, incloud:
#
#         type, dirname, filenames
#     """
#     # import ipdb; ipdb.set_trace()
#     if filename:
#         g_key = g_key.replace(':' + filename.replace('/', ':'), '')
#
#     keys = [k for k in g_key.split(':') if k]
#
#     g_data = settings.GroceriesConfig.GROCERIES_JSON
#     for k in keys:
#         if 'type' in g_data and 'dirname' in g_data and 'filename' in g_data:
#             break
#         g_data = g_data[k]
#
#     if 'type' not in g_data or 'dirname' not in g_data or 'filename' not in g_data:
#         return (-1, 'Can not get a valid g_config data!', None)
#
#     g_type = g_data['type']
#     g_dirname = g_data['dirname']
#     g_filenames = g_data['filename']
#
#     return (0, 'Success', (g_type, g_dirname, g_filenames))
