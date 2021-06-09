import abc
import serial
import re
import time

class PowerSupplyControl(object):
    """
    Abstract class for controlling power supplies.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, port, baudrate, stopbits, bytesize, parity):
        #Establish serial connection to the power supply
        self.serialConnection = serial.Serial(port=port, baudrate=baudrate, stopbits=stopbits, 
                            bytesize=bytesize,timeout=0.5, parity=parity,rtscts=1);
        
    @abc.abstractmethod
    def setOnOff(self, devstate):
        """
        Sets the PS ON or OFF
        """      
        raise NotImplementedError('not implemented')
             
    @abc.abstractmethod   
    def setVoltage(self, voltage, channel):
        """
        Sets a certain voltage for certain channel. 
        """      
        raise NotImplementedError('not implemented')
    
    
    @abc.abstractmethod   
    def getVoltage(self, voltage, channel):
        """
        Returns the current voltage of a channel
        """
        raise NotImplementedError('not implemented')
        
    @abc.abstractmethod   
    def setMaxCurrent(self, current, channel):
        """
        Returns the current voltage of a channel
        """
        raise NotImplementedError('not implemented')
       
    
    def __del__(self):
        self.serialConnection.flush()
        self.serialConnection.close()
   
    
class PowerSupplyControlInstek(PowerSupplyControl):    
    """
    Class to remote control an Instek power supply.
    """
    def setOnOff(self, devstate):
        """
        Sets the PS ON(1) or OFF(0)
        """ 
        if devstate:
            self.serialConnection.write(str.encode('OUT1\n'))
            print('INSTEK PPS turned ON\n')
        else:
            self.serialConnection.write(str.encode('OUT0\n'))
            print('INSTEK PPS turned OFF\n')
    
    def setVoltage(self, voltage, channel):
        """
        Sets a certain voltage for certain channel. 
        """  
        try:
            #set voltage
            voltageCommand = 'VSET' + str(channel) + ':' + str(voltage) + '\n'
            self.serialConnection.write(str.encode(voltageCommand))
            print ('Voltage of channel ' + str(channel) + ' is set to ' + str(voltage))
        
        except Exception:
            raise Exception("Failed to set voltage of channel " + str(channel))
            
       
    def getVoltage(self, channel):
        """
        Returns the current voltage of a channel
        """
           
        #get voltage
        voltageCommand = 'VSET' + str(channel) + '?\n'
        self.serialConnection.write(str.encode(voltageCommand)) 
        #read response...will be something like "015.12\r\n"
        time.sleep(0.1)
        response = self.serialConnection.read(8) 
        
        try:
            return float(response)
        except Exception:
            raise Exception("Failed to get the current voltage") 
     
    def setMaxCurrent(self, current, channel):
        """
        Sets the maximum current for a channel
        """ 
        try:
            #set current
            currCommand = 'ISET' + str(channel) + ':' + str(current) + '\n'
            self.serialConnection.write(str.encode(currCommand))
            print("Current of channel " + str(channel) + ' is set to ' + str(current) + '\n')
        
        except Exception:
            raise Exception("Failed to set current of channel " + str(channel) + 'to ' + str(current))
		
        