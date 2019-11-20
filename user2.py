import math
from paillier.paillier import *
import random
import os
import sys
import time
import user1

start_time = time.time();
from registrationserver import RegistrationServer
from verificationserver import VerificationServer

def __init__(self):
    rserver = RegistrationServer()
    vserver = VerificationServer()

    seedv = random.randint(1,10)

    random.seed(seedv)
    driverID = random.randint(1,1000)

    AuthID,SecretKey,public_keyj = rserver.register(driverID,vserver)

    RandomNumber = random.randint(1,100000)

    def verifyRID(self,RID):
        RIDother = RID
        user2.verifyRID(AuthID)
        Ej=[encrypt(public_key,r),encrypt(public_key,RIDj)]

    def exchange(self,[rother,RIDself]):
        Ei=[rother,RIDself]
        user2.exchange(Ej)

    flag = 0
    def finalex(retj):
        rcheck = decrypt(SecretKey,public_keyj,retj[1])
        if rcheck == RandomNumber:
            flag = 1

    if flag = 1:
        print("Communication Successfully Established with session key",decrypt(SecretKey,public_keyj,retj[0]))

    currtime = time.time()
    for i in ((currtime-start_time)/changetime):
        seed = 20
        AuthID = IDGenerator(AuthID,public_key,seed)
