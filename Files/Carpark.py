class CarPark():# Defining the CarPark class
    _carHalfHourlyRates = [[700, 1900, 0.6], [1900, 2230, 0.8]]
    _carNightCharge = 5
    _motorBikeCharges = [[700, 2230, 0.65]]
    _motorBikeNightCharge = 0.7
    _nextId = 1
    def __init__(self, _address):
        self._ID = CarPark._nextId
        self._address = _address
        CarPark._nextId += 1

    @property
    def _carparkId(self):
        return self._ID

    @_carparkId.setter
    def _carparkId(self,val):
        self._ID = val

    @property
    def address(self):
        return self._address

    def getCarHalfHourlyRate(self, aTime):
        for each_list in self._carHalfHourlyRates:
            if each_list[0] <= aTime < each_list[1]:
                return each_list
        return None

    def getMotorBikeCharge(self, aTime):
        for each_list in self._motorBikeCharges:
            if each_list[0] <= aTime < each_list[1]:
                return each_list
        return None

    def getCarNightCharge(self):
        return self._carNightCharge

    def getMotorBikeNightCharge(self):
        return self._motorBikeNightCharge

    def __str__(self):
        return f"ID: {self._ID} {self._address} **Outside of Central Area**"

    def __repr__(self):
        return self.__str__()


class CentralAreaCarPark(CarPark): # Defining the CentralAreaCarPark class
    _nightParkingSurcharge = 2
    _carHalfHourlyRates = [[700, 1700, 1.2], [1700, 2230, 0.9]]
    def __init__(self, _factor, _address):
        self._factor_adjust = _factor
        super().__init__(_address)

    @classmethod
    def getNightParkingSurcharge(cls):
        return cls._nightParkingSurcharge

    @classmethod
    def setNightParkingSurcharge(cls, val):
        cls._nightParkingSurcharge = val

    @property
    def factor(self):
        return  self._factor_adjust

    @factor.setter
    def factor(self, val):
        self._factor_adjust = val

    def getCarNightCharge(self):
        return self._nightParkingSurcharge + super()._carNightCharge

    def getCarHalfHourlyRate(self, aTime):
        for each_list in self._carHalfHourlyRates:
            each_list[-1] *= self._factor_adjust
            if each_list[0] <= aTime < each_list[1]:
                return each_list
        return None

    def __str__(self):
        return f"ID: {self._ID} Factor: {self._factor_adjust} {self.address} **Whithin Central Area**"