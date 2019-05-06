import struct


fpOut = open("data.bin","wb")

seq=0
dsize=1456
totalSize=0
num=0
mask=(1<<32)-1
for j in range(100000):
    fpOut.write( struct.pack("<IIIH",seq,dsize,totalSize&mask,totalSize>>32 ))
    #print (fpOut.tell())
    for i in range(91):
        for k in range(8):
            fpOut.write(struct.pack("<H",num&0xffff))
        num+=1
    totalSize=num*2*8
    seq+=1
    


fpOut.close()


"""
fpIn = open("data.bin","rb")
for j in range(3):
    data = fpIn.read(14)
    data =struct.unpack("<IIIH",data)
    print (data)

    if 0:
        for i in range(int(dsize/16)):
            data = fpIn.read(16)
            data = struct.unpack("<HHHHHHHH",data)
            print (data)
    
    data = np.fromfile(fpIn, dtype="<u2",count=int(dsize/2))
    #print (data.reshape)
    data = data.reshape(91,8).T
    print (data)
fpIn.close()
"""

