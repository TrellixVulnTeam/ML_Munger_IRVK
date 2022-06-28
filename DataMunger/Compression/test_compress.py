from cProfile import run
import compress
import os
import numpy as np
import random 
import string

import unittest


# Test helper methods.

def fill_a_file(filename, size):
    # Clear the file.
    with open(filename, mode = 'wb') as fout:
        fout.write(b'')

    # Fill with random data.
    with open(filename, 'a') as fout:
        text = random.choices(string.ascii_lowercase, k = size)
        fout.write(str(text))


def run_method(method, input, output):
    if output is None:
        output = input
    method(input, output)




class TestCompress(unittest.TestCase):
    def test_to_gz(self):
        input_filename = "./TestFiles/test_data.txt"
        output_filename = "./TestFiles/test_data.gz"

        # Fill with random input.
        fill_a_file(input_filename, 20000)

        input_size = os.path.getsize(input_filename)

        test_method = compress.to_gz
        run_method(test_method, input_filename, output_filename)
        
        output_size = os.path.getsize(output_filename)

        self.assertGreater(input_size, output_size)

    def test_un_gz(self):
        input_filename = "./TestFiles/test_data.txt"
        compressed_filename = "./TestFiles/test_data.gz"
        uncompressed_filename = "./TestFiles/uncompressed_gz.txt"

        # Fill with random input.
        fill_a_file(input_filename, 20000)
        input_size = os.path.getsize(input_filename)
        print("input_size: ", input_size)
        # Compress the file using gz. 
        compress.to_gz(input_filename, compressed_filename)

        compressed_size = os.path.getsize(compressed_filename)
        print("compressed size: ", compressed_size)
        method = compress.un_gz
        run_method(method, compressed_filename, uncompressed_filename)
        
        decompressed_size = os.path.getsize(uncompressed_filename)
        print("decompressed size: ", decompressed_size)
        self.assertGreater(decompressed_size, compressed_size)

    
    def test_to_bz2(self):
        input_filename = "./TestFiles/test_data.txt"
        output_filename = "./TestFiles/test_data.gz"

        # Fill with random input.
        fill_a_file(input_filename, 20000)

        input_size = os.path.getsize(input_filename)

        test_method = compress.to_bz2
        run_method(test_method, input_filename, output_filename)
        
        output_size = os.path.getsize(output_filename)

        self.assertGreater(input_size, output_size)

    def test_un_bz2(self):
        input_filename = "./TestFiles/test_data.txt"
        compressed_filename = "./TestFiles/test_data.bz2"
        uncompressed_filename = "./TestFiles/uncompressed_bz2.txt"

        # Fill with random input.
        fill_a_file(input_filename, 20000)
        input_size = os.path.getsize(input_filename)
        print("input_size: ", input_size)
        # Compress the file using gz. 
        compress.to_bz2(input_filename, compressed_filename)

        compressed_size = os.path.getsize(compressed_filename)
        print("compressed size: ", compressed_size)
        method = compress.un_bz2
        run_method(method, compressed_filename, uncompressed_filename)
        
        decompressed_size = os.path.getsize(uncompressed_filename)
        print("decompressed size: ", decompressed_size)
        self.assertGreater(decompressed_size, compressed_size)

    def test_to_lzma(self):
        input_filename = "./TestFiles/test_data.txt"
        output_filename = "./TestFiles/test_data.xz"

        # Fill with random input.
        fill_a_file(input_filename, 20000)

        input_size = os.path.getsize(input_filename)

        test_method = compress.to_lzma
        run_method(test_method, input_filename, output_filename)
        
        output_size = os.path.getsize(output_filename)

        self.assertGreater(input_size, output_size)

    def test_un_lzma(self):
        input_filename = "./TestFiles/test_data.txt"
        compressed_filename = "./TestFiles/test_data.xz"
        uncompressed_filename = "./TestFiles/uncompressed_lzma.txt"

        # Fill with random input.
        fill_a_file(input_filename, 20000)
        input_size = os.path.getsize(input_filename)
        print("input_size: ", input_size)
        # Compress the file using gz. 
        compress.to_lzma(input_filename, compressed_filename)

        compressed_size = os.path.getsize(compressed_filename)
        print("compressed size: ", compressed_size)
        method = compress.un_lzma
        run_method(method, compressed_filename, uncompressed_filename)
        
        decompressed_size = os.path.getsize(uncompressed_filename)
        print("decompressed size: ", decompressed_size)
        self.assertGreater(decompressed_size, compressed_size)

    def test_to_gzip(self):
        input_filename = "./TestFiles/test_data.txt"
        output_filename = "./TestFiles/test_data.gzip"

        # Fill with random input.
        fill_a_file(input_filename, 20000)

        input_size = os.path.getsize(input_filename)

        test_method = compress.to_gzip
        run_method(test_method, input_filename, output_filename)
        
        output_size = os.path.getsize(output_filename)

        self.assertGreater(input_size, output_size)

    def test_un_gzip(self):
        input_filename = "./TestFiles/test_data.txt"
        compressed_filename = "./TestFiles/test_data.gzip"
        uncompressed_filename = "./TestFiles/uncompressed_lzma.txt"

        # Fill with random input.
        fill_a_file(input_filename, 20000)
        input_size = os.path.getsize(input_filename)
        print("input_size: ", input_size)
        # Compress the file using gz. 
        compress.to_gzip(input_filename, compressed_filename)

        compressed_size = os.path.getsize(compressed_filename)
        print("compressed size: ", compressed_size)
        method = compress.un_gzip
        run_method(method, compressed_filename, uncompressed_filename)
        
        decompressed_size = os.path.getsize(uncompressed_filename)
        print("decompressed size: ", decompressed_size)
        self.assertGreater(decompressed_size, compressed_size)
    
    def test_to_gz_single_file(self):
        filename = "./TestFiles/test_data.txt"

        # Fill with random input.
        fill_a_file(filename, 20000)

        input_size = os.path.getsize(filename)

        test_method = compress.to_gz
        run_method(test_method, filename, filename)
        
        output_size = os.path.getsize(filename)

        self.assertNotEqual(0, output_size)
        self.assertGreater(input_size, output_size)

    def test_un_gz_single_file(self):
        filename = "./TestFiles/test_data.txt"
    
        # Fill with random input.
        fill_a_file(filename, 20000)
        input_size = os.path.getsize(filename)
        print("input_size: ", input_size)
        # Compress the file using gz. 
        compress.to_gz(filename, filename)

        compressed_size = os.path.getsize(filename)
        print("compressed size: ", compressed_size)
        method = compress.un_gz
        run_method(method, filename, filename)
        
        decompressed_size = os.path.getsize(filename)
        print("decompressed size: ", decompressed_size)
        self.assertNotEqual(0, input_size)
        self.assertNotEqual(0, compressed_size)
        self.assertNotEqual(0, decompressed_size)
        self.assertEqual(input_size, decompressed_size)
        self.assertGreater(decompressed_size, compressed_size)

    def test_to_bz2_single_file(self):
        filename = "./TestFiles/test_data.txt"

        # Fill with random input.
        fill_a_file(filename, 20000)

        input_size = os.path.getsize(filename)

        test_method = compress.to_bz2
        run_method(test_method, filename, filename)
        
        output_size = os.path.getsize(filename)

        self.assertNotEqual(0, output_size)
        self.assertGreater(input_size, output_size)

    def test_un_bz2_single_file(self):
        filename = "./TestFiles/test_data.txt"
    
        # Fill with random input.
        fill_a_file(filename, 20000)
        input_size = os.path.getsize(filename)
        print("input_size: ", input_size)
        # Compress the file using gz. 
        compress.to_bz2(filename, filename)

        compressed_size = os.path.getsize(filename)
        print("compressed size: ", compressed_size)
        method = compress.un_bz2
        run_method(method, filename, filename)
        
        decompressed_size = os.path.getsize(filename)
        print("decompressed size: ", decompressed_size)
        self.assertNotEqual(0, input_size)
        self.assertNotEqual(0, compressed_size)
        self.assertNotEqual(0, decompressed_size)
        self.assertEqual(input_size, decompressed_size)
        self.assertGreater(decompressed_size, compressed_size)

    def test_to_lzma_single_file(self):
        filename = "./TestFiles/test_data.txt"

        # Fill with random input.
        fill_a_file(filename, 20000)

        input_size = os.path.getsize(filename)

        test_method = compress.to_lzma
        run_method(test_method, filename, filename)
        
        output_size = os.path.getsize(filename)

        self.assertNotEqual(0, output_size)
        self.assertGreater(input_size, output_size)

    def test_un_lzma_single_file(self):
        filename = "./TestFiles/test_data.txt"
    
        # Fill with random input.
        fill_a_file(filename, 20000)
        input_size = os.path.getsize(filename)
        print("input_size: ", input_size)
        # Compress the file using gz. 
        compress.to_lzma(filename, filename)

        compressed_size = os.path.getsize(filename)
        print("compressed size: ", compressed_size)
        method = compress.un_lzma
        run_method(method, filename, filename)
        
        decompressed_size = os.path.getsize(filename)
        print("decompressed size: ", decompressed_size)
        self.assertNotEqual(0, input_size)
        self.assertNotEqual(0, compressed_size)
        self.assertNotEqual(0, decompressed_size)
        self.assertEqual(input_size, decompressed_size)
        self.assertGreater(decompressed_size, compressed_size)
    
    def test_to_gzip_single_file(self):
        filename = "./TestFiles/test_data.txt"

        # Fill with random input.
        fill_a_file(filename, 20000)

        input_size = os.path.getsize(filename)

        test_method = compress.to_gzip
        run_method(test_method, filename, filename)
        
        output_size = os.path.getsize(filename)

        self.assertNotEqual(0, output_size)
        self.assertGreater(input_size, output_size)

    def test_un_gzip_single_file(self):
        filename = "./TestFiles/test_data.txt"
    
        # Fill with random input.
        fill_a_file(filename, 20000)
        input_size = os.path.getsize(filename)
        print("input_size: ", input_size)
        # Compress the file using gz. 
        compress.to_gzip(filename, filename)

        compressed_size = os.path.getsize(filename)
        print("compressed size: ", compressed_size)
        method = compress.un_gzip
        run_method(method, filename, filename)
        
        decompressed_size = os.path.getsize(filename)
        print("decompressed size: ", decompressed_size)
        self.assertNotEqual(0, input_size)
        self.assertNotEqual(0, compressed_size)
        self.assertNotEqual(0, decompressed_size)
        self.assertEqual(input_size, decompressed_size)
        self.assertGreater(decompressed_size, compressed_size)
    
    

    


if __name__ == '__main__':
    unittest.main()
