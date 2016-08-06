#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: SimonLuo <simonluo@thstack.com>
from groceries import settings


def get_topic_templates(topic=None):
    """Get topic templates

    {
        <TYPE> : {
            'g_key': '',
            'type': '',
            'dirname': '',
            'filename': {}}
    }
    """
    if topic and topic not in settings.TOPIC_INCLUDES.keys():
        return (-1, 'Topic does not have templates!', None)

    res = {}
    if topic:
        for tname in settings.TOPIC_INCLUDES[topic]:
            res[tname] = settings.TEMPLATES[tname]
    else:
        res = settings.TEMPLATES
    return (0, 'Success!', res)


def get_configs_by_gkey():
    res = {}
    for key, values in settings.TEMPLATES.items():
        for v_k, v_v in values.items():
            res[v_v['g_key']] = v_v
    return (0, 'Success!', res)


def is_valid(g_key):
    k = g_key.split(':')
    if len(k) != 2:
        return (1, 'g_key must include one ":"!', None)

    if k[0] not in settings.TEMPLATES:
        return (1, 'g_key not exist!', None)
    elif k[1] not in settings.TEMPLATES[k[0]]:
        return (1, 'g_key not exist!', None)
    return (0, 'Success', None)


def get_template_config(g_key):
    """Get template config for one g_key"""
    s, m, r = is_valid(g_key)
    if s != 0:
        return (s, m, r)

    key1, key2 = g_key.split(':')
    return (0, 'Success!', settings.TEMPLATES[key1][key2])


def get_files(keys, without_keys=[]):
    res = {}
    for g_key in keys:
        if g_key in without_keys:
            continue

        s, m, r = get_template_config(g_key)
        if s != 0:
            return (s, m, r)
        g_type, g_dirname, g_files = r['g_type'], r['g_dirname'], r['files'] 

        if g_type == 'file':
            res[g_files['filename']] =  {'is_text': c['is_text']}
        elif g_type == 'dir':
            for filename, c in g_files.items():
                res[filename] = c
    return (0, 'Success!', res)


def get_file(g_key, filename=None):
    """目录模版需要指定文件名"""
    s, m, r = get_template_config(g_key)
    if s != 0:
        return (s, m, r)
    g_type, g_dirname, g_files = r['g_type'], r['g_dirname'], r['files'] 

    if g_type == 'dir':
        if not filename:
            return (1, 'Need filename!', None)

        if filename not in g_files:
            return (1, 'filename does not exist!', None)
    else:
        filename = g_files['filename']

    try:
        content = open(settings.PATH + '/groceries/templates/' + g_dirname + filename).read()
        if '\0' in content:
            content = 'Not text file'
        content = content[0:-1] if content and content[-1] == '\n' else content
    except Exception as e:
        return (-1, str(e), None)
    return (0, 'Success!', content)


def is_text(content):
    if '\0' in content:
        return (1, 'Not text file!', None)
    return (0, 'Success!', None)


def get_template_file(filename):
    g_key = filename
    filename = g_key.replace('program:', '').replace(':', '/')

    try:
        content = open('/opt/git/groceries/' + filename).read()
        content = content[0:-1] if content and content[-1] == '\n' else content
    except Exception as e:
        return (-1, str(e), None)
    return (0, 'Success!', content)


# def get_settings(g_key, filename=None):
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
#         return (-1, 'Can not get a valid settings data!', None)
#
#     g_type = g_data['type']
#     g_dirname = g_data['dirname']
#     g_filenames = g_data['filename']
#
#     return (0, 'Success', (g_type, g_dirname, g_filenames))
