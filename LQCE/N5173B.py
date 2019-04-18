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
    def set_alc_state(self, alc_state = "OFF"):
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
    
    def set_trigger_external_source(self, source):
        """TRIGger1 | TRIGger2 | PULSe"""
        self.write(":TRIGger:EXTernal:SOURce {}".format(source))
    def set_trigger_internal_source(self, source):
        """PVIDeo | PSYNc"""
        self.write(":TRIGger:INTernal:SOURce {}".format(source))
    def set_trigger_out_polarity(self, trig_channel, polarity):
        """POS | NEG"""
        self.write(":TRIGger:OUTPut{}:POLarity {}".format(trig_channel, polarity))
    def set_trigger_in_polarity(self, polarity):
        """POSitive | NEGative"""
        self.write(":TRIGger:SLOPe {}".format(polarity))
    def set_trigger_source(self, source):
        """BUS | IMMediate | EXTernal | INTernal | KEY | TIMer | MANual"""
        self.write(":TRIGger:SOURce {}".format(source))
    def trigger_arm(self):
        """this event command causes an armed LIST of Step sweep to immediately start without the selected trigger occurring"""
        self.write(":TRIGger:IMMediate")
    
    def set_pulse_internal_step_delay(self, step):
        """in ns"""
        self.write(":PULM:INTernal:DELay:STEP {}".format(step))
    def set_pulse_internal_delay(self, delay):
        """"""
        self.write(":PULM:INTernal:DELay {}".format(delay))
    def set_pulse_internal_frequency(self, freq):
        """default frequency a 1MHz"""
        self.write(":PULM:INTernal:FREQuency {}".format(freq))
    def set_pulse_train_ontime(self, time):
        self.write(":PULM:INTernal:TRAin:ONTime {}".format(time))
    def set_pulse_train_offtime(self, time):
        self.write(":PULM:INTernal:TRAin:OFFTime {}".format(time))
    def set_pulse_train_repetition(self, counts):
        self.write(":PULM:INTernal:TRAin:REPetition {}".format(counts))
    def set_pulse_width(self, width):
        self.write(":PULM:INTernal:PWIDth {}".format(width))
    def set_pulse_train_trigger(self, trigger = "TRIGgered"):
        """FRUN | TRIGgered | GATEd"""
        self.write(":PULM:INTernal:TRAin:TRIGger {}".format(trigger))
    def trig_pulse_immediate(self):
        self.write(":PULM:INTernal:TRAin:TRIGger:IMMediate")
    def set_pulse_source(self, source = "INTernal | EXTernal"):
        """INTernal | EXTernal"""
        self.write(":PULM:SOURce {}".format(source))
    def set_pulse_mode(self, mode = "PTRain"):
        """SQUare | FRUN | TRIGgered | ADOublet | DOUBlet | GATEd | PTRain"""
        self.write(":PULM:SOURce:INTernal {}".format(mode))
    