


from projects.project3.drink import Drink

class OrderItem:
    """Pairs items with customizations"""

    def __init__(self, item: Drink, customization: str = "Normal") -> None:
        self._item = item
        self._cust = customization

    @property
    def item(self) -> Drink:
        return self._item

    def __repr__(self) -> str:
        return f"{self._item} ({self._cust})"