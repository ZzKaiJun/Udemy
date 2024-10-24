# 類繼承

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"   # !r 調用 self 的 repr方法
    
    def disconnect(self):
        self.connected = False
        print("Disconnect.")


printer = Device("printer" , "USB")
print(printer)
printer.disconnect()


# Printer 繼承至 Device ， 有Device 的 method
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # self.name = name
        # self.connected_by = connected_by
        # self.connected = True
        super().__init__(name, connected_by)                         # 使用super class 
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)" 
    
    def print(self, pages):
        if self.connected == False:
            print("Your printer is not connected.")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer" , "USB" , 500)
printer.print(20)

print(printer)

printer.disconnect()
printer.print(30)