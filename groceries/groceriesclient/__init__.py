#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: SimonLuo <simonluo@thstack.com>
from groceries import settings


TEMPLATE_PATH = settings.PATH + '/' + 'groceries/templates/'


def get_templates(topic=None, g_key=None):
    """Get topic templates"""
    if topic and topic not in settings.TOPIC_INCLUDES.keys():
        return (1, 'Topic does not have templates!', None)

    res = {}
    if topic:
        for tname in settings.TOPIC_INCLUDES[topic]:
            res[tname] = settings.TEMPLATES[tname]
    else:
        res = settings.TEMPLATES

    if g_key:
        s, m, r = is_valid(g_key)
        if s != 0:
            return (s, m, r)
        k1, k2 = r
        if k1 not in res or k2 not in res[k1]:
            return (1, '[GS] g_key not exist!', None)
        res = res[k1][k2]

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
    return (0, 'Success', k)


def get_templatefiles(keys, without_keys=[]):
    res = {}
    for g_key in keys:
        if g_key in without_keys:
            continue

        s, m, r = get_templates(g_key=g_key)
        if s != 0:
            return (s, m, r)
        g_type, g_dirname, g_files = r['g_type'], r['g_dirname'], r['files'] 

        if g_type == 'file':
            res[g_files['filename']] =  {'is_text': c['is_text']}
        elif g_type == 'dir':
            for filename, c in g_files.items():
                res[filename] = c
    return (0, 'Success!', res)


def get_templatefile_content(g_key, filename=None):
    """获取模版内容"""
    s, m, r = get_templates(g_key=g_key)
    if s != 0:
        return (s, m, r)
    g_type, g_dirname, g_files = r['g_type'], r['g_dirname'], r['files'] 

    res = {}
    filenames = []
    if g_type == 'dir':
        if not filename:
            for f, v in g_files.items():
                if v['is_text'] is False:
                    res[f] = 'Not text file'
                else:
                    filenames.append(f)
        elif filename not in g_files:
            return (1, '[GS] filename does not exist!', None)
        else:
            filenames = [filename]
    elif g_type == 'file':
        if g_files['is_text'] is False:
            res[g_files['filename']] = 'Not text file'
        filenames = [g_files['filename']]
    else:
        raise Exception()

    try:
        for filename in filenames:
            content = open(settings.PATH + '/groceries/templates/' + g_dirname + filename).read()
            if '\0' in content:
                content = 'Not text file'
            content = content[0:-1] if content and content[-1] == '\n' else content
            res[filename] = content
    except Exception as e:
        return (-1, str(e), None)
    return (0, 'Success!', res)
