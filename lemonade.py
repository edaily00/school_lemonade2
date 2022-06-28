class MenuItem:

    def __init__(self, item_name, wholesale_cost, selling_price):
        self._item_name = item_name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_item_name(self):
        return self._item_name

    def get_wholesale_cost(self):
        return self._wholesale_cost

    def get_selling_price(self):
        return self._selling_price


class SalesForDay:

    def __init__(self, days_open, sales_dict):
        self._days_open = days_open
        self._sales_dict = sales_dict

    def get_day(self):
        return self._days_open

    def get_sales_dict(self):
        return self._sales_dict


class LemonadeStand:

    def __init__(self, name):
        self._name = name
        self._current_day = 0
        self._menu_dict = {}
        self._sales_for_day = []

    def get_name(self):
        return self._name

# Here I am able to use menu_item methods with period, I wanted to:
#                                                          self._menu_dict[menu_item.get_item_name() = menu_item
    def add_menu_item(self, menu_item):
        self._menu_dict[
            menu_item.get_item_name()] = menu_item

    def get_menu_dict(self):
        return self._menu_dict

    def enter_sales_for_today(self, sales_dict):
        all_sales = self._menu_dict.copy()
        try:
            for key in sales_dict:
                if key not in all_sales:
                    raise InvalidSalesItemError
        except InvalidSalesItemError:
            print("You entered an item not on the menu. NO SALES RECORDED")

        else:
            for key in all_sales:
                if key in sales_dict:
                    all_sales[key] = sales_dict[key]
                elif key not in sales_dict:
                    all_sales[key] = 0
            self._sales_for_day.append(all_sales.copy())
            self._current_day += 1

    def sales_of_menu_item_for_day(self, day, item_name):
        return self._sales_for_day[day][item_name]

    def total_sales_for_menu_item(self, item_name):
        total = 0
        length = len(self._sales_for_day)
        for i in range(length):
            total += self.sales_of_menu_item_for_day(i, item_name)
        return total

#Here when I tried to use menu_item with period get wholesale it does not work. I tried changing the parameter's name
#to menu_item still didnt work

    def total_profit_for_menu_item(self, item_name):
        total_sold = self.total_sales_for_menu_item(item_name)
        item_net_cost = self._menu_dict[item_name].get_selling_price() - self._menu_dict[item_name].get_wholesale_cost()
        profit = total_sold * item_net_cost
        return profit

    def total_profit_for_stand(self):
        total_profit = 0
        for key in self._menu_dict:
            total_profit += self.total_profit_for_menu_item(key)
        return total_profit


class InvalidSalesItemError(Exception):
    pass


"""
stand = LemonadeStand("Lemons Forever")
item1 = MenuItem("strawberry", 0.5, 1.25)
stand.add_menu_item(item1)
item2 = MenuItem("lemon", 0.25, 0.75)
stand.add_menu_item(item2)
item3 = MenuItem("tart", 1.00, 2.25)
stand.add_menu_item(item3)

day_0_sales = {
    "lemon": 1,
    "strawberry": 2,
    "tuna": 5
}
sales_2 = {
    "strawberry": 15,
    "lemon": 12,
    "tart": 6
}
sales_3 = {
    "strawberry": 10,
    "tart": 5
}
stand.enter_sales_for_today(day_0_sales)
stand.enter_sales_for_today(sales_2)
stand.enter_sales_for_today(sales_3)
print(stand.sales_of_menu_item_for_day(0, "lemon"))
print(stand.get_menu_dict())
print(stand.total_profit_for_stand())

"""
