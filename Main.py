from datetime import datetime
from Files import  Parking, Carpark, CarparkTrackingSystem


def CarParkApplication():
    while True:
        print("Menu")
        print("1. Park a Vehicle")
        print("2. Exit Carpark")
        print("3. Display Parking Summary for all Carparks")
        print("0. Exit")
        while True:
            try:
                user_input =int(input("Enter option: "))
                if user_input in [0,1,2,3]:
                    break
            except:
                print("The input is not a number")
        if user_input == 1:
            while True:
                try:
                    parking_type_input = int(input("Enter type of parking 1 - Car 2 - Motor bike: ")) #Getting the type of vehicle
                    if parking_type_input in [1,2]:
                        carpark_id_input = int(input("Enter carpark id: ")) #Getting the ID of the vehicle
                        if Park_System.searchCarParkById(carpark_id_input) != None: #Checking if the carpark ID exists in a carpark
                            vehicle_number_input = input("Enter vehicle number: ") #Getting the Number of vehicle
                            if True:
                                time_in_input = input("Enter time in in dd/mm/yyyy hh:mm AM/PM format: ") #Getting the time In of the vehicle
                                try :
                                    datetime.strptime(time_in_input, '%d/%m/%Y %H:%M %p')
                                except:
                                    raise Parking.ParkingException("Not in correct dd/mm/yyyy hh:mm AM/PM format")

                                #Checking if the Vehicle is already registered
                                if Park_System.getParkingByVehicleNumber(vehicle_number_input) == None:
                                    pass
                                else:
                                    raise Parking.ParkingDetailException(Park_System._parkings, "Error in adding a parking. Parking record shows vehicle is still in a carpark")
                                    break

                                #If everything's okay, we add it to the system
                                if carpark_id_input == 1: #If it's a Car
                                    parked = Parking.CarParking(time_in_input, vehicle_number_input, Car_parking)
                                    Park_System.addParking(parked)
                                elif carpark_id_input == 2: #If it's a Motorbike
                                    parked = Parking.MotorbikeParking(time_in_input, vehicle_number_input, Central_Car_Parking)
                                    Park_System.addParking(parked)

                                print(parked.__str__() + " *added.")

                                break

                        else:
                            raise Parking.ParkingException("carpark id does not belong to any carpark")
                    else:
                        raise Parking.ParkingException("Parking type is not a correct parking type.")
                except Parking.ParkingDetailException as e:
                    print(e)
                    print(Park_System.getParkingByVehicleNumber(vehicle_number_input))
                    while True:
                        choice = input("Do you want to exit the vehicle for this parking? y/n: ")
                        if choice == "y":
                            Park_System._parkings.pop()
                            if carpark_id_input == 1 :
                                parked = Parking.CarParking(time_in_input, vehicle_number_input, Car_parking)
                                Park_System.addParking(parked)
                            elif carpark_id_input == 2:
                                parked = Parking.MotorbikeParking(time_in_input, vehicle_number_input, Central_Car_Parking)
                                Park_System.addParking(parked)
                            print(parked.__str__() + " *added.")
                            break
                        elif choice == "n":
                            print("Choosing not to exit previous parking.")
                            break
                    break
                except Parking.ParkingException as e:
                    print(e)
                    break
                except:
                    print("Invalid value")
                    break
        elif user_input == 2:
            while True:
                try:
                    vehicle_number_input = input("Enter vehicle number: ")
                    if Park_System.getParkingByVehicleNumber(vehicle_number_input) != None:
                        vehicle_parking = Park_System.getParkingByVehicleNumber(vehicle_number_input)
                        print(vehicle_parking) #Showing the vehicle details
                        time_out_input = input("Enter time out in dd/mm/yyyy hh:mm AM/PM format: ") #Getting the time out of the vehicle
                        try :
                            datetime.strptime(time_out_input, '%d/%m/%Y %H:%M %p')
                        except:
                            raise Parking.ParkingException("Not in correct dd/mm/yyyy hh:mm AM/PM format")
                        print(time_out_input)
                        vehicle_parking.timeOut = time_out_input
                        break
                    else:
                        raise Parking.ParkingException("No vehicle found")
                except Parking.ParkingException as e:
                    print(e)
                    break
        elif user_input == 3:
            print(Park_System.listParkingByAllCarpark())
        elif user_input == 0:
            print("Exiting the program")
            break
#The above function still needs to be cut into smaller sections for readability, optimisation and debugging purposes


if __name__ == "__main__":
    Car_parking = Carpark.CarPark("11A Clementi Ave 12") #Example of Carpark, with the given Address
    Central_Car_Parking = Carpark.CentralAreaCarPark(1.1, "123 Syed Ameen Road")
    Park_System = CarparkTrackingSystem.CarParkTrackingSystem()
    Park_System.addCarpark(Car_parking) #Adding the carparks to the System, and set it's ID to 1, as it's the first Carpark
    Park_System.addCarpark(Central_Car_Parking) #Adding the carparks to the System, with ID as 2
    CarParkApplication()