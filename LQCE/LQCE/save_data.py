import os
from datetime import datetime
from time import gmtime, strftime, localtime



entries = os.listdir('C:\\Users\\Dmitry\\Google Диск (dimonchikgvd@gmail.com)')

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d-%b-%Y_')
    return formated_date

os.mkdir("D:\\Tempio\\Qubit0\\I-Tone")




time_part = strftime("%H-%M-%S", localtime())
date_part = strftime("%B-%d-%Y", localtime())
print("{}\\qubit_{}\\{}_{}".format(date_part, roman[qubitNumber], time_part, experiment_type))

rootFolder = '{}'.format(date_part)
qubitNumFolder = 'Qubit_{}'.format(roman[qubitNumber])

print('{}\\{}'.format(rootFolder, qubitNumFolder))



class dataPrepareToSave():
    def __init__(self):
        self.qubit_number = 1
        self.experiment_type = 'oneTone'
        self.chip_id = 'XMon-xxx'
        self.root_directory = 'D:\\Tempio\\'
        self.data_block = []
        
        
    def createNewInnerFolder(self):
        pass
        
    def createNewRootFolder(self):
        pass
        
    def getRootFolderName(self):
        return ('{}_{}'.format(self.qubit_id, strftime("%B-%d-%Y", localtime())))
        
    def getInternalFolderName(self, qubit_num = self.qubit_number):
        roman = {0: '0', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                    30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                    90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                    600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                    2000: 'MM', 3000: 'MMM'}
        return ('Qubit_{}'.format(roman[qubit_num]))
        
     def getMeasTypeFolderName(self, meas_type = self.experiment_type):
        return ('{}_{}'.format(strftime("%H-%M-%S", localtime()), meas_type))
    
    def oneToneDataPreparation(self, data, params, frequency_list, current_list):
        self.oneToneData_dict = {'chip_id':self.chip_id, 'parameters': params, 'nwa_frequency':frequency_list, 'current': current_list, 'data':data}
    
    def twoToneDataPreparation(self, data, params, frequency_list, current_list):
        self.twoToneData_dict = {'chip_id':self.chip_id, 'parameters': params, 'nwa_frequency':frequency_list, 'current': current_list, 'data':data}
    def acStarkDataPreparation(self, data, params, power_list, current_list):
        self.acStarkData_dict = {'chip_id':self.chip_id, 'parameters': params, 'power':power_list, 'current':current_list, 'data': data}
    
    def rabiDataPreparation(self, data, params):
        self.rabiData_dict = {'chip_id': self.chip_id, 'parameters': params, 'data': data}
    def ramseyDataPreparation(self, data, params):
        self.ramseyData_dict = {'chip_id': self.chip_id, 'parameters': params, 'data': data}
    def decayDataPreparation(self, data, params):
        self.decayData_dict = {'chip_id': self.chip_id, 'parameters': params, 'data': data}
    def echoDataPreparation(self, data, params):
        self.echoData_dict = {'ship_id': self.chip_id, ' parameters': params, 'data'; data}
        