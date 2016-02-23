from django.core.exceptions import PermissionDenied


class Ratelimited():
    def __init__(self):
        print 'DEBUG - Ratelimited'

        PermissionDenied()
