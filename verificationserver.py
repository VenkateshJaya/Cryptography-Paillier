import math
from paillier.paillier import *

from registrationserver import RegistrationServer

class VerificationServer:
    """VerificationServer is used to verify if the user is a part of the network
    """

    def __init__(self):
        self.values = []
        pass

    def store(self,AuthID,Secret):
        self.values.append([AuthID,Secret])

    def verification(self,AuthID,Ej,Ei):
        flag = 0
        position = 0
        for i,j in self.values:
            if i==AuthID:
                flag = 1
                Rki = j
        if flag == 1:
            ri = decrypt(Rki,public_keyi,Ei[0])
            RIDj = decrypt(Rki,public_keyi,Ei[1])
            flag2 = 0
            for i,j in self.values:
                if i == RIDj:
                    flag2 = 1
                    Rkj = j
            if flag2 == 1:
                rj = decrypt(Rkj,public_keyj,Ej[0])
                RIDi = decrypt(Rkj,public_keyj,Ej[1])
            check = 0
            if RIDi == AuthID:
                check = 1

        if check == 1:
            sesskey = random.randint(1,1000)
            reti = [encrypt(public_keyi,sesskey),encrypt(public_keyi,ri)]
            retj = [encrypt(public_keyj,sesskey),encrypt(public_keyj,rj)]

            return reti,retj
