from django.http import HttpResponse
from django.shortcuts import redirect

from .models import IpStorage



def get_header(header):
    def requester(request):
        data = request.META.get(header)
        return data
    return requester

get_IP = get_header('HTTP_X_FORWARDED_FOR')
get_browser = get_header('HTTP_USER_AGENT')

def save_ip(request):
    ip = get_IP(request)
    user_agent = get_browser(request)
    try:
        IpStorage.objects.create(ip = ip, user_agent = user_agent)
    except:
        return HttpResponse('An error ocurred')

    return redirect('https://youtu.be/dQw4w9WgXcQ')










