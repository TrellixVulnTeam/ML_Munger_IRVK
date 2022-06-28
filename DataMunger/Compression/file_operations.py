import os
import glob
import random
import shutil
import subprocess

def create_dir_tree_list(source):
    tree = []
    for root, dirs, files in os.walk(root):
        for f in files:
            path = os.path.join(root, f)
            tree.append(path)
    return tree

# Iterate through filenames and apply sent function to the filename.
# If filetype is not given, will apply operation to all files.  
def iterate_filelist_by_filename(directory, func = None, filetype= None, *args):
    if func is None:
        if filetype is None:
            for filename in os.listdir(directory):
                yield directory + "/" + filename
                
        else:
            for filename in os.listdir(directory):
                if filename.endswith(filetype):
                        yield directory + "/" + filename
                    
    else:
        if filetype is None:
            for filename in os.listdir(directory):
                try:
                    yield func(directory + filename, *args)
                except Exception as e:
                    print(str(func), "invalid for file: ", filename, "because of: ", e)
        
        else:
            for filename in os.listdir(directory):
                if filename.endswith(filetype):
                    try:
                        yield func(directory + filename, *args)
                    except Exception as e:
                        print(str(func), "invalid for file: ", filename, "because of: ", e)





def pick_random_file_in_dir(directory):
   filelist = os.listdir(directory)
   choice = random.randint(0, len(filelist)-1)
   print("new choice: ", filelist[choice])
   return directory + filelist[choice]



# Iterate recursively through directory.
def iterate_subdirs_by_filename(rootdir, func = None, filetypes= None):
    if func is None:
        if filetypes is None:
            for filename in glob.iglob(rootdir + '**/*.*', recursive=True):
                yield filename
        else: 
            for filename in glob.iglob(rootdir +'**/*.*', recursive=True):
                for filetype in filetypes:
                    if filename.endswith(filetype):
                        yield filename
    else:                        
        if filetypes is None:
            for filename in glob.iglob(rootdir + '**/*.*', recursive=True):
                try:
                    yield func(filename)
                except Exception as e:
                    print(str(func), "invalid for file: ", filename, "because of: ", e)
        else: 
            for filename in glob.iglob(rootdir +'**/*.*', recursive=True):
                for filetype in filetypes:
                    if filename.endswith(filetype):
                        try:
                            yield func(filename)
                        except Exception as e:
                            print(str(func), "invalid for file: ", filename, "because of: ", e)



# Iterate over subdirectory
def count_files_subfolder(directory):
    for subdir in os.listdir(directory):
        yield len(os.listdir(directory + subdir))

def iterate_by_subdir(directory):
    for subdir in os.listdir(directory):
        yield subdir

def check_subdir_in_dir(directory, subdir):
    filelist = os.listdir(directory)
    return subdir in filelist

def save(source, destination):
    print("saving:", source, "to:", destination)
    shutil.copy(source, destination)

def move(source, destination):
    print("moving:", source, "to:", destination)
    shutil.move(source, destination)

def make_directory(path):
    print("making dir: ", path)
    os.mkdir(path)

def split_filename(path):
    path, ext = os.path.splitext(path)
    split = path.split('/')[-1].split('\\')[-2]
    
    return split

def get_basename(path):
    return os.path.basename(path)

def get_filename(path):
    base = get_basename(path)
    return os.path.splitext(base)[0]

def get_ext(path):
    base = get_basename(path)
    return os.path.splitext(base)[1]

def remove_file(path):
    os.remove(path)

def remove_ext(path):
    return os.path.splitext(path)[0]

def run_7z(source, target):
    exe = "C:\\7za.exe"
    subprocess.call(exe + " a -t7z \"" + target + "\" \"" + source + "\" -mx=9")

def clear_directory(target):
    pass

def remove_dir_empty(target):
    os.rmdir(target)

def remove_dir_tree(target):
    shutil.rmtree(target)

def create_file_in_dir(dir, filename, ext = None):
    if ext is not None:
        filename += ext
    f = open(dir + filename, 'w')
    f.close()