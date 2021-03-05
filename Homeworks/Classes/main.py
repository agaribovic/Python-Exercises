class Vehicle:
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance
    
    def setMake(self, make):
        self.make = make
        
    def setModel(self):
        self.model = model
        
    def setYear(self):
        self.year = year
    
    def setWeight(self):
        self.weight = weight
        

class Cars(Vehicle):
    
    def __init__(self,  make, model, year, weight, needsMaintenance, tripsSinceMaintenance):
        super().__init__(make, model, year, weight, needsMaintenance, tripsSinceMaintenance) 
        self.isDriving = False
    
    def Drive(self):
        self.isDriving = True
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True
        
    def Stop(self):
        self.isDriving = False
    
    def Repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False
        
Car1 = Cars("BMW", "Q5", 2021, "1500kg", False, 99)

print("\nCar make:", Car1.make, "\nCar model:", Car1.model, "\nCar year:", Car1.year, "\nCar weight:", Car1.weight,"\nCar needs maintenance:", Car1.needsMaintenance, "\nCar number of trips:", Car1.tripsSinceMaintenance, "\nCar is driving:", Car1.isDriving, "\n")

Car1.Drive()

print(Car1.make, Car1.model, "needs maintenance:", Car1.needsMaintenance, "& number of trips since maintenance:", Car1.tripsSinceMaintenance)

Car1.Drive()

print(Car1.make, Car1.model, "needs maintenance:", Car1.needsMaintenance, "& number of trips since maintenance:", Car1.tripsSinceMaintenance)

Car1.Repair()

print(Car1.make, Car1.model, "needs maintenance:", Car1.needsMaintenance, "& number of trips since maintenance:", Car1.tripsSinceMaintenance, "\n")

Car2 = Cars("Renault", "Clio", 2013, "1000kg", False, 100)

print("Car make:", Car2.make, "\nCar model:", Car2.model, "\nCar year:", Car2.year, "\nCar weight:", Car2.weight,"\nCar needs maintenance:", Car2.needsMaintenance, "\nCar number of trips:", Car1.tripsSinceMaintenance, "\nCar is driving:", Car1.isDriving, "\n")

print(Car2.make, Car2.model, "needs maintenance:", Car2.needsMaintenance, "& number of trips since maintenance:", Car2.tripsSinceMaintenance)

Car2.Drive()

print(Car2.make, Car2.model, "needs maintenance:", Car2.needsMaintenance, "& number of trips since maintenance:", Car2.tripsSinceMaintenance)

Car2.Repair()

print(Car2.make, Car2.model, "needs maintenance:", Car2.needsMaintenance, "& number of trips since maintenance:", Car2.tripsSinceMaintenance, "\n")

Car3 = Cars("Audi", "TT", 2018, "1200kg", True, 101)

print("Car make:", Car3.make, "\nCar model:", Car3.model, "\nCar year:", Car3.year, "\nCar weight:", Car3.weight,"\nCar needs maintenance:", Car3.needsMaintenance, "\nCar number of trips:", Car3.tripsSinceMaintenance, "\nCar is driving:", Car3.isDriving, "\n")

print(Car3.make, Car3.model, "needs maintenance:", Car3.needsMaintenance, "& number of trips since maintenance:", Car3.tripsSinceMaintenance)

Car3.Repair()

print(Car3.make, Car3.model, "needs maintenance:", Car3.needsMaintenance, "& number of trips since maintenance:", Car3.tripsSinceMaintenance, "\n")

Car3.Drive()

print(Car3.make, Car3.model, "is driving:", Car3.isDriving)

Car3.Stop()

print(Car3.make, Car3.model, "is driving:", Car3.isDriving)