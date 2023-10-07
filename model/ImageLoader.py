from PIL import Image
from io import BytesIO
import requests


class ImageLoader:

    def load_image(self, image_url):
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()
