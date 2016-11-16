#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
应用描述
"""
import os
import tornado.web
from url import url
import jinja2
from tornado_jinja2 import Jinja2Loader

jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template/'), autoescape=False)
jinja2_loader = Jinja2Loader(jinja2_env)

setting = {
    "login_url": "/login",
    # "cookie_secret": "vickwww",
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    'xsrf_cookies': False,
    'template_loader': jinja2_loader
    # 'task_config_path': 'task/'
    }

application = tornado.web.Application(
    handlers=url,
    debug=True,
    **setting
    )
