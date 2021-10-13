class CalculateTotalPowerCurve():

    def __init__(self, input):
        self.meter_curve = input.meter_curve
        self.pv_curve = input.pv_curve
        self.__check_list_length()
        self.__calc_total_power_curve()
    
    def __check_list_length(self):
        len_meter_curve = len(self.meter_curve)
        len_pv_curve = len(self.pv_curve)
        if len_meter_curve != len_pv_curve:
            raise ValueError('Lenght of Meter Curve and PV Curve Input lists does not match!')
    
    def __calc_total_power_curve(self):
        self.total_power_curve = []
        for i in range(0, len(self.meter_curve)):
            time = self.meter_curve[i][0]
            meter_power = self.meter_curve[i][1]
            pv_power = self.pv_curve[i]
            total_power = meter_power + pv_power
            self.total_power_curve.append([time, meter_power, pv_power, total_power])