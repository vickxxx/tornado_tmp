#!/usr/bin/env python3
# coding:utf-8
"""
    handler示例
"""

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        welcome_word = "welcome you. this is rendered by jinja2"
        self.render('index.html', sth=welcome_word)
