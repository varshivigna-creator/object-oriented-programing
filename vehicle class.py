class vehicle:
    def  __init__ (self,max_speed,mileage):

        self.max_speed=max_speed
        self.mileage=mileage

car=vehicle(250,100) 

print("max speed:",car.max_speed)
print(" mileage:",car.mileage)