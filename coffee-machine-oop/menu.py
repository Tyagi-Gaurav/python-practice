from prettytable import PrettyTable


class Menu:
    def __init__(self, menu_item):
        self.menu_item = menu_item

    def __str__(self):
        x = PrettyTable()
        x.field_names = ["Available commands", "description"]

        for item in self.menu_item:
            x.add_row([item.item_name, item.description])

        return x.get_string()


class MenuItem:
    def __init__(self, item_name, description):
        self.item_name = item_name
        self.description = description
