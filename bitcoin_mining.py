from hashlib import sha256
import time

NOUNCE_VALUE = 10000000000

def SHA256(block):

    sha_code = sha256(block.encode('ascii'))
    result = sha_code.hexdigest()
    return result


def mining(block_no,trans,pre_hash,difficulty):
    pre_zeros = '0'*difficulty
    nounce = 1
    while True:
        block = str(block_no) + trans + pre_hash + str(nounce)
        new_hash = SHA256(block)
        nounce +=1
        if new_hash.startswith(pre_zeros):
            print(f"You have Successfully Mined !! and the Nounce Value is {nounce}")
            return new_hash
        if nounce == NOUNCE_VALUE:
            raise BaseException(f"Done with Minning after trying for {NOUNCE_VALUE} times..")
            break


if __name__ =='__main__':

    block = 10
    transaction = '''
    ABCD->EFGH->30,
    IJKL->MNOP->25,
    QRST->UVWX->40
    '''
    previous_hash = sha256('Akhilesh'.encode('ascii')).hexdigest()
    diff = 6
    print("Get yourself Ready for Mining...")
    start_time = time.time()
    new_hash = mining(block,transaction,previous_hash,diff)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Time taken for mining is {total_time} seconds..")
    print(f"Hash Value : {new_hash}")
