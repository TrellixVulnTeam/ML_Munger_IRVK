import archive
import random 
import string
import file_operations as fo

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
    
def add_test_files(dir):
    fo.create_file_in_dir(dir, "file1", ".txt")
    fo.create_file_in_dir(dir, "file2", ".txt")
    fo.create_file_in_dir(dir, "file3", ".txt")

def reset_dir(filename):
    try:
        fo.remove_dir_tree(filename)
        fo.remove_dir_empty(filename)
    except Exception as e:
        print("file already does not exist")
    finally:
        fo.make_directory(filename)



def run_method(method, input, output):
    if output is None:
        output = input
    method(input, output)

class TestCompress(unittest.TestCase):
    def test_to_tar_gz(self): 
        source = "./TestFiles/"
        add_test_files(source)
        dest = "./Archive/"
        reset_dir(source)
        reset_dir(dest)
        archive.to_tar_gz(source, dest)


    def test_un_tar_gz(self):
        source = "./TestFiles/"
        arch = "./Archive/"
        dest = "./DeArchive/"
        reset_dir(source)
        reset_dir(dest)
        reset_dir(arch)
        add_test_files(source)
        archive.to_tar_gz(source, arch)
        archive.un_tar(arch + ".tar.gz", dest)

    def test_to_tar_bz(self): 
        source = "./TestFiles/"
        add_test_files(source)
        dest = "./Archive/"
        reset_dir(source)
        reset_dir(dest)
        archive.to_tar_bz(source, dest)


    def test_un_tar_bz(self):
        source = "./TestFiles/"
        arch = "./Archive/"
        dest = "./DeArchive/"
        reset_dir(source)
        reset_dir(dest)
        reset_dir(arch)
        add_test_files(source)  
        archive.to_tar_bz(source, arch)
        archive.un_tar(arch + ".tar.bz", dest)

    def test_to_tar_xz(self): 
        source = "./TestFiles/"
        add_test_files(source)
        dest = "./Archive/"
        reset_dir(source)
        reset_dir(dest)
        archive.to_tar_xz(source, dest)


    def test_un_tar_xz(self):
        source = "./TestFiles/"
        arch = "./Archive/"
        dest = "./DeArchive/"
        reset_dir(source)
        reset_dir(dest)
        reset_dir(arch)
        add_test_files(source)  
        archive.to_tar_bz(source, arch)
        archive.un_tar(arch + ".tar.xz", dest)


        

if __name__ == '__main__':
    unittest.main()