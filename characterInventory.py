import json

class CharacterInventory:
    def __init__(self, character_name):
        self.file_name = f"{character_name}_inventory.json"
        if os.path.isfile(self.file_name):
            with open(self.file_name, "r") as f:
                self.items = json.load(f)
        else:
            self.items = []

    def add_item(self, item_name):
        self.items.append(item_name)
        with open(self.file_name, "w") as f:
            json.dump(self.items, f)

    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            with open(self.file_name, "w") as f:
                json.dump(self.items, f)
        else:
            print(f"{item_name} not found in inventory")

    def list_items(self):
        print("Inventory:")
        for item in self.items:
            print(item)

