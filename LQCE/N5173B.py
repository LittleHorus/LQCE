# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:37:29 2019

@author: Betretzen
"""

import LQCE.instr as instr



class N5173B_gen(instr.Instr):
    
    def __init__(self, visa_name):
        super(N5173B_gen,self).__init__(visa_name)
        self.cls()
        self._visainstrument.read_termination = '\n'
        self._visainstrument.timeout = 5000
    def set_frequency(self, freq, unit = 'Hz'):
        self.write("FREQuency:FIXed {}{}".format(freq, unit))
    def get_frequency(self):
        return (self.query(":FREQ:FIX?"))
    def get_freq(self):
        return(self.query(":FREQ:FIX?"))
    def set_freq_mode(self, freq_mode = ":FIXed"):
        """
        FIXed | CW | LIST
        """        
        self.write(":FREQ:MODE {}".format(freq_mode))
    def get_freq_mode(self):
        return (self.query(":FREQ:MODE?"))    
    def set_power(self, power):
        self.write(":POWer:LEVel {}dB".format(power))
    def get_power(self):
        return (self.query(":POWer:LEVel?"))
    def set_alc_state(self, alc_state = "ON"):
        self.write(":POWer:ALC {}".format(alc_state))
    def get_alc_state(self):
        return (self.query(":POWER:ALC?"))
    def set_output_state(self, output_state):
        self.write(":OUTPUT {}".format(output_state))
    def get_output_state(self):
        return (self.query(":OUTPUT?"))
    def set_modulation_state(self, mod_state):
        self.write(":OUTPut:MODulation {}".format(mod_state))
    def get_modulation_state(self):
        return (self.query(":OUTput:MOD?"))
    