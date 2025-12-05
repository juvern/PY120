class Device:
    def __init__(self, name):
        self.name = name

    def connect(self):
        return f"{self.name} is connecting..."

class Printer(Device):
    def __init__(self, name, ink_level):
        super().__init__(name)
        self.ink_level = ink_level

    def connect(self):
        status = super().connect()
        return f"{status} Connection successful."

    def print_document(self, doc_name):
        if self.ink_level > 0:
            self.ink_level -= 1
            return f"Printing '{doc_name}'. Ink level: {self.ink_level}"
        else:
            return "Cannot print. Low ink."

class Computer:
    def __init__(self, name, peripheral):
        self.name = name
        self.peripheral = peripheral # A Device object

    def run_task(self):
        print(self.peripheral.connect())
        print(self.peripheral.print_document("MyEssay.docx"))

my_printer = Printer("OfficeJet", 2)
my_computer = Computer("MacBook Pro", my_printer)

my_computer.run_task()
my_computer.run_task()
my_computer.run_task()

'''
What is the exact output when this script is run?

We have three classes here, one called Device and then we've got Printer which inherits from Device and then Computer. So let's start with the instantiation of Printer in line 33. So over here we've got Printer which has the arguments OfficeJet and To. When we instantiate the object we would also run the initializer method within Printer. We notice here that there is a super function calling initializer passing in the argument Permit and name. Super function here represents a proxy class that allows us to call the DunderInit method of the super class so that is why so rather than initialize self self dot name we can just extend the functionality of our initializer method so we would initialize the value self dot name equals OfficeJet and then the second the following line We would initialize the instant wearable ink level with the value of two Then we instantiate a computer object passing in the values of Macbook Pro and the object for myPrinter so let's now go back to the class definition for Computer so we see here that after instantiating the object We run the initializer method where we will pass value of self dot name or assign value of Macbook pro to instant wearable name and then the object myPrinter or which is an instant of the object printer to peripheral okay now let's see what happens when we run task so we call upon the method run task myComputer which is a computer object would then call the method runTask there is the method called runTask The first thing it will do is print which is this print statement which has a connect method disconnect method exists within the printer objects right yeah so when we do so what this line would prints over this time would do is call that connect method within the printer object The status here is going to extend from the divider So if you are running a device class which is the superclass and what do we have here? The status here is self.Name is connecting so in this instance the self is the computer So the name is MacBook pro so computer is connecting the name of the self The name that has been-the instant variable name within the computer instance... to this. So we would have computer, MacBook Pro is connecting, and now let's go back to the runToConnect, and then it would return the status, which is the return value- And it would end-oh sorry let me go back runTask run connect yep and then it would say connection MacBook Pro's connecting dot dot dot connection successful would print The second line calls printDocument The calling object here is the printer object so let's go to the printDocument which accepts a doc_name argument. We know the self.ink_level is 2. As it'smore than two we would have to reduce or decrement the ink level by one so now the ink- Self.ink level is gonna be reduced by one and then we finally print "Printing 'MyEssay.docx'. Ink level: 2"

The second line would follow a similar process. It will decrement the ink level to 2, 1, and then print "Printing 'MyEssay.docx'. Ink level: 1". However, the last one though is going to be different because it is going to return "Cannot print low ink." 



'''