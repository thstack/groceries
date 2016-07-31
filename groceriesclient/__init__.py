#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: SimonLuo <simonluo@thstack.com>
from groceries import config as g_config


def get_topic_templates(topic):
    """Get topic templates

    {
        <TYPE> : {
            'g_key': '',
            'type': '',
            'dirname': '',
            'filename': []}
    }
    """
    if topic not in g_config.TOPIC_INCLUDES.keys():
        return (-1, 'Topic does not have templates!', None)

    res = {}
    for tname in g_config.TOPIC_INCLUDES[topic]:
        res[tname] = g_config.TEMPLATES[tname]
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
