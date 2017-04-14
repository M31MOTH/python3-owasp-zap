# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2016 the ZAP development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This file was automatically generated.
"""

class brk(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def is_break_all(self):
        """
        Returns True if ZAP will break on both requests and responses
        """
        return next(iter(self.zap._request(self.zap.base + 'break/view/isBreakAll/').values()))

    @property
    def is_break_request(self):
        """
        Returns True if ZAP will break on requests
        """
        return next(iter(self.zap._request(self.zap.base + 'break/view/isBreakRequest/').values()))

    @property
    def is_break_response(self):
        """
        Returns True if ZAP will break on responses
        """
        return next(iter(self.zap._request(self.zap.base + 'break/view/isBreakResponse/').values()))

    @property
    def http_message(self):
        """
        Returns the HTTP message currently intercepted (if any)
        """
        return next(iter(self.zap._request(self.zap.base + 'break/view/httpMessage/').values()))

    def brk(self, type, state, scope=None, apikey=''):
        """
        Controls the global break functionality. The type may be one of: http-all, http-request or http-response. The state may be true (for turning break on for the specified type) or false (for turning break off). Scope is not currently used.
        """
        params = {'type' : type, 'state' : state, 'apikey' : apikey}
        if scope is not None:
            params['scope'] = scope
        return next(iter(self.zap._request(self.zap.base + 'break/action/break/', params).values()))

    def set_http_message(self, httpheader, httpbody=None, apikey=''):
        """
        Overwrites the currently intercepted message with the data provided
        """
        params = {'httpHeader' : httpheader, 'apikey' : apikey}
        if httpbody is not None:
            params['httpBody'] = httpbody
        return next(iter(self.zap._request(self.zap.base + 'break/action/setHttpMessage/', params).values()))

    def cont(self, apikey=''):
        """
        Submits the currently intercepted message and unsets the global request/response break points
        """
        return next(iter(self.zap._request(self.zap.base + 'break/action/continue/', {'apikey' : apikey}).values()))

    def step(self, apikey=''):
        """
        Submits the currently intercepted message, the next request or response will automatically be intercepted
        """
        return next(iter(self.zap._request(self.zap.base + 'break/action/step/', {'apikey' : apikey}).values()))

    def drop(self, apikey=''):
        """
        Drops the currently intercepted message
        """
        return next(iter(self.zap._request(self.zap.base + 'break/action/drop/', {'apikey' : apikey}).values()))

    def add_http_breakpoint(self, string, location, match, inverse, ignorecase, apikey=''):
        """
        Adds a custom HTTP breakpont. The string is the string to match. Location may be one of: url, request_header, request_body, response_header or response_body. Match may be: contains or regex. Inverse (match) may be true or false. Lastly, ignorecase (when matching the string) may be true or false.  
        """
        return next(iter(self.zap._request(self.zap.base + 'break/action/addHttpBreakpoint/', {'string' : string, 'location' : location, 'match' : match, 'inverse' : inverse, 'ignorecase' : ignorecase, 'apikey' : apikey}).values()))

    def remove_http_breakpoint(self, string, location, match, inverse, ignorecase, apikey=''):
        """
        Removes the specified break point
        """
        return next(iter(self.zap._request(self.zap.base + 'break/action/removeHttpBreakpoint/', {'string' : string, 'location' : location, 'match' : match, 'inverse' : inverse, 'ignorecase' : ignorecase, 'apikey' : apikey}).values()))


