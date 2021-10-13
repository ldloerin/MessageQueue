class CreateOutputText():
    def create_text(total_power_curve):
        output_text = "time; meter_power[kW]; pv_power[kW]; total_power[kW]"
        for item in total_power_curve:
            time = item[0]
            meter_power = item[1]
            pv_power = item[2]
            total_power = item[3]
            output_text += '\n' + time + '; %.3f' % meter_power + '; %.3f' % pv_power + '; %.3f' % total_power
        return output_text
