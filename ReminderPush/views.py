from django.shortcuts import render

# 測試 urls 連接
from django.http import HttpResponse
def index(request):
    return HttpResponse("ReminderPush")