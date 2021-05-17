import json
from DataStructures import Queue
from sms import send


# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")

print(type(queue.get_queue))


print(type(len(queue.get_queue())))

    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    if len(queue.get_queue()) > 0:
        print(queue.get_queue())
    else: print("No hay nadie en linea!") 

def add():
    name = str(input("Please insert name: "))
    number = input("Please insert phone number: ")
    item = {"name": name, "number" : number}
    queue.enqueue(item)

    if len(queue.get_queue()) == 0:
        print("No existen usuarios en cola")
    elif len(queue.get_queue()) < 2:
        print("Eres la primera persona en cola!")
    elif len(queue.get_queue()) > 1:
        print(f"Existen unas {len(queue.get_queue)} personas en cola!")
 

    print(f"Ahora faltan {queue.size()} personas en espera ")

def dequeue():

    if len(queue.get_queue()) != 0:
        deletedqueue = queue.dequeue()
        print(f"Se ha sacado a {deletedqueue}")
        print(f"Ahora faltan {queue.size()} personas en espera ")
    else: print("No existen personas en cola"

    # Falta agregar enviar el mini mensaje

def save():
      with open("queue.json", "w") as outfile:
        json.dump(queue.get_queue(),outfile,indent=4)
        print("Los cambios se han guardado")

def load():
    with open("queue.json") as file:
        data = json.load(file)
        queue.load_queue(data)
        return data

       




    
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    if option == 1:
        add()
    elif option == 2:
        dequeue()
    # add your options here using conditionals (if)
    elif option == 3:
        print_queue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
