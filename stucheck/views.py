# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserList
import urllib
import urllib2
import json
import hashlib

@csrf_exempt
def loginCheck(request):
    if request.method == 'POST':
        post_username = request.POST.get('username')
        post_password = request.POST.get('password')
        post_key = request.POST.get('key')
        if post_key == 'aEQNVqQv2ixRJYKB0LmmlMsE9e83PMRN':
            # email login
            code = loginEmail(post_username, post_password)
            # code -  0, 1, 3, 5
            if code == 0:
                # valid user
                writeToDatabase(post_username, post_password)
            # json code   
            jsonData = {
                'code': code,
            }
            # ensure_ascii=False Chinese
            return HttpResponse(json.dumps(jsonData, ensure_ascii=False), content_type='application/json')
        else:
            return None
    else:
        return None

# email login
def loginEmail(username, password):
    parameters = {
        'LoginName': username,
        'Password': password,
        'local1': 'zh_CN',
        'domain': 'stu.edu.cn',
    }
    data = urllib.urlencode(parameters)
    url = 'http://webmail.stu.edu.cn/cgi-bin/user_login'
    request = urllib2.Request(url, data)
    try:
        response = urllib2.urlopen(request)
        response_code = int(response.read())
        print response_code
        if response_code == 0:
            # succeed
            return 0
        elif response_code == 5:
            # incorrect password
            return 5
        elif response_code == 2:
            # incorrect username
            return 2
        else:
            # unknown error
            print 'Unknown Error'
            return 3
    except:
        print 'LoginEmail Error'
        return 1

# database - md5
def writeToDatabase(p_username, p_password):
    # generate md5
    md = hashlib.md5()
    key = p_username + p_password
    md.update(key)
    u_set = UserList.objects.filter(username=p_username)
    if u_set.count() > 0:
        # exist - update
        u = u_set[0]
        u.auth_key = md.hexdigest()
        u.save()
        print u'认证用户: ' + p_username + '  ' + md.hexdigest()
    else:
        # not exist - new
        u = UserList(username=p_username, auth_key=md.hexdigest())
        u.save()
        print u'新增用户: ' + p_username + '  ' + md.hexdigest()








