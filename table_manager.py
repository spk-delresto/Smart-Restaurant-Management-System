import heapq

class TableManager:
    def __init__(self):
        self.available_tables = []
        heapq.heapify(self.available_tables)

    def add_table(self, table_id, capacity):
        heapq.heappush(self.available_tables, (-capacity, table_id))

    def assign_table(self, group_size, is_reservation=False):
        if not self.available_tables:
            print("No tables available.")
            return None
        _, table = heapq.heappop(self.available_tables)
        print(f"Assigned table: {table} for group size: {group_size} (Reservation: {is_reservation})")
        return table
