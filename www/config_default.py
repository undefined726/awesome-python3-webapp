#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

# 数据库配置文件，注意配置信息可能被config_override.py中的定义覆盖
configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
