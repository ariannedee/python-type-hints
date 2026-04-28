"""
Add type hints to functions. Find at least 2 bugs.
"""
from typing import TypeAlias, TypedDict, NewType

SKU = NewType("SKU", str)


class Product(TypedDict):
    name: str
    price: float
    sku: SKU


class Order(TypedDict):
    product: Product
    quantity: int
    discount_code: str | None


class OrderResult(TypedDict):
    product_name: str
    quantity: int
    base_price: float
    discount: float
    total: float


OrderResults: TypeAlias = list[OrderResult]


def calculate_order_total(product: Product, quantity: int, discount_code: str | None) -> OrderResult:
    base_price = product['price'] * quantity

    if discount_code == "SAVE10":
        discount = base_price * 0.10
    elif discount_code == "SAVE20":
        discount = base_price * 0.20
    else:
        discount = 0.0

    total = base_price - discount

    return {
        'product_name': product['name'],
        'quantity': quantity,
        'base_price': base_price,
        'discount': discount,
        'total': total
    }


def process_orders(orders: list[Order]) -> tuple[list[OrderResult], float]:
    results = []
    grand_total = 0.0

    for order in orders:
        order_result = calculate_order_total(
            order['product'],
            order['quantity'],
            order.get('discount_code', None)
        )
        results.append(order_result)
        grand_total += order_result['total']

    return results, grand_total


if __name__ == "__main__":
    # Product data
    laptop: Product = {'name': 'Laptop', 'price': 999.99, 'sku': SKU('LAP001')}
    mouse: Product = {'name': 'Mouse', 'price': 29.99, 'sku': SKU('MOU001')}

    # Orders
    orders: list[Order] = [
        {'product': laptop, 'quantity': 2, 'discount_code': 'SAVE10'},
        {'product': mouse, 'quantity': 5, 'discount_code': None},
        {'product': laptop, 'quantity': 1, 'discount_code': 'SAVE20'},
    ]

    # Run the code
    order_results, total = process_orders(orders)

    print(f"Grand Total: ${total:.2f}")