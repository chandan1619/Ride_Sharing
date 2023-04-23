from __future__ import annotations
from abc import ABCMeta
from enum import Enum



class Person(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name


class RideStatus(Enum):
    Idle =1
    Started= 2
    Cancelled = 3
    COmpleted = 4

class Ride:

    amount_per_km = 10 

    def __init__(self,id,src,dest,seats, status):
        self.id = id
        self.src= src
        self.dest = dest
        self.seats = seats
        self.status = status

    
    @property
    def id_get(self):
        return self.id
    
    @id_get.setter
    def id_set(self,id):
        self.id = id
    
    @property
    def get_status(self):
        return self.status
    
    @get_status.setter
    def set_status(self, status):
        self.status = status

    

class Rider(Person):

    previous_ride = []

    def __init__(self, name, ride):
        super().__init__(name)
        self.ride = ride

    
    def create_ride(self,id,src,dest,seats):

        if src > dest :
            return f"{src} is greater than {dest}"
        self.ride = Ride(id,src,dest,seats,RideStatus.Idle)
    
    def start_ride(self):

        if self.ride.status == RideStatus.Idle:
            self.ride.status = RideStatus.Started
        else:
            return f"this is not the valid ride"
    
    def update_ride(self,id,src,dest,seats,status):
        if id != self.ride.id:
            return f"can not update the ride"

        if self.ride.status == RideStatus.COmpleted:
            return f"the ride with id {self.ride.id} is already completed"
        
        self.ride = Ride(id,src,dest,seats,status)
    
    def withdraw_ride(self, status):

        if self.ride.status == RideStatus.COmpleted:
            return f"ride is already completed"
        
        if self.ride.status == RideStatus.Started:
            return f"ride is already started"
        
        self.ride.status = status
        
    
    def close_ride(self):
        return self.calculate_fare(self.ride)

    def calculate_fare(self, ride):

        Rider.previous_ride.append(ride)

        if ride.seats == 1:
            return (ride.dest - ride.src) * Ride.amount_per_km * 0.5 if len(Rider.previous_ride) > 10 else 0.75
        return  (ride.dest - ride.src)*ride.seats*Ride.amount_per_km *  0.5 if len(Rider.previous_ride) > 10 else 0.75




class Driver(Person):
    def __init__(self, name):
        super().__init__(name)


if __name__ == "__main__":
    driver = Driver("abc")

    ride = Ride(1,10,50,1,RideStatus.Idle)
    rider = Rider("chandan", ride)
    print(rider.start_ride())
    print(rider.withdraw_ride(RideStatus.Cancelled))
    print(rider.update_ride(1,10,50,1,RideStatus.Cancelled))

