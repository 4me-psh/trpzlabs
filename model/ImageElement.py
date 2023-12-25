class ImageElement:
    def accept(self, visitor):
        visitor.visit_image(self)

#Клас елементу зображення