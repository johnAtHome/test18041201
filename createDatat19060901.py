import numpy as np
import struct


def createGenerator():
    for n in range(200000):
        for i in range(254):
            for j in range(128):
                data1 = struct.pack("<8h",j,i,n,0,-j,-i,-n,0)
                yield data1

generator1 = createGenerator()


mask1=(1<<32)-1
totalValue=0
packetNum=0
for j in range(8):
    print(j)
    fpOut1 = open("adc_data_Raw_{}.bin".format(j),"wb")
    for i in range(730456):
        binData = struct.pack("<II",packetNum,1456)
        fpOut1.write(binData)
        binData = struct.pack("<IH",  totalValue&mask1 , totalValue>>32 )
        fpOut1.write(binData)
        
        for k in range(91):       
            binData = next(generator1)
            fpOut1.write(binData)
        packetNum+=1
        totalValue=totalValue+1456
    fpOut1.close()



