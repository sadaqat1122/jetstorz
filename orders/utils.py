# orders/utils.py
import uuid

def generate_order_number():
    return str(uuid.uuid4()).replace('-', '')[:10]  # Generates a unique 10-character alphanumeric order number
