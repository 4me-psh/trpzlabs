import requests


class HTTPRequestHandler:
    #змінна для адресного рядка
    addressline = ''

    #основний метод для реквестів
    def send_get_request(self, url):
        response = requests.get(url)
        return response.text
