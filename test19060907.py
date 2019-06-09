import numpy as np
import struct
import os
import copy

class MyBuffer:
    def __init__(self):
        pass
    def startService(self,dir1):
        self.fileNo=0
        self.dir1 = dir1
        self.fpIn =open(self.dir1+os.sep+"adc_data_Raw_{}.bin".format( self.fileNo  ),"rb")
        self.targetSize = 128*254*8*2
        self.totalBytes=0
        self.bufferSize=0
        self.buffer1 = np.zeros(  (128*254*16+int(1456/8/2*100)))
    def endService(self):
        self.fpIn.close()
    def getFrame(self):
        ret1 = None
        for i in range(1000):
            binData = self.fpIn.read(14)
            if len(binData)==0:
                self.fpIn.close()
                self.fileNo+=1
                if self.fileNo>=8:
                    ret1 = None
                    break
                print ( "fileNo",self.fileNo )
                self.fpIn =open(self.dir1+os.sep+"adc_data_Raw_{}.bin".format( self.fileNo  ),"rb")
                binData = self.fpIn.read(14)
                if len(binData)==0:
                    ret1 = None
                    print ("EOF")
                    break
            data1 = struct.unpack("<IIIH",binData)
            totalBytes1=data1[2]+(data1[3]<<32)
            if totalBytes1 !=self.totalBytes:
                for k in np.arange((totalBytes1 - self.totalBytes)/1456):
                    self.buffer1[int(self.bufferSize/2):int((self.bufferSize+1456)/2)] = 0
                    self.bufferSize+=1456
            binData = self.fpIn.read(1456)
            array1 = np.frombuffer(binData,"<i2")
            self.buffer1[int(self.bufferSize/2):int((self.bufferSize+1456)/2)] = array1
            self.bufferSize+=1456
            self.totalBytes=self.totalBytes+data1[1]
            if self.targetSize<=self.bufferSize:
                #ret1 = copy.deepcopy(self.buffer1[:int(self.targetSize/2)])
                ret1 = self.buffer1[:int(self.targetSize/2)].copy()
                self.buffer1[:int((self.bufferSize-self.targetSize)/2)] = self.buffer1[int(self.targetSize/2):int(self.bufferSize/2)]
                self.bufferSize-=self.targetSize
                break
        return ret1
            


#print ()

         
#"""
myBuffer = MyBuffer()
myBuffer.startService(r".")

#for i in range(13000):
for i in range(13000):
    if (i%200)==0:
        print (i)
    array1 = myBuffer.getFrame()
    
    for j in range(254):
        for k in range(128):
            idx1=(j*128+k)*8
            arr1 = array1[idx1:(idx1+8)]
            if arr1[0]!=k or arr1[4]!=-k:
                print (arr1)
            if arr1[1]!=j or arr1[4+1]!=-j:
                print (arr1)
            if arr1[2]!=i or arr1[4+2]!=-i:
                print (arr1)
    
        
#myBuffer.getFrame()
myBuffer.endService()
#"""

