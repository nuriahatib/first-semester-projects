# Code to generate dictionary summary reports
def generate_report(orders):
    """
    Generate summary report:
    - Total products sold
    - Most popular product
    - Revenue per customer
    """
    total_sold = 0
    product_count = {}
    revenue_per_customer = {}

    for order in orders:
        product = order["product"]
        qty = order["quantity"]
        price = float(order["price"])
        customer = order["customer"]

        total_sold += qty
        product_count[product] = product_count.get(product, 0) + qty
        revenue_per_customer[customer] = revenue_per_customer.get(customer, 0) + (price * qty)

    most_popular = max(product_count, key=product_count.get)

    return {
        "total_products_sold": total_sold,
        "most_popular_product": most_popular,
        "revenue_per_customer": revenue_per_customer
    }
