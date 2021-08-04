from struct import unpack
import crypto

def choice(a, b):
    alternatives = [a,b]
    index = crypto.getrandbits(32)[0] & 0x01
    return alternatives[index]

def float_between(a, b):
    big = max(a,b)
    small = min(a,b)
    diff = big - small
    rand_num, scaler = unpack('I', crypto.getrandbits(32))[0], unpack('I', b'\xFF\xFF\xFF\xFF')[0]
    return small + rand_num*diff/scaler
