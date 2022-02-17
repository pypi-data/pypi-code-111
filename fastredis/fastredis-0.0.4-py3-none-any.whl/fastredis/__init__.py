#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import showlog
import redis
import envx
default_env = envx.read(file_name='redis.env')
redis_host_default = default_env.get('host', 'localhost')
redis_port_default = int(default_env.get('port', '6379'))
redis_pwd_default = default_env.get('password')


class Basics:
    def __init__(
            self,
            con_db=None,  # 需要连接的数据库
            host=redis_host_default,  # 连接的域名
            port=redis_port_default,  # 连接的端口
            password=redis_pwd_default  # 连接的密码
    ):
        # 初始化所有参数
        if con_db is None:
            self.con_db = 0
        else:
            self.con_db = con_db

        self.host = host
        self.port = port
        self.pwd = password
        self.connection = self.connect()  # 执行连接

    def connect(
            self
    ):
        # 执行连接
        pool = redis.ConnectionPool(
            host=self.host,
            port=self.port,
            password=self.pwd,
            db=self.con_db,
            max_connections=10
        )
        connection = redis.Redis(connection_pool=pool)
        return connection

    def get_db_key_list(
            self,
            connection=None
    ):
        """
        读取指定数据库的键列表
        """
        if connection is None:
            conn = self.connection
        else:
            conn = connection

        while True:
            try:
                keys = conn.keys()
                break
            except:
                showlog.error('获取失败，准备重连')
                self.connection = self.connect()

        key_list = list()
        for key in keys:
            key_list.append(key.decode())
        return key_list

    def read_list_key_values(
            self,
            key,
            connection=None
    ):
        """
        读取指定库的指定键的所有值列表
        """
        if connection is None:
            conn = self.connection
        else:
            conn = connection

        while True:
            try:
                values_count = conn.llen(key)  # 获取列表元素个数
                break
            except:
                showlog.error('获取失败，准备重连')
                self.connection = self.connect()

        values = list()
        for i in range(values_count):
            while True:
                try:
                    each_value = conn.lindex(key, i)
                    break
                except:
                    showlog.error('获取失败，准备重连')
                    self.connection = self.connect()
            if each_value is not None:
                values.append(each_value.decode())
        return values

    def list_add_l(
            self,
            key,
            value,
            connection=None
    ):
        # 在list左侧添加值
        if connection is None:
            conn = self.connection
        else:
            conn = connection

        while True:
            try:
                return conn.lpush(key, value)
            except:
                showlog.error('获取失败，准备重连')
                self.connection = self.connect()

    def list_add_r(
            self,
            key,
            value,
            connection=None
    ):
        # 在list右侧添加值
        if connection is None:
            conn = self.connection
        else:
            conn = connection

        while True:
            try:
                return conn.rpush(key, value)
            except:
                showlog.error('获取失败，准备重连')
                self.connection = self.connect()

    def list_pop_l(
            self,
            key,
            connection=None
    ):
        # 从左侧出队列
        if connection is None:
            conn = self.connection
        else:
            conn = connection

        while True:
            try:
                return conn.lpop(key)
            except:
                showlog.error('获取失败，准备重连')
                self.connection = self.connect()

    def list_pop_r(
            self,
            key,
            connection=None
    ):
        # 从右侧侧出队列
        if connection is None:
            conn = self.connection
        else:
            conn = connection

        while True:
            try:
                return conn.rpop(key)
            except:
                showlog.error('获取失败，准备重连')
                self.connection = self.connect()

    def set_string(
            self,
            name,
            value,
            connection=None,
            ex=None,
            px=None
    ):
        # 设置键值，ex过期时间（秒），px过期时间（毫秒）
        if connection is None:
            conn = self.connection
        else:
            conn = connection
        while True:
            try:
                return conn.set(
                    name,
                    value,
                    ex=ex,
                    px=px,
                    nx=False,
                    xx=False
                )
            except:
                showlog.error('获取失败，准备重连')
                self.connection = self.connect()

    def get_string(
            self,
            name,
            connection=None
    ):
        # 获取键值
        if connection is None:
            conn = self.connection
        else:
            conn = connection
        while True:
            try:
                return conn.get(name)
            except:
                showlog.error('获取失败，准备重连')
                self.connection = self.connect()

    def delete_string(
            self,
            name,
            connection=None
    ):
        # 删除键值
        if connection is None:
            conn = self.connection
        else:
            conn = connection
        while True:
            try:
                return conn.delete(name)
            except:
                showlog.error('获取失败，准备重连')
                self.connection = self.connect()


def list_add_r(
        key,
        value,
        env_file_name='redis.env'
):
    inner_env = envx.read(file_name=env_file_name)
    basics = Basics(
        host=inner_env['host'],
        port=int(inner_env.get('port', '27017')),
        password=inner_env['password']
    )
    basics.list_add_r(
        key=key,
        value=value
    )


def list_pop_l(
        key,
        env_file_name='redis.env'
):
    inner_env = envx.read(file_name=env_file_name)
    basics = Basics(
        host=inner_env['host'],
        port=int(inner_env.get('port', '27017')),
        password=inner_env['password']
    )
    basics.list_pop_l(
        key=key
    )

