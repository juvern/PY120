class Store:
    def __init__(self, name, inventory_count):
        self.name = name
        self.inventory_count = inventory_count

    def sell_items(self, count):
        if self.inventory_count >= count:
            self.inventory_count -= count
            return True
        return False

class Franchise:
    def __init__(self, name):
        self.name = name
        self.stores = [] # A list of Store collaborators

    def add_store(self, store):
        self.stores.append(store)

    def hold_sale(self, items_sold_per_store):
        for store in self.stores:
            store.sell_items(items_sold_per_store)

# Setup
megacorp = Franchise("MegaCorp")
store_a = Store("Downtown", 100)
store_b = Store("Uptown", 120)

megacorp.add_store(store_a)
megacorp.add_store(store_b)

# Action
megacorp.hold_sale(10)

print(f"{store_a.name} inventory: {store_a.inventory_count}")
print(f"{store_b.name} inventory: {store_b.inventory_count}")

'''
Analyze the following code.

- What is the final output of this script? 
- Explain the relationship between the Franchise object and the Store objects. 
- How does the Franchise object use its collaborators to perform the hold_sale action?

We have two classes: `store` and `franchise`. Within the `store` class, we've got an `initialize` method that has the parameters `name` and `inventory_count`. Within the `franchise` class, we also have an `initialize` method with the state of `name` and `stores`. So we can see here that the class `franchise` or an instance of a `franchise` has a list of `stores`. So it's going to have a relationship, and it's doing so by using collaborative objects. The `franchise` object is having to collaborate with the `store` object to carry out its responsibilities.

So then in lines 25, we have `franchise` instantiated with the `name` argument, with the `name` Megacorp. There is no, sorry, `franchises` (it's just the name), and it's called an empty list instantiated to `self.stores`. And then we have two stores which are two `store` objects instantiated. The first has the name downtown with an inventory count of 100. And then another one called uptown with an inventory count of 120. These states are unique to each of these instances. And then we call the `at_store` method on the Megacorp (which is a `franchise` object).

So if we now look at the `at_store` method, this is a method which appends an object or appends what's been passed to the `store`s instant variable. So here we can see after lines 29, 20, and 30, two `store` objects would be part of the elements of the `stores` list within the `franchise` object of Megacorp. Okay, then the `franchise` object Megacorp here is we call the `wholesale` method on Megacorp passing in the value of 10.

So let's go back to the class definition. We see an `instant` method here called `hold_sale` and it's a for loop, so for every store in `franchise` which is in the list, we would sell the items. So we know here that each `store` object also has the method, the attribute `sell_items`. So now let's go back to the `store` class definition. And then we can see here though there's an if statement, so if inventory count is more than the count, we decrement and then return true. So the return values here is a boolean, but we're also doing a reassigning of the value of inventory count. So let's see, inventory count in downtown is 100, inventory count of uptown is 120, so they're both more than 10. Yep, so each of these inventory count instance variables is going to decrement, it's going to reduce by 10. So then we find when we then finally print out the statements `store` name, so that would access the attribute `name` of that instance variable which is downtown. So downtown inventory would be again the inventory count, so it would reduce by 10. So before it was 100, now it's 90, and then similarly in the following line, we have uptown inventory, and it would decrement it by 10, so that would be a 110. So we've already explained the relationship between a `franchise` object and a `store` object. A `franchise` has a store, so this is a has-a relationship, not an is-a relationship, and we can see here that the `franchise` object needs the collaborators to be able to perform the `hold_sale` action. So within the `hold_sale` method, it is accessing the `sell_items` method within the `store` object. 

'''
