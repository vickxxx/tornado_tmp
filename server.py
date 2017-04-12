#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
服务主程序
"""
import os
import sys
import yaml
import time
import logging
import logging.config

import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options

from application import application

sys.path.append(os.path.abspath('.'))

define("port", default=80, help="run on th given port", type=int)
define('debug', default=True, help='enable debug mode')


def main():
    """
        呵呵哒
    """
    # 启用文件记录日志
    #tornado.options.define("log_file_prefix", "logs/my_app.log")
    
    logging.config.dictConfig(yaml.load(open('logging.yaml', 'r')))
    
    tornado.options.parse_command_line()
    if not sys.platform.startswith('win'):
        import coloredlogs
        coloredlogs.install(level='DEBUG', logging.getLogger("tornado"))    
    
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:%s/' % options.port)
    print('Quit the server with Control-C')
    ll = logging.getLogger("tornado.application")
    for i in range(120):
        ll.info(str(i))
        try:
            4/0
        except Exception as e:
            ll.exception("lelel")
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
