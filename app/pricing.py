"""Simple order pricing domain logic."""

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderInput:
    unit_price: float
    quantity: int
    member_level: str = "regular"  # regular, silver, gold
    coupon: float = 0.0


MEMBER_DISCOUNT = {
    "regular": 0.0,
    "silver": 0.05,
    "gold": 0.10,
}


class PricingError(ValueError):
    """Raised when order input is invalid."""


def calculate_order_total(order: OrderInput) -> float:
    if order.unit_price < 0:
        raise PricingError("unit_price 不能为负数")
    if order.quantity <= 0:
        raise PricingError("quantity 必须大于 0")
    if order.member_level not in MEMBER_DISCOUNT:
        raise PricingError("member_level 仅支持 regular/silver/gold")
    if order.coupon < 0:
        raise PricingError("coupon 不能为负数")

    subtotal = order.unit_price * order.quantity
    discount = subtotal * MEMBER_DISCOUNT[order.member_level]
    total = subtotal - discount - order.coupon
    return round(max(total, 0.0), 2)
