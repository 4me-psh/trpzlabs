class TagElement:
    def accept(self, visitor):
        visitor.visit_tag(self)

#Клас елементу тег