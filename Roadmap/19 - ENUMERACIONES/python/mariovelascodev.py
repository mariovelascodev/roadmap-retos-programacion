from enum import Enum
    
class Weekday(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def what_day_is(number):

    try:
        if number > 0 or number < 8:
            print(Weekday(number).name)
    except:
        print("Solo hay 7 días a la semana introduce un número del 1 al 7")

what_day_is(2)
what_day_is(5)

#EXTRA
class Status(Enum):
    PENDIENTE = 0
    ENVIADO = 1
    ENTREGADO = 2
    CANCELADO = 3

class Order:
    
    status = Status.PENDIENTE.name

    #Constructor
    def __init__(self, id):
        self.id = id

    #Mostrat estado pedido
    def show_status(self):
        print(f"El pedido con ID {self.id} esta en estado {self.status}")

    #Modificar estado pedido
    def update_status(self):
        pass
    
order_1 = Order(1)
order_1.show_status()