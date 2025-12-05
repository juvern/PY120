'''
In the code below, we hope to output BOB on the last line. Instead, we get the original name. Why? How could we adjust this code to output BOB?
'''
class Person:
    def __init__(self, name):
        self.name = name

    def change_name(self):
        self.name = self.name.upper()

bob = Person('Bob')
print(bob.name)
bob.change_name()
print(bob.name)


'''
Okay, here we've been asked to comment as to why we haven't been able to output Bob in uppercase in the last line, and we basically just get the same name.

Okay, so let's look at the class definition. Class definition here is of a person, a person object. We have an `initialize` method which assigns `name` to the `incident` variable's `name`, and we also have an `incident` method called `changeName`, I think this is where I'm spotting the problem here.

Because what we have instead is not actually an instance variable assignment; we just have a local variable assignment. So instead of updating the value of `incident` variable `name`, we're just creating a local variable called `name`.

So no, it's no wonder that when we do finally print the attribute `name` in line 14, we basically just get the value of Bob in capitalized, the original form basically which is the value that's been passed at initialization.

So to sum up, line 12 would expect to see the `name` `bob.name` printed out as the original form. `changeName` doesn't actually do anything because it creates a local variable called `name`, and then when we do print line 14, we're actually just printing the value that was originally initialized. 
'''