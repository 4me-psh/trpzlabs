class P2PNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.resources = {}  # Словник для зберігання ресурсів, доступних на цьому вузлі

    def share_resource(self, resource_id, resource_data):
        # Додавання ресурсу до доступних на цьому вузлі
        self.resources[resource_id] = resource_data

    def request_resource(self, resource_id, requesting_node):
        # Перевірка доступності ресурсу на цьому вузлі
        if resource_id in self.resources:
            # Якщо ресурс доступний, відправити його запитуючому вузлу
            return self.resources[resource_id]
        else:
            # Якщо ресурс відсутній, повернути відповідь про відсутність ресурсу
            return f"Ресурс із ID {resource_id} не знайдено."

#Клас для реалізації моделі взаємодії peer-to-peer