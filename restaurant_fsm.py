from transitions import Machine

class RestaurantTable:
    states = ['available', 'occupied', 'order_placed', 'food_prepared', 'served', 'billing', 'cleaning']

    def __init__(self, table_id):
        self.table_id = table_id
        self.machine = Machine(model=self, states=RestaurantTable.states, initial='available')

        self.machine.add_transition('seat_customer', 'available', 'occupied')
        self.machine.add_transition('place_order', 'occupied', 'order_placed')
        self.machine.add_transition('prepare_food', 'order_placed', 'food_prepared')
        self.machine.add_transition('serve_food', 'food_prepared', 'served')
        self.machine.add_transition('generate_bill', 'served', 'billing')
        self.machine.add_transition('clean_table', 'billing', 'available')
