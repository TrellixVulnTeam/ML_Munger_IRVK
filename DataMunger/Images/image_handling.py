# Standard libraries
import imghdr
from PIL import Image as im
from PIL import ImageChops
import imghdr

# Custom libraries.
import file_operations as fo

VALID_FORMATS = {
    "APNG": ["apng"],
    "BMP":["bmp"],
    "DDS":["dds"],
    "DIB":["dib"],
    "EPS":["eps"],
    "GIF":["gif"],
    "ICNS":["icns"],
    "ICO": ["ico"],
    "IM": ["im"],
    "JPEG": ["jpeg", 'jpg', 'jfif'],
    "JPEG 2000": ["j2k", "j2p", 'jpx'],
    "MSP": ["msp"],
    "PCX": ["pcx"],
    "PNG": ["png"],
    "PPM": ["pbm", "pgm","ppm", "pnm"],
    "SGI": ["sgi"],
    "SPIDER": ["spider"],
    "TGA": ["tga"],
    "TIFF": ["tiff","tif"],
    "WebP": ["webp"],
    "XBM": ["xbm"],
    "BLP": ["blp"],
    "CUR": ["cur"],
    "DCX": ["dcx"],
    "FLI": ["fli"],
    "FLC": ["flc"],
    "FPX": ["fpx"],
    "FTEX": ["ftex"],
    "GBR": ["gbr"],
    "GD": ["gd"],
    "IMT": ["imt"],
    "IPTC": ["iptc"],
    "NAA": ["naa"],
    "MCIDAS": ["mcidas"],
    "MIC": ["mic"],
    "MPO": ["mpo"],
    "PCD": ["pcd"],
    "PIXAR": ["pixar"],
    "PSD": ["psd"],
    "WAL": ["wal"],
    "WMF": ["wmf"],
    "XPM": ["xpm"],
}

def resize_images_overwrite(directory, size = (100, 100)):
    itr = fo.iterate_filelist_by_filename(directory, resize_image, None, size)
    for i in itr:
        filename, image = i
        image.save(directory + filename)
        image.close()

def resize_images_save(source, destination, size = (100, 100)):
    itr = fo.iterate_filelist_by_filename(source, resize_image, None, size)
    for i in itr:
        filename, image = i
        image.save(destination + filename)
        image.close()

def convert_grayscale_overwrite(directory):
    itr = fo.iterate_filelist_by_filename(directory, convert_grayscale)
    for i in itr:
        filename, image = i
        image.save(directory + filename)
        image.close()

def convert_grayscale_save(source, destination):
    itr = fo.iterate_filelist_by_filename(source, convert_grayscale)
    for i in itr:
        filename, image = i
        image.save(destination + filename)
        image.close()

def convert_filetype_overwrite(directory, ext):
    itr = fo.iterate_filelist_by_filename(directory, convert_filetype, None, ext)
    for i in itr:
        new_filename, old_filename, image = i
        image.save(directory + new_filename)
        image.close()
        old_ext = fo.get_ext(old_filename)
        if ext != old_ext:
            fo.remove_file(old_filename)
        

def convert_filetype_save(source, destination, ext):
    itr = fo.iterate_filelist_by_filename(source, convert_filetype, None, ext)
    for i in itr:
        new_filename, old_filename, image = i
        image.save(destination + filename)
        image.close()

def generate_rgb_check_list(source):
    rgb_list = []
    itr = fo.iterate_filelist_by_filename(source, check_rgb)
    for i in itr:
        filename, result = i
        rgb_list.append((filename, result))
    print(rgb_list)

def generate_type_check_list(source):
    type_list = []
    itr = fo.iterate_filelist_by_filename(source, check_filetype)
    for i in itr:
        filename, result = i
        type_list.append((filename, result))
    print(type_list)


# Helper functions

def resize_image(path, size):
    image = im.open(path)
    image = image.resize(size[0])
    filename = fo.get_basename(path)
    return filename, image
    
def get_num_pixels(path):
    width, height = im.open(path).size
    return width * height

def check_rgb(path):
    filename = fo.get_basename(path)
    image = im.open(path)
    
    if image.mode not in ("L", "RGB"):
        return filename, "Unsupported image mode"
    
    if image.mode == "RGB":
        rgb = image.split()

        if ImageChops.difference(rgb[0], rgb[1]).getextrema()[1]!= 0:
            return filename, True
        elif ImageChops.difference(rgb[1],rgb[2]).getextrema()[1]!= 0:
            return filename, True
    
    return filename, False

def check_filetype(path):
    filename = fo.get_basename(path)
    
    return filename, False

def convert_grayscale(path):
    image = im.open(path).convert('L')
    filename = fo.get_basename(path)
    return filename, image

def convert_filetype(path, ext):
    ext = ext.replace(".", "")
   
    new_filename = fo.get_filename(path)
    image = im.open(path).convert('RGB')
    old_ext = imghdr.what(path)
    print("old ext: ", old_ext)
    if old_ext is None:
        print(path + " " + "has unsupported filetype.")
        return old_ext, image

    elif valid_format(ext):
        raise Exception("Invalid file format: ", ext)

    return  new_filename + "." + ext, path, image
    

def check_filetype(path):
    filename = fo.get_filename(path)
    img_type = imghdr.what(path)
    
    if img_type == None or valid_format(img_type):
        return filename, "Unsupported filetype"

    return filename, img_type

def valid_format(ext):
    return any(ext in val for val in VALID_FORMATS.values()) == False