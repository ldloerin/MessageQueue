class CreateOutputText():

    def __init__(self, input):
        self.total_power_curve = input.total_power_curve
        self.__create_text()
    
    def __create_text(self):
        self.output_text = "time; meter_power[kW]; pv_power[kW]; total_power[kW]"
        for item in self.total_power_curve:
            time = item[0]
            meter_power = item[1]
            pv_power = item[2]
            total_power = item[3]
            self.output_text += '\n' + time + '; %.3f'%meter_power + '; %.3f'%pv_power + '; %.3f'%total_power