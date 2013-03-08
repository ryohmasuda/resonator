import labrad
import numpy
import time
import voltage_conversion
import csv
VC=voltage_conversion()

cxn = labrad.connect()
kdmm = cxn.Keithley_2100_DMM()

t=time.strftime("%H%M")
while(1):
    filename='c:/data_resonator_voltage/keithley_DMM_'+time.strftime("%d%m%Y_%H%M")+'.csv'
    fcsv=csv.writer(file(filename,"w"),lineterminator="\n")
    v=kdmm.getdcVolts()
    tempK=VC.converter(v)
    fcsv.writerow([t,v,temp])
    

    #time.sleep(60)
    
