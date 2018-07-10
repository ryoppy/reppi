import requests


class SendRequest(object):
    def __init__(self):
        self.response_json = {}

    def send(self, data, api_key):

        request_url = 'https://vision.googleapis.com/v1/images:annotate?key=' + api_key
        response = requests.post(url=request_url,
                                 data=data,
                                 headers={'Content-Type': 'application/json'})
        response_json = response.json()

        return response_json
