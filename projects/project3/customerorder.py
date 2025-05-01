from datastructures.array import Array
from projects.project3.orderitem import OrderItem


class CustomerOrder:
    """Saves customers order, including name and each item"""

    def __init__(self, name: str) -> None:
        self._order_name = name
        self._items = Array(starting_sequence=[], data_type=OrderItem)

    def append(self, item: OrderItem) -> None:
        if isinstance(item, OrderItem):
            self._items.append(item)
        else:
            raise TypeError("Cannot add something to Order that is not an order item")
        
    def __iter__(self) -> iter:
        for item in self._items:
            yield item
        

    def __repr__(self):
        return f"\n {self._order_name}: \n {'\n'.join([str(item) for item in self._items if item is not None])}"