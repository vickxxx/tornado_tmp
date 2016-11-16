#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
服务主程序
"""
import os
import sys

sys.path.append(os.path.abspath('.'))

import tornado.ioloop
import tornado.options
import tornado.httpserver
# from db.db import *
from application import application
from tornado.options import define, options

define("port", default=80, help="run on th given port", type=int)
define('debug', default=True, help='enable debug mode')

def main():
    """
        呵呵哒
    """
    # 启用文件记录日志
    # tornado.options.define("log_file_prefix", "logs/my_app.log")  
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:%s/' % options.port)
    print('Quit the server with Control-C')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
