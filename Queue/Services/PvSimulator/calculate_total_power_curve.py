class CalculateTotalPowerCurve():
    def execute_workflow(self, meter_curve, pv_curve):
        self.__check_list_length(meter_curve, pv_curve)
        self.__calc_total_power_curve(meter_curve, pv_curve)

    def __check_list_length(self, meter_curve, pv_curve):
        len_meter_curve = len(meter_curve)
        len_pv_curve = len(pv_curve)
        if len_meter_curve != len_pv_curve:
            raise ValueError('Lenght of Meter Curve and PV Curve Input lists does not match!')

    def __calc_total_power_curve(self, meter_curve, pv_curve):
        self.total_power_curve = []
        for i in range(0, len(meter_curve)):
            time = meter_curve[i][0]
            meter_power = meter_curve[i][1]
            pv_power = pv_curve[i]
            total_power = meter_power + pv_power
            self.total_power_curve.append([time, meter_power, pv_power, total_power])
