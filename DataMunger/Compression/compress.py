import bz2
import zlib
import gzip
import lzma
import zipfile

import os
import sys


# Compression functions.


def to_bz2(input, output):
    with open(input, mode='rb') as fin:
        data = fin.read()
        
    with bz2.open(output, 'wb') as fout:
        fout.write(data)
    

def to_gz(input, output):
    with open(input, mode='rb') as fin:
        data = fin.read()
        compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
       
    with open(output, mode='wb') as fout:
        fout.write(compressed_data)

def to_lzma(input, output):
    with open(input, mode='rb') as fin:
        data = fin.read()

    with lzma.LZMAFile(output, mode='wb') as fout:
        fout.write(data)
    
def to_gzip(input, output):
    with open(input, mode='rb') as fin:
        data = fin.read()
        
    with gzip.open(output, 'wb') as fout:
        fout.write(data)



# Undoes compression.



def un_bz2(input, output):
    with bz2.open(input, "rb") as fin:
        data = fin.read()

    with open(output, mode='wb') as fout:
        fout.write(data)

def un_gz(input, output):
    with open(input, mode='rb') as fin:
        data = fin.read()
        decompressed_data = zlib.decompress(data)
    
    with open(output, mode='wb') as fout:
        fout.write(decompressed_data)

def un_lzma(input, output):
    with lzma.LZMAFile(input, mode='rb') as fin:
        decompressed_data = fin.read()    
    with open(output, mode='wb') as fout:
        fout.write(decompressed_data)

def un_gzip(input, output):
    with gzip.open(input, mode='rb') as fin:
        fin.seek(0)
        decompressed_data = fin.read()    
    with open(output, mode='wb') as fout:
        fout.write(decompressed_data)

