from datastructures.linkedlist import LinkedList
from projects.project3.drink import Drink, DrinkList, Prices
from projects.project3.customerorder import CustomerOrder
from projects.project3.orderitem import OrderItem
from projects.project3.text_fix import text_fix



class BistroSystem:
    """Main bistro system run code"""

    def __init__(self):
        self._open_orders = LinkedList(data_type=CustomerOrder)
        self._finished_orders = LinkedList(data_type=CustomerOrder)
        self.Menu()
        self._itemnames = dict()
            

    def Menu(self) -> None:
        """Menu system code, does each case for menu 1-6"""
        ch = input("Main Menu: \n" \
        "1. Display Menu \n" \
        "2. Take New Order \n" \
        "3. View Open Orders \n" \
        "4. Mark Next Order as Complete \n" \
        "5. View End-of-Day Report \n" \
        "6. Exit \n \n" \
        "Enter your choice: ")
        try:
            int(ch)
        except:
            self.Menu()
        match int(ch.strip()):
            case 1:
                print("Menu: (Prices listed for M size)")
                print(*[f"{DrinkList[item.name].value}. {text_fix(item.name)}: ${item.value }" + "\n" for item in Prices])
                print("\n")
                self.Menu()
            case 2:
                self.Order()
                print("\n")
                self.Menu()
            case 3:
                print(*self._open_orders)
                print("\n")     
                self.Menu()        
            case 4:
                if not self._open_orders.empty:
                    print(f"Order for {self._open_orders.head.data._order_name} is completed!")
                    self._finished_orders.append(self._open_orders.head.data)
                    self._open_orders.remove(self._open_orders.head.data)
                    print("\n")
                else:
                    print("No orders to complete!")
                self.Menu()
            case 5:
                l = []
                value = 0.0
                if self._open_orders.empty:
                    for order in self._finished_orders:
                        for item in order:
                            if item is not None:
                                l.append(item.item)
                    for item in l:
                        value += item.value
                        value = round(value, 2)
                    print("End of Day Report: \n" \
                            "---------------------")
                    print(*[item.name + "   $" + str(item.value) + "\n" for item in l])
                    print(f"Total Revenue: {value}")



                else:
                    print("Finish all your orders first!")
                    print("\n")
                    self.Menu()
            case 6:
                exit()

    def Order(self, order: CustomerOrder = None) -> None:
        """Ordering an item, goes through name, drink, size, and customization"""
        if order is None:
            order = CustomerOrder(input("What is the name for the order? "))
        for i in range(int(input("How many drinks would you like to order? "))):
            drink = int(input(f"Drink #{i+1}: Enter drink number (1-{len(DrinkList)}) "))
            size = input(f"What size do you want your {DrinkList(drink).name}?  (S, M, L) ")
            customization = input(f"Any customization for {DrinkList(drink).name}? ")
            order.append(OrderItem(Drink(drink, size), customization))
        confirm = input(f"Confirm order? (yes/no) ")
        if confirm.strip().upper() in ["N", "NO"]:
            self.Order(order)
        else:
            print("Order placed successfully!")
            self._open_orders.append(order)
            