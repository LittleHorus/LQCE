# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:11:49 2019

@author: Numeon
"""

import LQCE.instr as instr
import numpy as np
import math


class zvl13(instr.Instr):
    
    def __init__(self, visa_name):
        super(zvl13,self).__init__(visa_name)
        self.cls()
        self._visainstrument.read_termination = '\n'
        self._visainstrument.timeout = 5000
        
    def get_parameters(self):
        return {"bandwidth":self.get_bandwidth(),
                "nop":self.get_nop(),
                "power":self.get_power(),
                "averages":self.get_averages(),
                "freq_limits":self.get_freq_limits(),
                "cf_span":self.get_cf_span(),
                "meas_counts":self.get_meas_counts()}
    def set_parameters(self,parameters_dict):
        """
        Method allowing to set all or some of the nwa parameters at once
        (bandwidth,nop,power,averages,freq_limits)
        """
        if "bandwidth" in parameters_dict.keys():
            self.set_bandwidth(parameters_dict["bandwidth"])
        if "nop" in parameters_dict.keys():
            self.set_nop(parameters_dict["nop"])
        if "power" in parameters_dict.keys():
            self.set_power(parameters_dict["power"])
        if "averages" in parameters_dict.keys():
            self.set_averages(parameters_dict["averages"])
        if "freq_limits" in parameters_dict.keys():
            self.set_freq_limits(parameters_dict["freq_limits"])
        if "cf_span" in parameters_dict.keys():
            self.set_cf_span(parameters_dict["cf_span"])
        if "meas_counts" in parameters_dict.keys():
            self.set_meas_counts(parameters_dict["meas_counts"])
    def select_S_param(self, S_param = "S21", channel = 1):
        """
        select S measurement type
        channel not used
        S_param type S11 | S12 | S21 | S22
        """
        self.write("CALCulate{}:PARameter:MEASure trc1, {}".format(channel, S_param))
    
    def trigger_setup(self, trigger_mode = "IMMediate"):
        """
        trigger mode selection
        immediate | external
        """
        self.write("TRIGger:SOURce {}".format(trigger_mode))
    def set_averages(self,averages):
        self.write("AVERage:COUNt {}".format(averages))
    def get_averages(self):
        return(self.query("AVERage:COUNt?"))
    def set_average_state(self,average_state = "OFF"):
        self.write("AVERage: {}".format(average_state))
    def clear_average(self):
        self.write("AVERage: CLEar")
    def set_bandwidth(self, bandwidth):
        self.write("SENSe1:BANDwidth:RES {}".format(bandwidth))
    def get_bandwidth(self):
        return (self.query("SENSe1:BANDwidth:RES?"))
    def set_nop(self, nop):
        self.write("SWEep:POINts {}".format(nop))
    def get_nop(self):
        return (self.query("SWEep:POINts?"))        
    def set_power(self, power):
        self.write('SOURce1:POWer {}'.format(power))
    def get_power(self):
        return (self.query('SOURce1:POWer?'))
    def set_output_state(self, output_state):
        self.write("OUTPut1 {}".format(output_state))
    def get_output_state(self):
        return (self.query("OUTPut1?"))
    def set_freq_limits(self, freq_limits):
        self.write("SENSe:FREQuency:START {}".format(freq_limits[0]))
        self.write("SENSe:FREQuency:STOP {}".format(freq_limits[1]))
    def get_freq_limits(self):
        return [self.query("SENSe:FREQuency:START?"), self.query("SENSe:FREQuency:STOP?")]#list of 2 arg
    def set_cf_span(self, cf_span = [2.5e9, 2e9]):
        self.write("FREQ:CENT {}".format(cf_span[0]))
        self.write("FREQ:SPAN {}".format(cf_span[1]))
    def get_data(self, data_frames_count):
        curves = [0]*data_frames_count
        out_data = []
        out_phase = []
        out_data_re = []
        out_data_im = []
        for i in range(data_frames_count):
            curves[i] = self.query("CALCulate1:DATA:NSWeep? SDATa, {}".format(i+1))
            np_d = np.fromstring(curves[i], sep = ',')
            temp_data = []*int(len(np_d)/2)
            temp_phase = []*int(len(np_d)/2)
            temp_re = []*int(len(np_d)/2)
            temp_im = []*int(len(np_d)/2)
            
            for j in range(int(len(np_d)/2)):
                temp_data.append(20*math.log(math.sqrt(np_d[2*j]**2+np_d[2*j+1]**2),10))
                temp_phase.append(math.atan2(np_d[2*j+1],np_d[2*j]))
                temp_re.append(np_d[2*j])
                temp_im.append(np_d[2*j+1])
            out_data.append(temp_data)
            out_phase.append(temp_phase)
            out_data_re.append(temp_re)
            out_data_im.append(temp_im)
        return (out_data, out_phase, out_data_re, out_data_im)
    def get_formatted_data(self, data_frames_count = 1, format = 'ReIm'):
        '''Supported formats: ReIm(default) | S21Phase'''
        curves = [0]*data_frames_count
        
        if format == 'ReIm':
            re = []
            im = []
            av_re = []
            av_im = []
            for i in range(data_frames_count):
                curves[i] = self.query("CALCulate1:DATA:NSWeep? SDATa, {}".format(i+1))
                np_data =  np.fromstring(curves[i], sep = ',')
                temp_re = []*int(len(np_data)/2)
                temp_im = []*int(len(np_data)/2)
                for j in range(int(len(np_data)/2)):
                    temp_re.append(np_data[2*j])
                    temp_im.append(np_data[2*j+1])
                re.append(temp_re)
                im.append(temp_im)
            av_re = np.average(re, 0)
            av_im = np.average(im, 0)
            return (av_re, av_im)
        if format == 'S21Phase':
            s21 = []
            phase = []
            av_s21 = []
            av_phase = []
            for i in range(data_frames_count):
                curves[i] = self.query("CALCulate1:DATA:NSWeep? SDATa, {}".format(i+1))
                np_data = np.fromstring(curves[i], sep = ',')
                temp_s21 = []*int(len(np_data)/2)
                temp_phase = []*int(len(np_data)/2)            
                for j in range(int(len(np_data)/2)):
                    temp_s21.append(20*math.log(math.sqrt(np_data[2*j]**2+np_data[2*j+1]**2),10))
                    temp_phase.append(math.atan2(np_data[2*j+1],np_data[2*j])) 
                s21.append(temp_s21)
                phase.append(temp_phase)
            if data_frames_count == 1:
                return (s21,phase)
            av_s21 = np.average(s21, 0)
            av_phase = np.average(phase, 0)
            return (av_s21, av_phase)
        
    def set_data_mode(self, mode):
        """
        this func set the format of fetching data from analyzer
        available formats: "ReIm" | "MagdB_Phase" | "Mag_Phase"
        not realized 
        """
        pass
    def set_display_state(self, display_state = "OFF"):
        self.write("SYSTEM:DISPLAY:UPDATE {}".format(display_state))
    def get_X_axis_values(self):
        return (np.fromstring(self.query("CALCulate1:DATA:STIMulus?"), sep = ','))
    def convert_data_to_format(self, data, data_format):
        converted_data = np.array()
        if data_format == "ReIm":
            pass
        if data_format == "dBMag_Phase":
            pass
        if data_format == "Mag_Phase":
            pass
        return (converted_data)
    def trig_meas(self):
        self.write("INIT1:IMM;*WAI")
    def set_meas_counts(self, meas_count):
        """
        set number of measurement at once run
        """
        self.write("SWEep:COUNt {}".format(meas_count))
    def get_meas_counts(self):
        return (self.query("SWEep:COUNt?"))
    
    def set_continuous_meas_mode(self, state = "OFF"):
        self.write("INITiate1:CONTinuous {}".format(state))
    def get_continuous_meas_mode(self):
        return (self.query("INITiate1:CONTinuous?"))
    def set_standard_config(self, parameters_dict):
        if (self.query("INSTrument?")) != "NWA":
            self.write("INSTrument NWA")
        self.set_timeout(10000)
        self.set_continuous_meas_mode("OFF")
        self.set_display_state("ON")
        self.clear_average()
        self.set_average_state("OFF")
        self.set_averages(1)
        self.set_parameters(parameters_dict)
    def set_byte_order(self, byte_order = "NORMal"):
        """
        NORMal - big endian (LSB)
        SWAPped - little endian (MSB)
        """
        self.write("FORMat:BORDer {}".format(byte_order))
    def get_byte_order(self):
        return (self.query("FROMat:BORDer?"))
    def set_data_format(self, data_format = "ASCii", real_length = 32):
        """
        ASCii | REAL
        REAL - float value 32 or 64 
        """
        if data_format == "REAL":
            self.write("FORMat {},{}".format(data_format, real_length))
        if data_format == "ASCii":
            self.write("FROMat {}".format(data_format))
    def get_data_format(self):
        return (self.query("FORMat?"))
    def set_if_filter_selectivity(self, if_speed = "FAST"):
        """
        FAST | NORMal
        """
        self.write("BANDwidth:SELect {}".format(if_speed))
    def get_if_filter_seceltivity(self):
        return (self.query("BANDwidth:SELect?"))
    def set_calibration(self, cal_state = "ON"):
        self.write("CORRection:FACTory {}".format(cal_state))
    def get_calibration_state(self):
        return (self.query("CORRection:FACTory?"))
    def set_autoscale(self):
        self.write("DISPlay:TRACE1:Y:AUTO ONCE")
    