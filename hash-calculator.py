# !/usr/bin/env python
# ==============================================================================
# Title:           hash-calculator.py
# Version:         1.0
# Author:          it-joe (https://github.com/it-joe)
# DateCreated:     10/7/2016
# DateUpdated:     
# Python Version:  2.7.12+
# ==============================================================================

import hashlib
import optparse
import os


SIZE = 65536

def compare(expectedHash, calculatedHash):
    print('\n')
    print(calculatedHash.upper(), ' = Calculated Hash')
    print(expectedHash.upper(), ' = Expected Hash')
    if expectedHash.upper() == calculatedHash.upper():
        print('\nResult: MATCH!')
    else:
        print('\nResult: NO MATCH!', )

		
def md5(file, expectedHash):
    hasher = hashlib.md5()
    with open(file, 'rb') as checkFile:
        buffer = checkFile.read(SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = checkFile.read(SIZE)
    calculatedHash = hasher.hexdigest()
    compare(expectedHash, calculatedHash)

	
def sha1(file, expectedHash):
    hasher = hashlib.sha1()
    with open(file, 'rb') as checkFile:
        buffer = checkFile.read(SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = checkFile.read(SIZE)
    calculatedHash = hasher.hexdigest()
    compare(expectedHash, calculatedHash)

	
def sha224(file, expectedHash):
    hasher = hashlib.sha224()
    with open(file, 'rb') as checkFile:
        buffer = checkFile.read(SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = checkFile.read(SIZE)
    calculatedHash = hasher.hexdigest()
    compare(expectedHash, calculatedHash)

	
def sha256(file, expectedHash):
    hasher = hashlib.sha256()
    with open(file, 'rb') as checkFile:
        buffer = checkFile.read(SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = checkFile.read(SIZE)
    calculatedHash = hasher.hexdigest()
    compare(expectedHash, calculatedHash)

	
def sha384(file, expectedHash):
    hasher = hashlib.sha384()
    with open(file, 'rb') as checkFile:
        buffer = checkFile.read(SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = checkFile.read(SIZE)
    calculatedHash = hasher.hexdigest()
    compare(expectedHash, calculatedHash)

	
def sha512(file, expectedHash):
    hasher = hashlib.sha512()
    with open(file, 'rb') as checkFile:
        buffer = checkFile.read(SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = checkFile.read(SIZE)
    calculatedHash = hasher.hexdigest()
    compare(expectedHash, calculatedHash)

	
def main():
    parser = optparse.OptionParser('[Usage] -a <algorithm> -f <file> -e <expected hash>')
    parser.add_option('-a', dest='algorithm', type='string', help='specify algorithm')
    parser.add_option('-f', dest='file', type='string', help='specify file')
    parser.add_option('-e', dest='hash', type='string', help='specify expected hash')
    
    (options, args) = parser.parse_args()
    algorithm = options.algorithm
    file = options.file
    expectedHash = options.hash

    if algorithm == None or file == None or expectedHash == None:
        print (parser.usage)
        exit(0)

    if not (os.path.isfile(file)):
        print('Error: %s file not found' % file)
        exit(0)

    if algorithm == 'md5':
        md5(file, expectedHash)
    elif algorithm == 'sha1':
        sha1(file, expectedHash)
    elif algorithm == 'sha224':
        sha224(file, expectedHash)
    elif algorithm == 'sha384':
        sha384(file, expectedHash)
    elif algorithm == 'sha256':
        sha256(file, expectedHash)
    elif algorithm == 'sha512':
        sha512(file, expectedHash) 
    else:
        print('Error: No supported algorithm found!')    

		
if __name__ == '__main__':
    main()