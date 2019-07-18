# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:01:21 2019

@author: Dmitry
"""
import serial
from ctypes import (Union, Array, c_uint8, c_float, cdll, CDLL)
from enum import Enum
import crcmod


class uint8_array(Array):
    _type_ = c_uint8
    _length_ = 4
class f_type(Union):
    _fields_ = ("float", c_float), ("char", uint8_array)


class Nsk_current_source(object):

    def __init__(self, com_name):
        self.com_name = com_name
        self.session_open = 0
        self.serial_device = serial.Serial()
        self.serial_device.port = com_name
        self.serial_device.baudrate = 115200
        self.serial_device.timeout = 5
        
        '''
        try:
            self.serial_device = serial.Serial(port = com_name, baudrate = 115200, timeout = 5)
            self.session_open = 1
        except  serial.SerialException:
                print("COM port already initialize")
                
        ''' 
        self.datain_buf = []
        self.dataout_buf = []
        self.active_channel = 1
        

    def close(self):
        self.serial_device.close()
        self.session_open = 0
    def open(self):
        if self.session_open == 0:
            try:
                self.serial_device.open()
                self.session_open = 1
            except serial.SerialException:
                print("com port not open")
        else:
            print("device already initialize")
    def write(self, data_bytearray):
        self.serial_device.write(data_bytearray)
    def read(self, bytes_num):
        return (self.serial_device.read(bytes_num))
		
    def crc8(self, data_in):
        """
        this function evaluate crc
        poly: 0x0131
        
        """
        crc8_func = crcmod.mkCrcFun(0x131, initCrc=0x00, xorOut=0x00)
        return (crc8_func(bytearray(data_in)))
    
    def formated_data(self, data_in):
        temp_data = data_in 
        temp_data.append(self.crc8(data_in))
        return (bytearray(temp_data))
    def enable_channel(self, ch_num = 1):
        temp_cmd = [0]*9
        temp_cmd[0] = 0xC1
        temp_cmd[1] = 0xA0 | ch_num
        temp_cmd[2] = 0xA0
        temp_cmd[3] = 0xA0
        temp_cmd[4] = 0xA0
        temp_cmd[5] = 0xA0
        temp_cmd[6] = 0xA0
        temp_cmd[ch_num+1] = 0xA1
        temp_cmd[7] = 0xA0
        temp_cmd[8] = 0xA0
        ftemp = []
        ftemp = self.formated_data(temp_cmd)
        self.write(ftemp)
        return (self.read(10))
    
    def disable_channel(self, ch_num = 1):
        temp_cmd = [0]*9
        temp_cmd[0] = 0xC1
        temp_cmd[1] = 0xA0 | ch_num
        temp_cmd[2] = 0xA0
        temp_cmd[3] = 0xA0
        temp_cmd[4] = 0xA0
        temp_cmd[5] = 0xA0
        temp_cmd[6] = 0xA0
        temp_cmd[ch_num+1] = 0xA0
        temp_cmd[7] = 0xA0
        temp_cmd[8] = 0xA0
        ftemp = []
        ftemp = self.formated_data(temp_cmd)
        self.write(ftemp)
        return(self.read(10))  
    def set_channel_state(self, ch_num, state):
        """control supply delivery of the analog channel"""
        temp_cmd = [0]*9
        temp_cmd[0] = 0xC1
        temp_cmd[1] = 0xA0 | ch_num
        temp_cmd[2] = 0xA0
        temp_cmd[3] = 0xA0
        temp_cmd[4] = 0xA0
        temp_cmd[5] = 0xA0
        temp_cmd[6] = 0xA0
        if state == 0:
            temp_cmd[ch_num+1] = 0xA0
        if state == 1:    
            temp_cmd[ch_num+1] = 0xA1
        temp_cmd[7] = 0xA0
        temp_cmd[8] = 0xA0
        ftemp = []
        ftemp = self.formated_data(temp_cmd)
        self.write(ftemp)
        return (self.read(10))        
    def set_range(self, ch_num = 1, range_value = '1uA'):
        temp_cmd = [0]*9
        temp_cmd[0] = 0xC1
        temp_cmd[1] = 0x60 | ch_num
        temp_cmd[2] = 0x60
        temp_cmd[3] = 0x60
        temp_cmd[4] = 0x60
        temp_cmd[5] = 0x60
        temp_cmd[6] = 0x60
        if range_value == '1uA':
            temp_cmd[ch_num+1] = 0x60
        if range_value == '10uA':
            temp_cmd[ch_num+1] = 0x61
        if range_value == '100uA':
            temp_cmd[ch_num+1] = 0x62
        if range_value == '1mA':
            temp_cmd[ch_num+1] = 0x63
        if range_value == '10mA':
            temp_cmd[ch_num+1] = 0x64
        if range_value == '100mA':
            temp_cmd[ch_num+1] = 0x65
        temp_cmd[7] = 0x60
        temp_cmd[8] = 0x60
        ftemp = []
        ftemp = self.formated_data(temp_cmd)
        self.write(ftemp)
        return(self.read(10))
    def set_out_mode(self, ch_num = 1, out_mode = 'INNER_LO_OUTER_LO'):
        """
        set relay configuration
        available regimes:
        INNER_LO_OUTER_LO | INNER_LO_OUTER_GND | INNER_LOGND_OUTER_LOGND | 
        INNER_GUARD_OUTER_LO | INNER_GUARD_OUTER_LOGND | INNER_LO_OUTER_NC |
        INNER_NC_OUTER_LO
        """
        temp_cmd = [0]*9
        temp_cmd[0] = 0xC1
        temp_cmd[1] = 0x30 | ch_num
        temp_cmd[2] = 0x30
        temp_cmd[3] = 0x30
        temp_cmd[4] = 0x30
        temp_cmd[5] = 0x30
        temp_cmd[6] = 0x30
        if out_mode == 'INNER_LO_OUTER_LO':
            temp_cmd[ch_num+1] = 0x31
        if out_mode == 'INNER_LO_OUTER_GND':
            temp_cmd[ch_num+1] = 0x32
        if out_mode == 'INNER_LOGND_OUTER_LOGND':
            temp_cmd[ch_num+1] = 0x33
        if out_mode == 'INNER_GUARD_OUTER_LO':
            temp_cmd[ch_num+1] = 0x34
        if out_mode == 'INNER_GUARD_OUTER_LOGND':
            temp_cmd[ch_num+1] = 0x35
        if out_mode == 'INNER_LO_OUTER_NC':
            temp_cmd[ch_num+1] = 0x36
        if out_mode == 'INNER_NC_OUTER_LO':
            temp_cmd[ch_num+1] = 0x37
        temp_cmd[7] = 0x30
        temp_cmd[8] = 0x30
        ftemp = []
        ftemp = self.formated_data(temp_cmd)
        self.write(ftemp)
        return(self.read(10))
    def set_voltage_compliance(self, ch_num = 1, voltage_compliance_value = 10):
        """ no hardware support"""
        pass
    def get_voltage_compliance(self):
        temp_cmd = [0xC1, 0xB0, 0xBF, 0xBF, 0xBF, 0xBF, 0xBF, 0xBF, 0xBF]
        self.write(self.formated_data(temp_cmd))
        temp_list = []
        temp_list = list(self.read(10))
        return([temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6]])
    def set_output_state(self, ch_num = 1, state = 0):
        temp_cmd = [0]*9
        temp_cmd[0] = 0xC1
        temp_cmd[1] = 0x70 | ch_num
        temp_cmd[2] = 0x70
        temp_cmd[3] = 0x70
        temp_cmd[4] = 0x70
        temp_cmd[5] = 0x70
        temp_cmd[6] = 0x70
        if state == 0:
            temp_cmd[ch_num+1] = 0x70
        if state == 1:
            temp_cmd[ch_num+1] = 0x71
        temp_cmd[7] = 0x70
        temp_cmd[8] = 0x70
        ftemp = []
        ftemp = self.formated_data(temp_cmd)
        self.write(ftemp)
        return (self.read(10))
    def get_output_state(self, ch_num):
        """no realized, need fix mcu programm to implement """
        pass
    def float_to4bytes(self, float_data):
        temp_data = f_type()
        temp_data.float = float_data
        return temp_data.char[:]
    def byteArray_toFloat(self, data_array, offset = 0):
        temp_data = f_type()
        temp_data.char[:] = (data_array[0+offset],data_array[1+offset],data_array[2+offset],data_array[3+offset])
        return temp_data.float
        
    def set_current(self, ch_num = 1, current_value = 0.0):
        temp_float_as_4bytes = []*4
        temp_float_as_4bytes = self.float_to4bytes(current_value)
        temp_cmd = [0]*9
        temp_cmd[0] = 0xC1
        temp_cmd[1] = 0xD0 | ch_num
        temp_cmd[2] = temp_float_as_4bytes[0]
        temp_cmd[3] = temp_float_as_4bytes[1]
        temp_cmd[4] = temp_float_as_4bytes[2]
        temp_cmd[5] = temp_float_as_4bytes[3]
        temp_cmd[6] = 0xD0
        temp_cmd[7] = 0xD0
        temp_cmd[8] = 0xD0
        ftemp = []
        ftemp = self.formated_data(temp_cmd)
        self.write(ftemp)
        return (self.read(10))
    def set_active_channel(self, ch_num):
        self.active_channel = ch_num
    