import unittest
from LemonadeStand import LemonadeStand
from LemonadeStand import MenuItem
from LemonadeStand import SalesForDay
from LemonadeStand import InvalidSalesItemError


class TestLemonadeStand(unittest.TestCase):

    def test_get_name(self):
        new_stand = LemonadeStand("lemons2cool")
        self.assertEqual(new_stand.get_name(), "lemons2cool")

    def test_enter_sales_for_day(self):
        new_stand = LemonadeStand("lemons2cool")
        item1 = MenuItem("lemon", .5, 1)
        new_stand.add_menu_item(item1)
        sales = {"lemon": 5}
        new_stand.enter_sales_for_today(sales)
        self.assertEqual(new_stand.sales_of_menu_item_for_day(0,"lemon"), 5)

    def test_enter_sales_for_day_error(self):
        new_stand = LemonadeStand("lemons2cool")
        item1 = MenuItem("lemon", .5, 1)
        new_stand.add_menu_item(item1)
        sales = {"tuna": 5}

        with self.assertRaises(InvalidSalesItemError):
            new_stand.enter_sales_for_today(sales)






