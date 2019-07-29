# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:37:16 2019

@author: Dmitry
"""

import LQCE.instr as instr

class K2636B(instr.Instr):
    
    def __init__(self, visa_name):
        super(K2636B,self).__init__(visa_name)
        self.cls()
        self._visainstrument.read_termination = '\n'
        self._visainstrument.timeout = 5000
        self._channel_a_mode = 0 #current mode
        self._channel_b_mode = 0 #current mode
        
    def _get_voltage_compliance(self, channel = "a"):
        return self.query("smu{}.source.compliance".format(channel))
    
    def _set_current_mode(self, channel = "a"):
        self.write("smu{}.source.func = 0".format(channel))
    def _set_voltage_mode(self, channel = "a"):
        self.write("smu{}.source.func = 1".format(channel))
    def _get_source_mode(self, channel = "a"):
        return self.query("smu{}.source.func".format(channel))
    def _set_highc_mode(self, channel = "a", highc_state = 0):
        self.write("smu{}.source.highc = {}".format(channel, highc_state))
    def _set_current_level(self, channel = "a", level = 0):
        self.write("smu{}.source.leveli = {}".format(channel, level))
    def _get_current_level(self, channel = "a"):
        return self.query("smu{}.measure.i()".format(channel))
    def _set_voltage_level(self, channel = "a", level = 0):
        self.write("smu{}.source.levelv = {}".format(channel, level))
    def _get_voltage_level(self, channel = "a"):
        return self.query("smu{}.measure.v()".format(channel))
    def _set_output_state(self, channel = "a", state = 0):
        self.write("smu{}.source.output = {}".format(channel, state))
    def _get_output_state(self, channel = "a"):
        return self.query("smu{}.source.output".format(channel))
    def _set_current_range(self, channel = "a", crange = "1e-3"):
        self.write("smu{}.source.rangei = {}".format(channel, crange))
    def _get_current_range(self, channel = "a"):
        return self.query("smu{}.source.rangei".format(channel))
    def _set_voltage_range(self, channel = "a", vrange = 1):
        self.write("smu{}.source.rangev = {}".format(channel, vrange))
    def _get_voltage_range(self, channel = "a"):
        return self.query("smu{}.source.rangev".format(channel))
    