# -*- coding: utf-8 -*- 
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from statistic.models import Phone
from .models import Category, PhoneList, Version
import json
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf

@csrf_exempt
def phoneData(request):
    if request.method == 'POST':
        device_post = request.POST.get('device')
        key_post = request.POST.get('key')
        if key_post == 'KqePnWoGfHhbLCU4yoPEXi5qXWQk69IE':
            # sync++
            p = Phone.objects.get()
            p.sync_amount += 1
            if device_post == 'iOS':
                # iOS
                p.ios_sync_amount += 1
            elif device_post == 'Android':
                # Android
                p.android_sync_amount += 1
            else:
                # unrecognized device
                return None
            p.save()
            # prepare data
            phoneData = []
            for categoryData in Category.objects.all():
                categoryDict = {}
                categoryDict['name'] = categoryData.category_name
                listArray = []
                for listData in PhoneList.objects.filter(phone_category=categoryData):
                    listArray.append({
                        'name': listData.phone_name,
                        'num1': listData.phone_num1,
                        'num2': listData.phone_num2,
                    })
                categoryDict['list'] = listArray
                phoneData.append(categoryDict)
            # add Version
            v = Version.objects.get()
            jsonData = {
                'version': v.version_num,
                'data': phoneData,
            }
            # ensure_ascii=False Chinese
            return HttpResponse(json.dumps(jsonData, ensure_ascii=False), content_type='application/json')
        else:
            return None
    else:
        return None