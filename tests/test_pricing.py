import unittest

from app.pricing import OrderInput, PricingError, calculate_order_total


class PricingTest(unittest.TestCase):
    def test_regular_user(self):
        total = calculate_order_total(OrderInput(unit_price=100, quantity=3))
        self.assertEqual(total, 300.00)

    def test_gold_with_coupon(self):
        total = calculate_order_total(
            OrderInput(unit_price=200, quantity=2, member_level="gold", coupon=30)
        )
        self.assertEqual(total, 330.00)

    def test_total_not_negative(self):
        total = calculate_order_total(OrderInput(unit_price=10, quantity=1, coupon=999))
        self.assertEqual(total, 0.00)

    def test_invalid_quantity(self):
        with self.assertRaises(PricingError):
            calculate_order_total(OrderInput(unit_price=10, quantity=0))


if __name__ == "__main__":
    unittest.main()
