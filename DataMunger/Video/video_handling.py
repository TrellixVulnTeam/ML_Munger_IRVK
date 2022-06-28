import cv2

import file_operations as fo

def get_frames_all_videos_by_rate(source, dest, ext = ".png", rate = 1):
    itr = fo.iterate_filelist_by_filename(source, get_video_frames_frame_rate, None, dest, ext, rate)
    for i in itr:
        filename, image = i
        image.save(directory + filename)
        image.close()

def get_frames_all_videos_by_sec(source, dest, ext = ".png", num_sec_mult = 1):
    itr = fo.iterate_filelist_by_filename(source, get_video_frames_seconds, None, dest, ext, num_sec_mult)
    for i in itr:
        filename, image = i
        image.save(directory + filename)
        image.close()


def get_video_frames_frame_rate(path, new_filename, ext, rate = 1):
    filename = fo.get_basename(path)
    cap = cv2.VideoCapture(filename)
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        try:
            cv2.imwrite(new_filename + filename + str(count) + ext, frame)
        
        except:
            print(ext, " is invalid file format.")
            cap.release()
            cv2.destroyAllWindows()
            return
        count += rate
        cap.set(1, count)
    cap.release()
    cv2.destroyAllWindows()

def get_video_frames_seconds(path, new_filename, ext, num_sec_mult = 1):
    filename = fo.get_basename(path)
    cap = cv2.VideoCapture(filename)
    count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    rate = fps * num_sec_mult

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        try:
            cv2.imwrite(new_filename + filename + str(count) + ext, frame)
        
        except:
            print(ext, " is invalid file format.")
            cap.release()
            cv2.destroyAllWindows()
            return
        count += rate
        cap.set(1, count)
    cap.release()
    cv2.destroyAllWindows()
    
    