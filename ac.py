import ac_issuer
import ac_prover
import ac_verifier
import time
import os
import psutil



def main():
    start_time = time.time()
    print('Test protocol')
    issuer = ac_issuer.Issuer
    issuer.genKeyPair(issuer,['Name', 'Driver ID', 'Age'])
    print('IPK :')
    ipk = issuer.getIssuerPublicKey(issuer)
    print(ipk)
       
    prover = ac_prover.Prover(['UserName1', 319872389, 21])
    nonce = issuer.getNonce()
    Request = prover.genCredRequest(ipk, nonce)
    print('REQUEST : ')
    print (Request)
    
    Credential = issuer.genCredential(issuer, Request)
    if Credential:
        if prover.setCredential (Credential):
            print('CREDENTIAL issued to the user:')
            print(Credential)
        else: print ('Error sig')    
    else:
        print('Error gen credential')
    print("\n Time taken for registration--- %s seconds --- \n" % (time.time() - start_time))
    start_time = time.time()
    Predicate = (0,1,0)
    print('Predicat for ', ipk.AttributeNames, ' : ', Predicate)
    
    DI, Proof = prover.genProof(Predicate)   
    print('PROOF: ', Proof )
    print('DI', DI)

    
    verifier = ac_verifier.Verifier
    print('VERIFY Proof = ', verifier.verifyProof(DI, Proof, ipk))

    print("\n Time taken for authentication--- %s seconds --- \n" % (time.time() - start_time))

   
    process = psutil.Process(os.getpid())
    print("--- No of bytes used ---")
    print(process.memory_info().rss)  # in bytes 


if __name__ == "__main__":
    main()
    
