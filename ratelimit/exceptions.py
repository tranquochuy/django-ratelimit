import json

from tastypie.http import HttpBadRequest


class Ratelimited():
    """
    Override
    """

    def __init__(self):
        return HttpBadRequest(
            json.dumps(None),
            content_type='application/json',
            status=403)
