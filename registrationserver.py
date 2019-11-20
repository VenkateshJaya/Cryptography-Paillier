import math
from paillier.paillier import *
import random
import os
import sys

class RegistrationServer:
    def __init__ (self):
        self.priv, self.pub = generate_keypair(1024)

    def register(self, DriverID, vserver):
        secret_key,public_key = generate_keypair(1024)
        AuthID = encrypt(self.pub,DriverID)
        Secret = encrypt(self.pub,secret_key)
        vserver.store(AuthID,Secret)

        return AuthID,Secret,pub
