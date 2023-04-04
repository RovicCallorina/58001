class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance

    def centimeter(self):
        return self.__distance * 100

    def kilometer(self):
        return self.__distance / 1000

    def inches(self):
        return self.__distance * 39.37

    def display(self):

       print("The conversion from Meter to Centimeter is " , self.centimeter())
       print("The conversion from Meter to Kilometer is"  ,self.kilometer())
       print("The conversion from Meter to inches is"  ,self.inches())

distance = DistanceConversion(float(input("Meter: ")))
distance.display()









