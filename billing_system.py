class BillingSystem:
    def calculate_bill(self, order_items, tax_rate=0.1, discount=0):
        subtotal = sum(item['price'] for item in order_items)
        tax = subtotal * tax_rate
        total = subtotal + tax - discount
        return {
            'subtotal': subtotal,
            'tax': tax,
            'discount': discount,
            'total': total
        }
