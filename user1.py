import math
from paillier.paillier import *
import random
import os
import sys
import time
import user2

start_time = time.time();
from registrationserver import RegistrationServer
from verificationserver import VerificationServer

int changetime = 5

if __name__ == '__main__':
    rserver = RegistrationServer()
    vserver = VerificationServer()

    seedv = random.randint(1,10)

    random.seed(seedv)
    driverID = random.randint(1,1000)

    AuthID,SecretKey,public_keyi = rserver.register(driverID,vserver)

    r = random.randint(1,100000)

    def verifyRID(self,RID):
        RIDother = RID
        user2.verifyRID(AuthID)
        Ej=[encrypt(public_key,r),encrypt(public_key,RIDj)]

    def exchange(self,[rother,RIDself]):
        Ei=[rother,RIDself]
        user2.exchange(Ej)

    reti,retj = vserver.verification(AuthID,Ei,Ej)

    user2.finalex(retj)

    rcheck = decrypt(SecretKey,public_keyi,reti[1])
    if rcheck == r:
        flag = 1

    if flag == 1:
        print("Communication Successfully Established with sesskey",decrypt(SecretKey,public_keyi,reti[0]))

    currtime = time.time()
    for i in ((currtime-start_time)/changetime):
        seed = 20
        AuthID = IDGenerator(AuthID,public_key,seed)
