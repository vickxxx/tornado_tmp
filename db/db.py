#!/usr/bin/env python3
# -*-coding:utf-8-*-
import sqlite3
import sys

sys.setdefaultencoding("utf-8")

DB_PATH = 'sdp.db'
db_init_flag = 0

CRT_USER = '''CREATE TABLE user ( "id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    "name"  TEXT NOT NULL,
                                    "pwd"  TEXT NOT NULL,
                                    "nick"  TEXT,
                                    "roleid"  INTEGER,
                                    "premission_code"  INTEGER,
                                    "phone"  TEXT,
                                    "ctime"  TEXT,
                                    "mtime"  TEXT,
                                    "lasttime"  TEXT,
                                    "invalid" INTEGER ,
                                    "ext"  TEXT
                                    );'''

CRT_ROLE = '''CREATE TABLE role ( "id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    "dscpt"  TEXT NOT NULL,
                                    "premission_code"  INTEGER,
                                    "ctime"  TEXT,
                                    "mtime"  TEXT,
                                    "invalid" INTEGER,
                                    "ext"  TEXT
                                    );'''
CRT_DEVICE = '''CREATE TABLE device ( "id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    "mac"  TEXT NOT NULL,
                                    "brand"  TEXT,
                                    "model"  TEXT,
                                    "os_ver"  TEXT,
                                    "andriod_ver"  TEXT,
                                    "phone"  TEXT,
                                    "color"  TEXT,
                                    "owner"  TEXT,
                                    "access_flag"  INTEGER,
                                    "test_times"  TEXT,
                                    "fail_times"  TEXT,
                                    "ctime"  TEXT,
                                    "mtime"  TEXT,
                                    "invalid" INTEGER DEFAULT 0,
                                    "ext"  TEXT
                                    );'''

CRT_PORTAL = '''CREATE TABLE portal ( "id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    "brand"  TEXT NOT NULL,
                                    "shop"  TEXT,
                                    "path"  TEXT,
                                    "url"  TEXT,
                                    "direct_flag" INTEGER,
                                    "onekey_flag" INTEGER,
                                    "test_times"  TEXT,
                                    "fail_times"  TEXT,
                                    "ctime"  TEXT,
                                    "mtime"  TEXT,
                                    "invalid" INTEGER,
                                    "ext"  TEXT
                                    );'''
CRT_NODE = '''CREATE TABLE node ( "id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    "node_id",
                                    "brand"  TEXT NOT NULL,
                                    "mem"  TEXT,
                                    "cpu"  TEXT,
                                    "portal_id" INTEGER,
                                    "wifidog"  TEXT,
                                    "premission_code" INTEGER,
                                    "ctime"  TEXT,
                                    "mtime"  TEXT,
                                    "invalid" INTEGER,
                                    "ext"  TEXT
                                    );'''
CRT_TASK = '''CREATE TABLE task ( "id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    "taskname" TEXT,
                                    "dscpt" TEXT,
                                    "portal_id" TEXT,
                                    "file" TEXT,
                                    "creater" TEXT,
                                    "times" TEXT,
                                    "fail_times" TEXT,
                                    "premission_code" INTEGER,
                                    "ctime"  TEXT,
                                    "mtime"  TEXT,
                                    "invalid" INTEGER,
                                    "ext"  TEXT
                                    );'''


########################################################################
class mb_db:
    """数据库操作接口"""
    db_path = 'db/sdp.db'
    cur = None
    conn = None
    db_user_col = ["id", "name", "pwd", "nick", "roleid", "premission_code", "phone", "ctime", "mtime", "lasttime",
                   "invalid", "ext"]
    db_role_col = ["id", "dscpt", "premission_code", "ctime", "mtime", "invalid", "ext"]
    db_device_col = ["id", "mac", "brand", "model", "os_ver", "andriod_ver", "phone", "color", "owner", "access_flag",
                     "test_times", "fail_times", "ctime", "mtime", "invalid", "ext"]
    db_portal_col = ["id", "brand", "shop", "path", "url", "direct_flag", "onekey_flag", "test_times", "fail_times",
                     "ctime", "mtime", 'invalid', "ext"]
    db_node_col = ["id", "node_id", "brand", "mem", "cpu", "portal_id", "wifidog", "premission_code", "ctime", "mtime",
                   "invalid", "ext"]
    db_task_col = ["id", "taskname", "dscpt", "portal_id", "file", "creater", "times", "fail_times", "premission_code",
                   "ctime", "mtime", "invalid", "ext"]
    tables = {'user': db_user_col, 'role': db_role_col, 'device': db_device_col, 'portal': db_portal_col,
              'node': db_node_col, 'task': db_task_col}

    # ----------------------------------------------------------------------
    def create_tbl(self):
        self.cur.execute(CRT_USER)
        self.cur.execute(CRT_ROLE)
        self.cur.execute(CRT_DEVICE)
        self.cur.execute(CRT_NODE)
        self.cur.execute(CRT_PORTAL)
        self.cur.execute(CRT_TASK)

    def __init__(self):
        """初始化数据库，建立连接"""
        isempty = False
        if not os.path.exists(self.db_path):
            # self.create_tbl()
            isempty = True
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        self.conn.text_factory = str
        # self.cur.execute(CRT_USER)
        # self.cur.execute(CRT_TASK)
        if isempty:
            self.create_tbl()
            print
            'create tables'
            isempty = False

    def get_names(self):
        res = self.cur.execute('SELECT id,name FROM user;')
        r = dict(list(self.cur.fetchall()))
        return r

    def get_row(self, table, pair):

        if pair[0] == 'id':
            res = self.cur.execute(
                'select * from {table} where {key} = {value} and not invalid; '.format(table=table, key=pair[0],
                                                                                       value=pair[1]))

        else:
            res = self.cur.execute(
                'select * from {table} where {key} = "{value}" and not invalid; '.format(table=table, key=pair[0],
                                                                                         value=pair[1]))
        r = list(self.cur.fetchall())
        if len(r) < 1:
            return None
        res = list()
        for row in r:
            res.append(list(row))
        if res:
            res.append(self.tables[table])
            # print res,'\nssssssssss',r
            return res

    def get_rows(self, table):
        # print 'get_rows',table
        res = self.cur.execute('select * from {table} where not invalid ;'.format(table=table))  # where invalid
        r = list(self.cur.fetchall())
        res = list()
        for row in r:
            res.append(list(row))
        if res:
            res.append(self.tables[table])
            # print res,'\nssssssssss',r
            return res

    def add_row(self, table, vals):
        var_count = len(self.tables[table]) - 1
        # print '?,'*count
        placeholder = ('?,' * var_count)[0:-1]
        # print placeholder
        sql_str = 'INSERT INTO {table} ({cols}) VALUES ({placeholder});'.format(table=table,
                                                                                cols=','.join(self.tables[table][1:]),
                                                                                placeholder=placeholder)
        # print sql_str
        try:
            r = self.cur.execute(sql_str, vals)
            self.conn.commit()
            # print r
        except Exception as e:
            # print ','.join(self.db_user_col[1:])
            print
            'insert error：', e
            # print len(vals)

    def del_row(self, table, row_id):
        print
        str(row_id)
        try:
            act_dict = {'id': row_id, 'invalid': '1'}
            self.alt_row(table, act_dict)
            # r = self.cur.execute('DELETE FROM {table} WHERE id = {row_id} ;'.format(table=table,row_id=row_id))
            self.conn.commit()
        except Exception as e:
            # print ','.join(self.db_user_col[1:])
            print
            'delete error：', e

    def alt_row(self, table, info_dict):
        '''修改更新数据库信息，info_dict参数为字段为键的字典。{'id':2,name:'新用户'},id为必须'''

        if 'id' not in info_dict:
            print
            'must include id...'

        sql_str = 'UPDATE {table} SET '.format(table=table)
        for k, v in info_dict.items():
            print
            k, v
            # print sql_str.join(str(k))
            if k in (
            'roleid', 'premission_code', 'invalid', 'id', 'direct_flag', 'onekey_flag', 'access_flag', 'portal_id'):
                sql_str += (k + ' = ' + v + ',')
            else:
                sql_str += (k + ' = "' + v + '",')
                # print sql_str
        row_id = info_dict.pop('id')
        sql_str = sql_str[0:-1] + ' WHERE id = {row_id}'.format(row_id=row_id)  # +row_id
        # print sql_str

        self.cur.execute(sql_str);
        self.conn.commit()


if __name__ == '__main__':

    sys.path.append(os.path.abspath('../'))
    d = mb_db()
    role_test = ('猛男3', 123, 'ddd', None, 'NULL', 'ttt')
    user_test = ('345', 'ddd', 'None', 1, 'ttt', '猛男2', '123', 'ddd', 2, 'NULL')
    d.add_row('user', user_test)
    d.add_row('role', role_test)
    d.del_row('role', '14')
    role_info_dict = {'id': '6', 'dscpt': '谁吃了我的蛋糕', 'premission_code': '112', 'ctime': '2015-8-2'}
    user_info_dict = {'id': '7', 'name': '谁吃了我的蛋糕', 'premission_code': '112', 'ctime': '2015-8-2'}
    d.alt_row('user', user_info_dict)
    str(d.get_rows('user'))
