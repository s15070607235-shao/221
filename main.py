from app.pricing import OrderInput, calculate_order_total


def main() -> None:
    order = OrderInput(unit_price=199, quantity=2, member_level="gold", coupon=20)
    total = calculate_order_total(order)
    print(f"订单总价: ¥{total}")


if __name__ == "__main__":
    main()
