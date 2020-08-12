class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def handle(self):
        print("accident occured. take detour")

    def print_exception(self):
        print("User defined exception, ", self.msg)


try:
    raise Accident('crash between two cars')
except Accident as e:
    e.print_exception()
    e.handle()

try:
    raise MemoryError('Memory error')
except MemoryError as e:
    print(e)
