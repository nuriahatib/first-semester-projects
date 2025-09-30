# Entry point for the MiniMart data reporting system
from utils import apply_discount
from report_generator import generate_report

# Simulating new orders
orders = [
    {"customer": "Alice Johnson", "product": "Milk", "price": "50", "quantity": 2},
    {"customer": "Bob Smith", "product": "Bread", "price": "30", "quantity": 5},
    {"customer": "Alice Johnson", "product": "Eggs", "price": "120", "quantity": 1},
    {"customer": "Charlie Brown", "product": "Rice", "price": "200", "quantity": 3},
    {"customer": "Diana Prince", "product": "Sugar", "price": "150", "quantity": 2}
]

# Applying discount example
discounted_price = apply_discount("200", 15)
print(f"Discounted Price: {discounted_price}")

# Identifying customers with large orders
print("\nCustomers with large orders:")
for order in orders:
    if order["quantity"] >= 3 or float(order["price"]) * order["quantity"] > 500:
        print(f"{order['customer']} placed a large order of {order['quantity']} {order['product']}")

# Generating the report
report = generate_report(orders)

print("\nSales Report:")
print(f"Total products sold: {report['total_products_sold']}")
print(f"Most popular product: {report['most_popular_product']}")
print("Revenue per customer:")
for customer, revenue in report["revenue_per_customer"].items():
    print(f"  {customer}: {revenue}")
