import numpy as np


class GeneratePvCurve():

    def __init__(self, input):
        self.day_length = len(input.meter_curve) # 1 measure point / 10 minutes during 24 hours
        self.sunrize = input.config['sunrize']
        self.sunset = input.config['sunset']
        self.ramp_steps = int(input.config['dawn'] * 6)
        self.max_pv_power = input.config['max_pv_power']
        self.__calculate_daylight()
        self.__create_solar_radiation_distribution()
        self.__initialize_pv_curve()
        self.__generate_pv_curve()
    
    def __calculate_daylight(self):
        '''measure points during estimated sun radiation between 08:00 - 19:50 in 10 minute steps'''
        self.daylight_length = (self.sunset - self.sunrize) * 6
    
    def __create_solar_radiation_distribution(self):
        self.x_values = np.linspace(1, self.daylight_length, self.daylight_length) 
        self.mu = int(self.daylight_length / 2)
        self.sigma = 15
        self.__gaussian()
    
    def __gaussian(self):
        self.y_values = list(np.exp(-np.power(self.x_values - self.mu, 2.) / (2 * np.power(self.sigma, 2.))))
    
    def __initialize_pv_curve(self):
        self.morning_measure_points = self.sunrize * 6 
        self.morning_measure_points -= self.ramp_steps

    def __generate_pv_curve(self):
        ramp_value = self.y_values[0] / self.ramp_steps
        self.pv_curve = [0] * self.morning_measure_points
        for i in range(1, self.ramp_steps):
            self.pv_curve.append(ramp_value * i)
        self.pv_curve += self.y_values
        ramp_value = self.y_values[-1] / self.ramp_steps
        for i in range(self.ramp_steps - 1, -1, -1):
            self.pv_curve.append(ramp_value * i)
        self.pv_curve += [0] * (self.day_length - len(self.pv_curve))
        for i in range(0, len(self.pv_curve)):
            self.pv_curve[i] = self.pv_curve[i] * self.max_pv_power