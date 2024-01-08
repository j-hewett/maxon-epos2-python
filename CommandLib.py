from ctypes import *
import numpy as np

nodeID = 1
ErrorCode = c_uint()
DeviceErrorCode = c_uint()

def SetSpeed(epos,target_speed,keyHandle):
    epos.VCS_SetVelocityMust(keyHandle, nodeID, target_speed, byref(ErrorCode))
    
def GetObject(epos,ObjectIndex,keyHandle):

    ObjectSubIndex=0x00
    NbOfBytesToRead=0x04

    NbOfBytesRead=c_uint()
    pData=c_int()
    ErrorCode=c_uint()

    #Request 'object' data from motor controller
    ret = epos.CVS_GetObject(keyHandle, nodeID, ObjectIndex, ObjectSubIndex, byref(pData), NbOfBytesToRead, byref(NbOfBytesRead), byref(ErrorCode))

    if ret == 1:
        return pData.value
    else:
        print("Error getting value at object index: ",ObjectIndex)
        return 0
    

    