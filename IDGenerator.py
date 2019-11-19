import math
from paillier.paillier import *

class IDGenerator:
    def __init__(self, authID, public_key, s):
        self.authID = authID
        self.pubkey = public_key
        random.seed(s)
        y = random.randint(1,1000)
        cy = encrypt(pubkey, y)
        newID = e_add(pubkey, authID, cy)
        return newID
    
