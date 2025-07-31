from restaurant_fsm import RestaurantTable
from table_manager import TableManager
from billing_system import BillingSystem

# FSM Demo
table1 = RestaurantTable(1)
print(f"Initial State: {table1.state}")
table1.seat_customer()
print(f"After seating customer: {table1.state}")
table1.place_order()
print(f"After placing order: {table1.state}")

# Table Manager Demo
tm = TableManager()
tm.add_table("T1", 4)
tm.add_table("T2", 6)
tm.add_table("T3", 2)

assigned_table = tm.assign_table(3, is_reservation=True)

# Billing Demo
billing = BillingSystem()
order = [
    {'name': 'Burger', 'price': 250},
    {'name': 'Fries', 'price': 100},
    {'name': 'Drink', 'price': 80}
]
bill = billing.calculate_bill(order_items=order, tax_rate=0.13, discount=30)

print("\n📋 Final Bill:")
print(f"Subtotal: Rs. {bill['subtotal']}")
print(f"Tax (13%): Rs. {bill['tax']}")
print(f"Discount: Rs. {bill['discount']}")
print(f"Total: Rs. {bill['total']}")
