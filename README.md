# PowerSupplyControlInstek

The PowerSupplyControlInstek folder contains a console applications to remote control power supply INSTEK.

Please note:

## INSTEK

*	Make sure, that the INSTEK power supply device connected to your bench matches the configuration settings.
*	For "GWinstek GPD-2303S" check these settings on the following documentation, page 36: https://www.tme.eu/Document/d01836c0b53439b01d485be8e53686dd/GPD-3303+User+Manual+20080521.pdf
*	Settings are stored in PowerSupplyControlInstek\settings.cfg file
*	By default, these settings are:

		baud_rate = 115200 (despite that in the documentation is written 9600, this power supply works on 115200)
		stop_bits = 1
		byte_size = 8
		parity = N
		port = COM7 (please change in settings.cfg according to the used COM port)
		max_current = 3.0
		device = INSTEK

## Set State and Voltage of INSTEK power supply

* 	Example: 
		execute 'setVoltage.bat 1 --CH1Vlt 12 --CH2Vlt 24' via cmd or via powerOn.bat (open with notepad++ or other program to change voltage parameters), where '1' is for setting state ON, '--CH1Vlt 12' is for setting the voltage of channel 1 to 12, '--CH2Vlt 12' is for setting the voltage of channel 2 to 12. values can be changed. by default they are 0.0V;
		execute 'setVoltage.bat 0 via cmd or via powerOff.bat, where '0' is for setting state OFF.                                                           