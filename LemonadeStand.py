#Author: Eric Daily
#Github username: edaily00
#date: 6/23/2022
#This program can create items, record sales, and tell you how much you profited
class MenuItem:
    # initializing menu item class with name wholesale and selling price
    def __init__(self, item_name, wholesale_cost, selling_price):
        self._item_name = item_name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price
    # creating get methods for class
    def get_item_name(self):
        return self._item_name

    def get_wholesale_cost(self):
        return self._wholesale_cost

    def get_selling_price(self):
        return self._selling_price


class SalesForDay:
    #initializing sales for day class which uses day and a sales dictionary
    def __init__(self, days_open, sales_dict):
        self._days_open = days_open
        self._sales_dict = sales_dict
    # creating get methods
    def get_day(self):
        return self._days_open

    def get_sales_dict(self):
        return self._sales_dict


class LemonadeStand:
    #initializing the stand with a name the class also keeps track of the day, a menu, and sales for the day
    def __init__(self, name):
        self._name = name
        self._current_day = 0
        self._menu_dict = {}
        self._sales_for_day = []

    def get_name(self):
        return self._name
    #putting menu item object into the meny
    def add_menu_item(self, menu_item):
        self._menu_dict[menu_item.get_item_name()] = menu_item

    def get_menu_dict(self):
        return self._menu_dict
        #takes the sales dictionary and and adds it to the sales for day list
    def enter_sales_for_today(self, sales_dict):

        all_sales = self._menu_dict.copy()
        #barely understand this. If an item on the sale dict doesnt match to the menu it raises an exception
        # and dumps all data.. It seems to work, but I cannot get the test to work assertRaise(InvalidSalesItemError)
        try:
            for key in sales_dict:
                if key not in all_sales:
                    raise InvalidSalesItemError
        except InvalidSalesItemError:
            print("Entered item not on the menu! NO SALES RECORDED!")
        else:
            for key in all_sales:
                if key in sales_dict:
                    all_sales[key] = sales_dict[key]
                elif key not in sales_dict:
                    all_sales[key] = 0
            self._sales_for_day.append(SalesForDay(self._current_day, all_sales.copy()))
            self._current_day += 1
        #returns sales of item for particular day
    def sales_of_menu_item_for_day(self, day, item_name):
        return self._sales_for_day[day].get_sales_dict()[item_name]
        #returns total sales for item
    def total_sales_for_menu_item(self, item_name):
        total = 0
        length = len(self._sales_for_day)
        for i in range(length):
            total += self.sales_of_menu_item_for_day(i, item_name)
        return total
        #uses total sales and item costs to get profit
    def total_profit_for_menu_item(self, item_name):
        total_sold = self.total_sales_for_menu_item(item_name)
        item_net_cost = self._menu_dict[item_name].get_selling_price() - self._menu_dict[item_name].get_wholesale_cost()
        profit = total_sold * item_net_cost
        return profit
        #adds up all profits from each item
    def total_profit_for_stand(self):
        total_profit = 0
        for key in self._menu_dict:
            total_profit += self.total_profit_for_menu_item(key)
        return total_profit


class InvalidSalesItemError(Exception):
    pass

#main fuction
def main():

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
        "strawberry": 5,
        "lemon": 10,
        "tart": 0
    }
    sales_3 = {
        "strawberry": 0,
        "tart": 0
    }
    stand.enter_sales_for_today(day_0_sales)
    stand.enter_sales_for_today(sales_2)
    stand.enter_sales_for_today(sales_3)


if __name__ == '__main__':
    main()
