from math import sqrt

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def detect(a):
    x = a.count(1)
    y = a.count(-1)
    z = a.count(0)
    if (x>35):
        return 1
    if (y>35):
        return -1
    else:
        return 0

x = open("FIFOSamples.csv")

binSize = 1000 #100 bins per second
mrbin = 0
curBinCount = 0
bins = []

avLen = 50
movingAv = []
curAv = 0
highDiffs = [0.025]*4
lowDiffs = [-0.025]*4 #0.1

segments = []

detected = []

recv = False
cntr = 0

dBits = False
dSegments = False
dDiffs = False

curCount = 0
nextTrans = None
for line in x:
    I,Q = map(int,line.split(","))
    
    amp=sqrt(I**2+Q**2)
    
    if (curBinCount==binSize):
        bins.append(mrbin/float(binSize))
        curBinCount = 0
        #print '|'*int(mrbin/5000)
        #print mrbin/binSize
        curAv+=mrbin/binSize
        if(len(bins)>avLen):
            curAv-=bins[-avLen]
            movingAv.append(curAv/avLen)
            #print curAv/avLen
            
            if (len(movingAv)>1):
                diff = movingAv[-1]-movingAv[-2]
                if dDiffs: print diff
                threshHigh = sum(highDiffs[-4:])/8
                threshLow = sum(lowDiffs[-4:])/8
                
                if (diff>threshHigh):
                    segments.append(1)
                    highDiffs.append(diff)
                elif (diff<threshLow):
                    segments.append(-1)
                    lowDiffs.append(diff)
                else:
                    segments.append(0)
                    #it's in the middle - a hold
                if (len(segments)>50):
                    if (segments[-35:-5].count(1)>25): #about 80%
                        if (segments[-5]==1):
                            if (segments[-4:].count(1)==0):
                                nextTrans = curCount+47
                                if dSegments: print "Clock-resync"
#[30 80% ones-with-the-last-one-a-1,5-non-ones,]
                    if (segments[-35:-5].count(-1)>25): #about 80%
                        if (segments[-5]==-1):
                            if (segments[-4:].count(-1)==0):
                                nextTrans = curCount+47
                                if dSegments: print "Clock-resync"
                                        
                    if (curCount==nextTrans):
                        a =  detect(segments[-50:])
                        if (a==0):
                            if (len(detected)>0):
                                detected.append(detected[-1])
                            else:
                                detected.append(0)
                        elif (a==1):
                            detected.append(1)
                        elif (a==-1):
                            detected.append(0)
                        if dBits: print detected[-1]
                        cntr+=1
                        
                        if (recv==False):
                            if (detected[-4:]==[1,0,0,1]):
                                recv = True
                                print "Heard start bits"
                                cntr = 0
                        else:
                            #print detected[-1]
                            if (detected[-8:]==[1,1,1,1,1,1,1,1]):
                                recv = False
                                print "Ending"
                                cntr = 0
                            elif cntr == 8:
                                cntr = 0
                                s = frombits(detected[-8:])
                                print s


                        #print curCount
                        if dSegments: print "Resetting Count"
                        nextTrans+=50
                curCount+=1
                if dSegments: print segments[-1]
                
        mrbin = 0

    mrbin+=amp
    curBinCount+=1
        
        
##DETECT 0101
