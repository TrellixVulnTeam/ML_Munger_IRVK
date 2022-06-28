import tarfile
from zipfile import ZipFile
import file_operations as fo

# Common extensions for each.
# .tar – A raw tar file.
# .tar.gz, .tgz, .tar.gzip – Gzip tar archive.
# .tar.bz2, .tbz, .tbz2, .tar.bzip2 – Bzipped tar archive.
# .tar.Z, .Z, .taz – Compress tar archive.
# .lzma, xz - compress lzma tar archive
#import file_operations as fo

import file_operations as fo

def search(search_term, string_being_searched):
    return search_term in string_being_searched

def contains_tar_gz_extension(str):
    return ((search(".tar.gz", str) and str[-7] == ".tar.gz") or
        (search(".tgz", str) and str[-4] == ".tgz")  or      
        (search(".tar.gzip", str) and str[-9] == ".tar.gzip"))
           
def contains_tar_bz2_extension(str):
    return ((search(".tar.bz2",str) and str[-8] == ".tar.bz2") or
        (search(".tbz", str) and str[-4] == ".tbz")  or      
        (search(".tbz2", str) and str[-5] == ".tbz2")
        (search(".tar.bzip2", str) and str[-10] == ".tar.bzip2"))

def contains_tar_lzma_extension(str):
    return  ((search(".tar.lzma", str) and str[-9] == ".tar.lzma") or
        (search(".tar.xz", str) and str[-7] == ".tar.xz"))
    

def to_tar_gz(source, output):
    print("output:", type(contains_tar_gz_extension(output)))
    if not contains_tar_gz_extension(output):
        output += ".tar.bz2"

    with tarfile.open(name = output, mode = "w:gz") as tar:
        tar.add(source, arcname=fo.get_basename(source))

def to_tar_bz(source, output):
    if not contains_tar_bz2_extension(output):
        output += ".tar.gz"
    with tarfile.open(output, "w:bz2") as tar:
        tar.add(source, arcname=fo.get_basename(source))

def to_tar_xz(source, output):
    if not contains_tar_lzma_extension(output):
        output += ".tar.lzma"
    with tarfile.open(output, "w:xz") as tar:
        tar.add(source, arcname=fo.get_basename(source))

    
def to_zip(source, output):
    paths = fo.create_dir_tree_list(source)
    with ZipFile(output + ".zip", 'w') as zip:
        for p in paths:
            zip.write(p)


def to_7z(source, output):
    fo.run7z(source, output)


# Decompress the archive.
def un_tar(source, output):
    with tarfile.open(source) as tar:
        tar.extractall(output)
    
def un_zip(source, output):
    paths = fo.create_dir_tree_list(source)
    with ZipFile(output + ".zip", 'w') as zip:
        for p in paths:
            zip.write(p)