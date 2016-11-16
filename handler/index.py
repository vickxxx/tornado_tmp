#!/usr/bin/env python3
# coding:utf-8
"""
    handler示例
"""

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        welcome_word = "welcome you. this is randered by jinja2"
        self.render('index.html', sth=welcome_word)

