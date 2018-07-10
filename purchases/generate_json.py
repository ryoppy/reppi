import base64


class GenerateJson(object):
    def __init__(self):
        self.request_json = {}

    def generate(self, image_file):
        request_list = []

        with open(image_file, 'rb') as image_file:
            content_json_obj = {
                'content': base64.b64encode(image_file.read()).decode('UTF-8')
            }

        feature_json_obj = [{
            'type': 'TEXT_DETECTION',
            'maxResults': 10,
        }]

        request_list.append({
            'features': feature_json_obj,
            'image': content_json_obj,
        })

        self.request_json = {
            'requests': request_list
        }

        return self.request_json
