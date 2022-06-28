from pydub import AudioSegment
import ffmpeg
import matplotlib.pyplot as plt
from PIL import Image as im
import subprocess
from scipy.io import wavfile


# import file_operations as fo


# def convert_soundfile_save(source, dest, filetype):
#     itr = fo.iterate_filelist_by_filename(source, convert_to_soundtype, None, dest, filetype)
#     for i in itr:
#         filename = i

        
# def convert_soundfile_overwrite(path, filetype):
#     itr = fo.iterate_filelist_by_filename(path, convert_to_soundtype, None, path, filetype)
#     for i in itr:
#         filename = i
#         ext = fo.get_ext(filename)
#         if ext != "." + filetype:
#             fo.remove_file(filename)

# Helper methods
       
def generate_melspec(path):
    audio =  AudioSegment.from_wav(path)
    arr = audio.get_array_of_samples()
    fs = audio.frame_rate
    plt.specgram(arr, Fs=fs)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format = 'png')
    image = im.open(img_buf)
    img_buf.close()
    return image

# def convert_to_soundtype(source, dest, filetype):
#     new_filename = dest + fo.get_filename(source) 
#     command = f"ffmpeg -i {source} -hide_banner -loglevel error -nostats -y -ab 160k -ac 2 -ar 44100 -vn {new_filename}.{filetype}"
#     subprocess.call(command, shell=True)
#     print("Converting: ", source)
#     return source

generate_melspec("./sound_test_output/BreathingAvSR1.wav")


