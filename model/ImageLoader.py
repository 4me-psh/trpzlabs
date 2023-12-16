from PIL import Image
from io import BytesIO
import requests
from model.PageCompiler import PageCompiler


class ImageLoader(PageCompiler):
    def content_compile(self, image_url):
        self.load_image(image_url)

    addressline = ''

    # метод для завантаження зображень на сторінку
    def load_image(self, image_url):
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()
