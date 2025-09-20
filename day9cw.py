class Vehicle:
    def __init__(self, vehicle_id: str, base_rate: float):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate

    def display_details(self):
        return f"""Vechicle ID = {self._vehicle_id}
Base Rate = {self._base_rate}"""
    def rental_charge(self):
        return 0.0    
  
        
class Car(Vehicle):
    def __init__(self,vehicle_id:str,base_rate:float,num_seats:int):
        super().__init__(vehicle_id,base_rate)
        self.num_seats = num_seats
    
    def rental_charge(self):
        return self._base_rate * self.num_seats
    
class Bike(Vehicle):
    def __init__(self, vehicle_id:str, base_rate:float,bike_type:str):
        super().__init__(vehicle_id,base_rate)
        self.bike_type = bike_type

    def rental_charge(self):
        return self._base_rate * 0.5
    
def calculate_rental(vehicle:Vehicle):
    print(vehicle.display_details())
    return f""" vehicle.rental_charge()
    *********************"""


car1 = Car("car1101",700.00,5)
bike1 = Bike("bike101",500,"scooter")

rental_rate = calculate_rental(car1)
print(rental_rate)

print(calculate_rental(bike1))





    
    
