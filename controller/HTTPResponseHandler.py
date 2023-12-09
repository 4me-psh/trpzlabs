import urllib.request
import urllib.error
import HTTPRequestHandler
import model.ErrorsProxy as erpr


class HTTPResponseHandler:
    addressline = ''

    # основний метод для респонс
    def send_get_response(self, url):

        try:
            HTTPRequestHandler.HTTPRequestHandler.send_get_request(url)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                erpr.ErrorsProxy.error_404()
            elif err.code == 502:
                erpr.ErrorsProxy.error_502()
            elif err.code == 503:
                erpr.ErrorsProxy.error_503()
