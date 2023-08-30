# -*- coding:utf-8 -*-　　


from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class ApiResponseMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        return response
