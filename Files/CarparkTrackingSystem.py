class CarParkTrackingSystem():
    def __init__(self, _carparks = [], _parkings = []):
        self._carparks = _carparks
        self._parkings = _parkings

    def addCarpark(self, carpark):
        for car in self._carparks:
            if carpark.address == car.address: #Checking if the collection has the car address
                return False #If it does, we return False
        #Else, we append it and return True
        self._carparks.append(carpark)
        return True

    def searchCarParkById(self, carparkId):
        for car in self._carparks:
            if car._carparkId == carparkId:
                return car
        return None

    def searchCarParkByAddress(self, address):
        for car in self._carparks:
            if car._address == address:
                return car
        return None

    def getParkingByVehicleNumber(self, vehicleNumber, currentOnly = True):
        for park in self._parkings:
            if park.vehicle == vehicleNumber:
                return park

    def getParkingByCarpark(self, carparkId, currentOnly = True):
        pass #Work in progress

    def addParking(self, parking):
        self._parkings.append(parking)# Needs to have some restrictions and a raise

    def listParkingByAllCarpark(self):
        returned_string = ""
        currently_parked = 0
        completed_parked = 0
        total_currently_parked = 0
        for carpark in self._carparks:
            returned_string += "Detail of carpark " + carpark.__str__() + "\n"
            for park in self._parkings:
                if park.carpark._ID == carpark._ID:
                    returned_string += park.__str__() + "\n"
                    if park.timeOut == None:
                        currently_parked += 1
                        total_currently_parked += 1 #This one won't get resetted so we can check how many are in total
                    else:
                        completed_parked += 1

            returned_string += "Number of completed parking: " + str(completed_parked) + "\n"
            returned_string += "Number of vehicles parked in carpark currently: " + str(currently_parked) + "\n"
            currently_parked = 0
            completed_parked = 0
        returned_string += "Summary for all carparks" + "\n"
        returned_string +=  f"Number of vehicles parked in all carparks currently: {total_currently_parked}"
        return returned_string