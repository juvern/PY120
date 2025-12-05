class CPU:
    def __init__(self, core_count):
        self.core_count = core_count

    def process_data(self, data):
        return f"Processing '{data}' with {self.core_count} cores."

class RAM:
    def __init__(self, size_gb):
        self.size_gb = size_gb
        self.memory = []

    def allocate(self, data):
        self.memory.append(data)
        return f"Allocated memory for '{data}'."

class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        self.power_state = 'off'

    def boot(self):
        self.power_state = 'on'
        print("Computer is booting...")

    def run_program(self, program_data):
        if self.power_state == 'on':
            self.ram.allocate(program_data)
            result = self.cpu.process_data(program_data)
            print(result)
        else:
            print("Cannot run program. Computer is off.")

# Example Usage
my_cpu = CPU(8)
my_ram = RAM(16)
my_computer = Computer(my_cpu, my_ram)

my_computer.boot()
my_computer.run_program("my_file.txt")

'''
So we have three classes: CPU, RAM, and Computer. Let's determine the relationship between each of them.

At initialization, for the CPU class, we initialize the value of core count. For RAM, it looks like we initialize the size GB and also the memory. So let me... Okay. And then with Computer, we initialize the value of CPU and RAM, and also power state as well.

When we go to line 38, when we instantiate a Computer class, we can see here that we're passing in two arguments and there are actually two separate objects: a CPU object that has been initialized with the value 8 and a RAM object that has been initialized with the value 16. I can already see here that the relationship between Computer is a has-a: a Computer has a CPU and a Computer has a RAM.

When we call the method boot, that's all quite straightforward. We update or reassign the power state variable to on and then print "Computer is booting."

When we call the run_program instance method, if it's on (which it is because of the previous method call), we are now calling the method within the RAM class object here. There's collaboration going on here: the RAM object is collaborating with the Computer object. And then the assignment of the variable result is actually... again, we're calling a method processData within the CPU object. We can say that both CPU and RAM here are collaborators.

Let's see what result it actually prints out. We call run_program, we pass in the argument my_file.txt, we allocate the program data. When we allocate the program data, we append the data (in this instance, the program data) to the memory, which is the myFile.txt. So now the instance variable within RAM, or the variable myRAM, is going to be myFile.txt.

Then we print the result, and the result is basically the return value. The return value here is calling the method processData, so we're then saying processingData (which is my_file.txt) with the self.coreCount cores, and we know that those cores is 8. So the final print value here is "Processing myFile.txt with 8 cores." 

'''