class ScriptElement:
    def accept(self, visitor):
        visitor.visit_script(self)

#Клас елементу скрипт