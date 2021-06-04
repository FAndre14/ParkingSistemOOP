from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class ParkingCalculator(ABC): # Defining the ParkingCalculator class

    def calculateCharge(self, timeIn, timeOut, carpark):
        get_time_in = str(int(f"{timeIn:%H}")) + str(f"{timeIn:%M}")
        total_charged = 0
        if  (timeOut- timeIn).seconds / 60 <=10:
            print("Under 10 minute difference")
            return total_charged
        else:
            while timeIn <= timeOut: #While time in has not passed time out, keep looping
                if 700 <= int(get_time_in) <= 2230: #We check if we're in the day shifts
                    for rate_list in carpark._carHalfHourlyRates:
                        if rate_list[0] <= int(get_time_in) < rate_list[1]:
                            while int(get_time_in) <= rate_list[1]:
                                if timeIn >= timeOut:
                                    break
                                total_charged += rate_list[2]
                                timeIn += timedelta(minutes = 30)
                                get_time_in = str(int(f"{timeIn:%H}")) + str(f"{timeIn:%M}")
                elif int(get_time_in) > 2230: #Applying the Night shift rate
                            total_charged += 5
                            timeIn = datetime(timeIn.year, timeIn.month, timeIn.day + 1, 7, timeIn.second * 60)
                            get_time_in = str(int(f"{timeIn:%H}")) + str(f"{timeIn:%M}")
            return total_charged



    @abstractmethod
    def getDayRate(self, startTime, carpark):
        pass

    @abstractmethod
    def getNightRate(self, carpark):
        pass

    @abstractmethod
    def getCharges(self, endTime, startTime, rate):
        pass


class MotorbikeParkingCalculator(ParkingCalculator): #Defining MotorbikeParkingCalculator class
    def getDayRate(self, startTime, carpark):
        return carpark.getMotorBikeCharge(startTime)[-1]

    def getNightRate(self, carpark):
        return carpark.getMotorBikeNightCharge()

    def getCharges(self, endTime, startTime, rate):
        print("Motorbike calculator")
        carpark = rate
        return ParkingCalculator.calculateCharge(self, startTime, endTime, carpark)


class CarParkingCalculator(ParkingCalculator): #Defining CarParkingCalculator class
    def getDayRate(self, startTime, carpark):
        return carpark.getCarHalfHourlyRate(startTime)[-1]

    def getNightRate(self, carpark):
        return carpark.getCarNightCharge()

    def getCharges(self, endTime, startTime, rate):
        pass #To do