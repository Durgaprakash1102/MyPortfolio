from .models import VisitorLog
from django.utils.timezone import now

MY_IPS = ['your.pythonanywhere.ip.address']  # Add your PythonAnywhere IP here

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # Sometimes X-Forwarded-For can have multiple IPs: client, proxy1, proxy2...
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class VisitorLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        ip = get_client_ip(request)

        # Skip logging if IP is in MY_IPS or path starts with admin or if it's AJAX request
        if not request.path.startswith('/admin') \
           and request.headers.get('x-requested-with') != 'XMLHttpRequest' \
           and ip not in MY_IPS:

            ua = request.META.get('HTTP_USER_AGENT', '')
            ref = request.META.get('HTTP_REFERER', '')
            path = request.path

            VisitorLog.objects.create(
                ip_address=ip,
                user_agent=ua,
                referrer=ref,
                path=path,
                timestamp=now()
            )
        return response
