import image_handling as ih
import sound_handling as sh
# source = "./test_dir_copy/"
# source = "./test_type/"
# dest = "./output_dir/"

# ih.resize_images_save(source, dest, (100, 100))
# ih.resize_images_overwrite(source, (100, 100))
# ih.generate_rgb_check_list(dest)
# ih.resize_images_save(source, dest, (100, 100))
# ih.convert_filetype_overwrite(dest, ".png")
# ih.generate_type_check_list(dest)

source = "./sound_test_source/"
dest = "./sound_test_output/"

sh.convert_soundfile_overwrite(dest, "wav")


