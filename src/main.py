import power_supply_controller
import ConfigParser
import sys
import argparse
import os 
from os.path import expanduser

if __name__ == '__main__': 
    
    try: 
        CH1Vlt = 0.0
        CH2Vlt = 0.0
        
        #get settings.cfg file path
        cfgPath = os.path.abspath(os.getcwd())
        settingsFilePath = cfgPath + "\settings.cfg"
        
        #read default settings from settings.cfg
        config = ConfigParser.ConfigParser()
        config.read(settingsFilePath)
        baudRate = int(config.get('Settings','baud_rate'))
        stopBits = int(config.get('Settings','stop_bits'))
        byteSize = int(config.get('Settings','byte_size'))
        parity = config.get('Settings', 'parity')
        port = config.get('Settings', 'port')
        maxCurrent = float(config.get('Settings', 'max_current'))
        device = config.get('Settings', 'device')
        
        
        #overwrite settings in case they are given on the console as well
        commandLineParser = argparse.ArgumentParser(description= 'Allows to remote control an INSTEK power supply. Use setVoltage.bat 1 --CH1Vlt 12 --CH2Vlt 12 e.g. to set the first and second channel' +
                                                                ' of an INSTEK power control to 12V. Default values for the other optional arguments are located in the ' + 
                                                                'settings.cfg file.')  
        commandLineParser.add_argument('devstate', action="store", type=int)                                                                    
        commandLineParser.add_argument('--CH1Vlt', action="store", dest= "CH1Vlt", default = CH1Vlt, type=float)
        commandLineParser.add_argument('--CH2Vlt', action="store", dest= "CH2Vlt", default = CH2Vlt, type=float)
        commandLineParser.add_argument('--baudrate', action="store", dest= "baudRate", default = baudRate, type=int)
        commandLineParser.add_argument('--stopbits', action="store", dest= "stopBits", default = stopBits, type=int)
        commandLineParser.add_argument('--bytesize', action="store", dest= "byteSize", default = byteSize, type=int)
        commandLineParser.add_argument('--parity', action="store", dest= "parity", default = parity)
        commandLineParser.add_argument('--port', action="store", dest= "port", default = port)
        commandLineParser.add_argument('--maxcurrent', action="store", dest= "maxCurrent", default = maxCurrent)
        commandLineParser.add_argument('--device', action="store", dest= "device", default = device)
        arguments = commandLineParser.parse_args()
  
        CH1Vlt = arguments.CH1Vlt
        CH2Vlt = arguments.CH2Vlt
        baudRate = arguments.baudRate
        stopBits = arguments.stopBits
        byteSize = arguments.byteSize
        parity = arguments.parity
        port = arguments.port
        maxCurrent = arguments.maxCurrent
        device = arguments.device
        
        print('device used: ' + device)
        print('baudRate: ' + str(baudRate))
        print('stopBits: ' + str(stopBits))
        print('byteSize: ' + str(byteSize))
        print('parity: ' + str(parity))
        print('port: ' + str(port))
        print('maxCurrent: ' + str(maxCurrent) + '\n')
        
        channelSetVoltage = [CH1Vlt, CH2Vlt]
            
        #set INSTEK power supply ON or OFF
        powerSupply = power_supply_controller.PowerSupplyControlInstek(port, baudRate, stopBits, byteSize, parity)
        powerSupply.setOnOff(bool(arguments.devstate))
            
        if bool(arguments.devstate):
            channel = 1
            for voltage in channelSetVoltage:
                #set desired voltage of INSTEK power supply
                powerSupply.setVoltage(voltage, channel)
            
                #ensure in addition that current can flow
                powerSupply.setMaxCurrent(maxCurrent, channel)
                channel += 1
            

    except Exception as e:
        print(e)
        sys.exit(2)
    


    
    

    
    
    


    
