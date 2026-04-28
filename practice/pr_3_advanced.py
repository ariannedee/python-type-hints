"""
Add type hints
"""

def calculate_order_total(product, quantity, discount_code):
    """Process a product order"""
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


def process_orders(orders):
    """Calculate totals for multiple orders"""
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


def find_expensive_orders(order_results, threshold):
    expensive = []
    for order in order_results:
        if order['total'] > threshold:
            expensive.append(order)
    return expensive

if __name__ == "__main__":
    laptop = {'name': 'Laptop', 'price': 999.99, 'sku': 'LAP001'}
    mouse = {'name': 'Mouse', 'price': 29.99, 'sku': 'MOU001'}

    orders = [
        {'product': laptop, 'quantity': 2, 'discount_code': 'SAVE10'},
        {'product': mouse, 'quantity': 5, 'discount_code': None},
        {'product': laptop, 'quantity': 1, 'discount_code': 'SAVE20'},
    ]

    order_results, total = process_orders(orders)
    expensive = find_expensive_orders(order_results, 500.0)

    print(f"Grand Total: ${total:.2f}")
    print(f"Expensive orders: {len(expensive)}")
