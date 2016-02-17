import json
from datetime import datetime

def serializer(obj):
    """Serializer for objects not serializable by default in JSON"""

    if isinstance(obj, datetime):
        str_datetime = obj.isoformat()
        return str_datetime

    return obj.__dict__

class HAR:
    """Represents an HTTP Archive file"""
    def __init__(self):
        self.log = {}
        self.log['version'] = "1.2"
        self.log['creator'] = {}
        self.log['creator']['name'] = "dumbhar"
        self.log['creator']['version'] = "0.1"
        self.log['creator']['comment'] = ""
        self.log['browser'] = {}
        self.log['browser']['name'] = "dumbhar"
        self.log['browser']['version'] = "0.1"
        self.log['browser']['comment'] = ""
        self.log['pages'] = []
        self.log['entries'] = []
        self.log['comment'] = ""


    def to_json(self):
        return json.dumps(self, default=serializer, sort_keys=True, indent=4)


class Page:
    """Represents an HTTP Archive page"""
    def __init__(self):
        self.startedDateTime = datetime.now()
        self.id = ""
        self.title = ""
        self.pageTimings = {}
        self.pageTimings['onContentLoad'] = -1
        self.pageTimings['onLoad'] = -1
        self.pageTimings['comment'] = ""


    def to_json(self):
        return json.dumps(self, default=serializer, sort_keys=True, indent=4)


class Entry:
    """Represents an HTTP Archive entry"""
    def __init__(self):
        self.pageref = ""
        self.startedDateTime = datetime.now()
        self.time = 0
        self.request = {}
        self.request['method'] = "GET"
        self.request['url'] = ""
        self.request['httpVersion'] = "HTTP/1.1"
        self.request['cookies'] = []
        self.request['headers'] = []
        self.request['queryString'] = []
        self.request['postData'] = {}
        self.request['headersSize'] = -1
        self.request['bodySize'] = -1
        self.request['comment'] = ""
        self.response = {}
        self.response['status'] = 200
        self.response['statusText'] = "OK"
        self.response['httpVersion'] = "HTTP/1.1"
        self.response['cookies'] = []
        self.response['headers'] = []
        self.response['content'] = {}
        self.response['redirectUrl'] = ""
        self.response['headersSize'] = -1
        self.response['bodySize'] = -1
        self.response['comment'] = ""
        self.cache = {}
        self.cache['beforeRequest'] = {}
        self.cache['afterRequest'] = {}
        self.cache['comment'] = ""
        self.timings = {}
        self.timings['blocked'] = -1
        self.timings['dns'] = -1
        self.timings['connect'] = -1
        self.timings['send'] = 0
        self.timings['wait'] = 0
        self.timings['receive'] = 0
        self.timings['ssl'] = -1
        self.timings['comment'] = ""


        def to_json(self):
            return json.dumps(self, default=serializer, sort_keys=True, indent=4)
