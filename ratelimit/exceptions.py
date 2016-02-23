from tastypie.http import HttpResponse


class Ratelimited(HttpResponse):
    status_code = 403
