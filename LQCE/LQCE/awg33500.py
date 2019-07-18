# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:59:18 2019

@author: Aurelian
"""
import LQCE.instr as instr



class awg33500(instr.Instr):
    
    def __init__(self, visa_name):
        super(awg33500,self).__init__(visa_name)
        self.cls()
        self._visainstrument.read_termination = '\n'
        self._visainstrument.timeout = 5000
        

    def set_voltage(self, channel = 1, voltage = 0):
        self.write("SOURce{}:VOLTage {}".format(channel, voltage))
    def set_voltage_units(self, units = "VPP"):
        """
        set units
        available formats: VPP | VRMS | DBM 
        """
        self.write("VOLTage:UNIT {}".format(units))
    def set_voltage_offset(self,channel, offset):
        self.write("SOURce{}:VOLTage:OFFSet {}".format(channel, offset))
    def set_frequency(self, channel = 1, freq = 10000):
        self.write("SOURce{}:AM:INTernal:FREQuency {}".format(channel, freq))
    def set_waveform_type(self, channel, waveform_type = "PULSe"):
        """
        SINusoid | SQUare | PULSe | RAMP | NRAMp | TRIangle | NOISe | PRBS | ARB | DC
        """
        self.write("SOURce{}:FUNCtion {}".format(channel, waveform_type))
    def set_output(self, channel , state):
        self.write("OUTPut{} {}".format(channel, state))
    def set_output_polarity(self, channel, polarity = "NORMal"):
        """NORMal | INVerted"""
        self.write("OUTPut{}:POLarity {}".format(channel, polarity))
    def set_sync_output(self, state = "OFF"):
        """ OFF | ON """
        self.write("OUTPut:SYNC {}".format(state))
    def set_sync_mode(self,channel = 1, mode = "NORMal"):
        """CARRier | NORMal | MARKer"""
        self.write("OUTPUT{}:SYNC:MODE {}".format(channel, mode))
    def set_polarity(self, channel, polarity = "NORMAL"):
        """NORMAL | INVerted"""
        self.write("OUTPUT{}:SYNC:POLARITY {}".format(channel, polarity))
    def set_sync_source(self, channel = "CH1"):
        """
        set the channel as a source of sync output
        CH1 | CH2 available params
        """
        self.write("OUTPUT:SYNC:SOURCE {}".format(channel))
    def set_pulse_period(self, channel, period):
        """
        previously need to set pulse function to Period param
        set the period of pulse in seconds
        """
        self.write("SOURce{}:FUNCtion:PULSe:PERiod {}".format(channel, period))
    def set_pulse_width(self, channel, width):
       self.write("SOURce{}:FUNCtion:PULSe:WIDTh {}".format(channel, width))
    def set_pulse_duty_cycle(self, channel, duty_cycle):
        """
        Duty Cycle = 100(Pulse Width )/Period
        Pulse duty cycle: 0% to 100%
        duty cycle - percents
        """
        self.write("SOURce{}:FUNCtion:PULSe:DCYCle {}".format(channel, duty_cycle))
    def set_pulse_leading_edge(self, channel, edge):
        self.write("SOURce{}:FUNCtion:PULSe:TRANsition:LEADing {}".format(channel, edge))
    def set_pulse_trailing_edge(self, channel, edge):
        self.write("SOURce{}:FUNCtion:PULSe:TRANsition:TRAiling {}".format(channel, edge))
    def set_pulse_both_edge(self, channel, edge):
        self.write("SOURce{}:FUNCtion:PULSe:TRANsition:BOTH {}".format(channel, edge))
    def set_modulation_source(self, source = "INTernal"):
        """INTernal | EXTernal | CH1 | CH2"""
        self.write("AM:SOURce {}".format(source))
    def set_trigger_slope(self, slope = "POSitive"):
        """POSitive | NEGative"""
        self.write("OUTPut:TRIGger:SLOPe {}".format(slope))
    def set_triger_output(self, state = "OFF"):
        """ON | OFF"""
        self.write("OUTPut:TRIGger {}".format(state))
    def set_burst_state(self, channel = 1, state = "OFF"):
        """ON | OFF"""
        self.write("SOURce{}:BURSt:STATe {}".format(channel, state))
    def set_burst_mode(self, channel, mode = "TRIGgered"):
        """TRIGgered | GATed"""
        self.write("SOURce{}:BURSt:MODE {}".format(channel, mode))
    def set_burst_polarity(self, channel, polarity = "NORMal"):
        """NORMal | INVerted"""
        self.write("SOURce{}:BURSt:GATE:POLarity {}".format(channel, polarity))
    def set_waveform_frequency(self, channel = 1, freq = 10000):
        self.write("SOURce{}:FREQuency {}".format(channel, freq))
    def set_burst_count(self, channel, cycles = 1):
        self.write("SOURce{}:BURSt:NCYCles {}".format(channel, cycles))
    def set_burst_period(self, channel, period):
        self.write("SOURce{}:BURSt:INTernal:PERiod {}".format(channel, period))
    def set_burst_trigger_source(self, channel = 1, source = "IMMediate"):
        """IMMediate | EXTernal | TIMer | BUS"""
        self.write("TRIGger{}:SOURce {}".format(channel, source))
    def set_trigger_source(self, channel = 1, source = "IMMediate"):
        """IMMediate | EXTernal | TIMer | BUS"""
        self.write("TRIGger{}:SOURce {}".format(channel, source))
    def send_trigger(self):
        self.write("*TRG")
    def set_burst_phase(self, channel, phase):
        """
        set phase in angles value
        -360 to +360
        3.6 of angle corresponded to 0.01 of period
        """
        self.write("SOURce{}:BURSt:PHASe {}".format(channel, phase))
    def synchronize_channels(self):
        self.write("SOURce1:PHASe:SYNChronize")
        self.write("SOURce2:PHASe:SYNChronize")
    
    def set_phase_units(self, units = "DEG"):
        """DEGree | RADian | SECond """
        self.write("UNIT:ANGLe {}".format(units))
    def awg_init_burst_mode(self):  
        self.set_modulation_source("INT")
        self.set_waveform_type(1,"PULSe")
        self.set_waveform_type(2,"DC")
        self.set_voltage_offset(2, 0)
        self.set_voltage_offset(1, 0.05)
        self.set_pulse_width(1,1e-6)#set width 100ns
        self.set_pulse_period(1,1e-4)#set period 1ms
        self.set_pulse_both_edge(1, 20e-9)
        self.set_sync_source("CH1")
        self.set_sync_mode(1, "CARRier")
        self.set_burst_state(1,"ON")
        self.set_burst_mode(1, "TRIGgered")
        self.set_burst_count(1, 10000)
        self.set_burst_trigger_source(1, "BUS")
        self.set_sync_output("ON")
        self.set_output(1, "ON")
        self.set_output(2, "ON")
    def awg_init(self, mixer_calibration_result):  
        self.set_modulation_source("INT")
        self.set_waveform_type(1,"PULSe")
        self.set_waveform_type(2,"DC")
        self.set_voltage_offset(2, mixer_calibration_result[1])
        self.set_voltage_offset(1, 0.05 + mixer_calibration_result[0])
        self.set_pulse_period(1,13e-6)
        self.set_voltage(1,100e-3)
        self.set_pulse_width(1,15e-6)
        self.set_pulse_period(1,15e-6)
        self.set_pulse_both_edge(1, 20e-9)
        self.set_sync_source("CH1")
        self.set_sync_mode(1, "CARRier")
        self.set_sync_output("ON")
        self.set_output(1, "ON")
        self.set_output(2, "ON")
    def awg_init_custom(self, mixer_calibration_result, readout_width, period):  
        self.set_modulation_source("INT")
        self.set_waveform_type(1,"PULSe")
        self.set_waveform_type(2,"DC")
        self.set_voltage_offset(2, mixer_calibration_result[1])
        self.set_voltage_offset(1, 0.5 + mixer_calibration_result[0])
        self.set_voltage(1,1000e-3)
        self.set_pulse_period(1,period)
        self.set_pulse_width(1,readout_width)
        self.set_pulse_period(1,period)
        self.set_pulse_both_edge(1, 20e-9)
        self.set_sync_source("CH1")
        self.set_sync_mode(1, "CARRier")
        self.set_sync_output("ON")
        self.set_output(1, "ON")
        self.set_output(2, "ON")
    def awg_init_custom_2ch(self, mixer_calibration_result, readout_width, period):  
        self.set_modulation_source("INT")
        self.set_waveform_type(1,"PULSe")
        self.set_waveform_type(2,"PULSe")
        self.set_voltage_offset(2, 0.5 + mixer_calibration_result[1])
        self.set_voltage_offset(1, 0.5 + mixer_calibration_result[0])
        self.set_voltage(2,1000e-3)
        self.set_voltage(1,1000e-3)
        
        self.set_pulse_period(1,period)
        self.set_pulse_width(1,readout_width)
        self.set_pulse_period(1,period)
        self.set_pulse_both_edge(1, 20e-9)
        
        self.set_pulse_period(2,period)
        self.set_pulse_width(2,readout_width)
        self.set_pulse_period(2,period)
        self.set_pulse_both_edge(2, 20e-9)  
        
        self.set_sync_source("CH1")
        self.set_sync_mode(1, "CARRier")
        self.set_sync_output("ON")
        self.set_output(1, "ON")
        self.set_output(2, "ON") 
        
    def awg_base_init(self):  
        self.set_waveform_type(1,"DC")
        self.set_waveform_type(2,"DC")
        self.set_voltage_offset(1, 0)
        self.set_voltage_offset(2, 0)
        self.set_sync_output("OFF")
        self.set_output(1, "ON")
        self.set_output(2, "ON")
    def awg_set_voltage_with_offset(value, offset):
        self.set_voltage_offset(1, offset[0] + value/2)
        self.set_voltage(1, value)
    def awg_set_delay(self, delay):
        self.set_phase_units("SEC")
        self.write("SOURce1:PHASe {}".format(-100e-9 - delay*1e-9))
        #awg.write("SOURce2:PHASe {}".format(-100e-9 - delay*1e-9))
