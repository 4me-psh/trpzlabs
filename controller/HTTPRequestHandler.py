import requests


class HTTPRequestHandler:

    def send_get_request(self, url):
        response = requests.get(url)
        return response.text
