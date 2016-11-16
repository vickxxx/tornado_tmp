#!/usr/bin/env python3
#coding:utf-8
"""
url路由管理
"""

from handler.index import IndexHandler


url = [
    (r'/', IndexHandler)
    ]

print("ok")