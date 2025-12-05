'''
We expect the code below to output "Spartacus weighs 45 lbs and is 24 inches tall." 

Why does our change_info method not work as expected?
'''

class GoodDog:
    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def change_info(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def info(self):
        return f"{self.name} weighs {self.weight} and is {self.height} tall."

sparky = GoodDog('Spartacus', '12 inches', '10 lbs')
sparky.change_info('Spartacus', '24 inches', '45 lbs')
print(sparky.info())
# => Spartacus weighs 10 lbs and is 12 inches tall.


'''
 So, what we have right now is when we call the `info` method, it doesn't look like the `change_info` method has worked as expected. So, let's have a look at the class definition.

The class is called `GooDoc`. It's going to initialize a method assigning instance variables `name`, `height`, and `size`. And then we call it `changeweight` with the arguments that have been passed. It also has an instant method called `change_info` that takes in the similar arguments. And finally, it's got `info` with only `self` passed to it returning a value.

So, in line 21, we instantiate a `GooDoc` object with those attributes `name`, `height`, and `weight`. And then we call `change_info`. We can see though that this is not going to work because instead of referencing instance variables, we are actually using local variables instead. Instance variables would have the prefix `self` so that it tells Python that we should be updating the instance variable. So, `name` here is a local variable. So, it's `height` and `weight`, and they would disappear or their state when you persist within that method itself. So, it hasn't actually gone and update our instance variable.

So, if we wanted the `change_info` to work as expected, we would have to update lines 14 to 16 to add the prefix `self`.
'''