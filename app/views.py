from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    tn=input('enter a value: ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic has created successfully')

def insert_webpages(request):
    tn=input('enter a value:')
    n=input('enter a value:')
    u=input('enter a value:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpages.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    return HttpResponse('webpage created successfully')

def insert_access(request):
    tn=input('enter topic:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name:')
    u=input('enter a url:')
    WO=Webpages.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    
    d=input('enter date:')
    a=input('enter author:')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()

    return HttpResponse('access created successfully')





    


