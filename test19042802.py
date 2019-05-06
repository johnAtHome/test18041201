import struct


"""
fpIn = open("data.bin","rb")
for j in range(3):
    print ("###")
    print (j*(1456+14))
    print (fpIn.tell(),end=" ")
    data = fpIn.read(14)
    data =struct.unpack("<IIIH",data)
    print (data)
    print (fpIn.tell())
    data = np.fromfile(fpIn, dtype="<u2",count=int(dsize/2))
    #print (data.reshape)
    data = data.reshape(91,8).T
    #print (data)
fpIn.close()
"""
"""
fpIn = open("data.bin","rb")
for j in range(3):
    fpIn.seek(j*(1456+14))
    data = fpIn.read(14)
    data =struct.unpack("<IIIH",data)
    fpIn.seek(j*(1456+14)+14)
    data = np.fromfile(fpIn, dtype="<u2",count=int(dsize/2))
    data = data.reshape(91,8).T
    print (data)
fpIn.close()
"""


buffer1 = np.zeros((8,128*254+91*10))
fpIn = open("data.bin","rb")

frameNum=0
frameLen=200
frameLen=15
frameLen=128*254
packetLen = 91
#packetLen = 7
srcHeader=14
srcData=1456
data = np.zeros((8,frameLen))
baseSliceIdx = np.arange(packetLen)
for j in range(10):
    frameStart = j*frameLen
    frameEnd   = (j+1)*frameLen
    packetStart = int(frameStart/packetLen)
    packetEnd   = np.ceil(frameEnd/packetLen).astype(int)
    packetStartOffset =    frameStart%packetLen
    lcnt1=0
    buffer1[:,:]=0
    data[:,:]=0
    for i in range(packetStart,packetEnd,1):
        srcOffset=i*packetLen
        dstOffset=lcnt1*packetLen
        idx1=i*packetLen
        srcSliceIdx=baseSliceIdx
        fpIn.seek(i*(srcData+srcHeader)+srcHeader)
        a1 = np.fromfile(fpIn, dtype="<u2",count=int(dsize/2))
        a1 = a1.reshape(packetLen,8).T        
        dstSliceIdx=baseSliceIdx+dstOffset
        buffer1[:,dstSliceIdx]=a1[:,srcSliceIdx]
        lcnt1+=1
    #print (buffer1[packetStartOffset:packetStartOffset+frameLen])
    data[:,:] = buffer1[:,packetStartOffset:packetStartOffset+frameLen]
    print (data)
    print ("")

fpIn.close()

