#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
  一个简单的MVC，用来启动Web框架 ORM框架和配置
'''

import os,re,time,base64,hashlib,logging

from transwarp.web import get, post, ctx ,view ,interceptor,seeother,notfound

from models import User, Blog, Comment

#@view指定模板文件：blogs.html
@view('blogs.html')
@get('/')
def index():
    blogs =Blog.find_all()
    user = User.find_first('where email=?','admin@example.com')
    return dict(blogs=blogs,user=user)
