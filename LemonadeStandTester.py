import unittest
from LemonadeStand import LemonadeStand
from LemonadeStand import MenuItem
from LemonadeStand import InvalidSalesItemError

if __name__ == '__main__':
    unittest.main()

class TestLemonadeStand(unittest.TestCase):

    def test_get_item_name(self):
        item = MenuItem("ice", 0.50, 1.00)
        self.assertEqual(item.get_item_name(), "ice")

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

        """
        def test_enter_sales_for_day_error(self):
            new_stand = LemonadeStand("lemons2cool")
            item1 = MenuItem("lemon", .5, 1)
            new_stand.add_menu_item(item1)
            sales0 = {"lemon": 2}
            sales1 = {"tuna": 5}
            new_stand.enter_sales_for_today(sales0)
    
            with self.assertRaises(InvalidSalesItemError):
                new_stand.enter_sales_for_today(sales1)
        """

    def test_get_selling_price(self):
        item1 = MenuItem("lemon", 0.5, 1)
        self.assertEqual(item1.get_selling_price(), 1)

    def test_assert_true(self):
        item1 = MenuItem("lemon", 0.5, 1)
        self.assertTrue(item1.get_item_name().islower())





