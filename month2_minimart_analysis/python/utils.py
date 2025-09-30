# Utility functions for data conversion and filtering
def apply_discount(price_str, discount_percent=10):
    """
    Convert price from string to float and apply discount.
    """
    try:
        price = float(price_str)
        discounted = price - (price * discount_percent / 100)
        return round(discounted, 2)
    except ValueError:
        print(f"Invalid price: {price_str}")
        return None
