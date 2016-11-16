#!/usr/bin/env python3
# coding:utf-8
"""
    handler示例
"""

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        lst = "welcome you."
        self.render('index.html')

