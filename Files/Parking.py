from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from . import ParkingCalculator

class ParkingException(Exception): #Defining the ParkingException, subclass of Exception class
    pass


class ParkingDetailException(ParkingException): #Defining a subclass ParkingDetailException of the ParkingException class
    def __init__(self, parkList, message):
        super().__init__(message)
        self._parkList = parkList

    @property
    def getParking(self):
        return self._parkList


class Parking(ABC): #Defining the abstract Parking class
    _calculator = None

    def __init__(self, timeIn, vehicleNumber, carpark, timeOut = None, charges = 0):
        self._timeIn = timeIn
        self._vehicleNumber = vehicleNumber
        self._carpark = carpark
        self._timeOut = timeOut
        self._charges = charges

    @property
    def timeIn(self):
        return self._timeIn

    @property
    def vehicle(self):
        return self._vehicleNumber

    @property
    def carpark(self):
        return self._carpark

    @property
    def timeOut(self):
        return self._timeOut

    @timeOut.setter
    def timeOut(self, NewtimeOut):
        NewtimeOut = datetime.strptime(NewtimeOut,"%d/%m/%Y %H:%M %p")
        self._timeIn = datetime.strptime(self._timeIn,"%d/%m/%Y %H:%M %p")

        NewtimeOut = datetime.strftime(NewtimeOut,"%d %b %Y %H:%M %p")
        self._timeIn = datetime.strftime(self._timeIn,"%d %b %Y %H:%M %p")
        if self._timeOut != None:
            raise ParkingException("Time out has already been recorded!")
        elif self._timeIn > NewtimeOut:
            raise ParkingException("Time out cannot be earlier than time in!")
        else:
            self._timeOut = NewtimeOut
            #calling the calculator of the vehicle to calculate the charges, and set _charges with the return value

    @property
    def charges(self):
        if self._timeOut == None:
            raise ParkingException("Charges not recorded yet as vehicle has not left carpark")
        else:
            return self._charges

    def __str__(self):
        timeout_message = self._timeOut if self._timeOut != None else f"*Parked in carpark {self.carpark._ID}"
        charges_message = self._charges if self._charges != 0 else "$0.00"
        timein_date = ""
        if isinstance(self._timeIn, str):
            try:
                timein_date = datetime.strptime(self._timeIn,"%d/%m/%Y %H:%M %p") #Transforming the date from str to a datetime
            except:
                pass
        if isinstance(self._timeOut, datetime):
            try:
                timein_date = datetime.strftime(timein_date,"%d %b %Y, %H:%M %p") #Formatting the date as we need
            except:
                pass
        return f"Time In: {timein_date} Time Out: {timeout_message} Charges: {charges_message} \nCarpark {self._carpark.__str__()}\nVehicle: {self._vehicleNumber}"

    def __repr__(self):
        return self.__str__()

class MotorbikeParking(Parking): #Defining the MotorbikeParking class
    _parkingCalculator = ParkingCalculator.MotorbikeParkingCalculator()

    def __str__(self):
        return Parking.__str__(self) + " Motor Bike"


class CarParking(Parking): #Defining the CarParking class
    _parkingCalculator = ParkingCalculator.CarParkingCalculator()

    def __str__(self):
        return Parking.__str__(self) + " Car"