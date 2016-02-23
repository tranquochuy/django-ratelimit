from django.http import HttpResponse


class Ratelimited():
    def __init__(self):
        HttpResponse(code=403)
