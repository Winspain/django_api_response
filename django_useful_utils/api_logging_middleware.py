# -*- coding:utf-8 -*-　　
import json
import logging
import time

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class ApiLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.start_time = time.time()
        try:
            body = json.loads(request.body)
        except Exception:
            body = str(request.body)
        if request.FILES:
            body = 'file contents'
        post = str(request.POST)
        response = self.get_response(request)
        execute_time = round((time.time() - request.start_time) * 1000)
        try:
            response_data = str(response.content, encoding='utf-8') if response.status_code != 500 else 'Please check error log'
        except Exception as e:
            response_data = e
        logging.info(f'{execute_time}{response_data}')
