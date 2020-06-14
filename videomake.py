import cv2
import os
import re

cwd = os.getcwd()
# Thanks to Mark Byers on stackoverflow https://stackoverflow.com/a/4836734
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

# Thanks to BoboDarph on stackoverflow https://stackoverflow.com/a/44948030
images = [img for img in os.listdir(os.path.join(cwd, 'results/H/')) if img.endswith(".jpg")]

frame = cv2.imread(os.path.join('results/H/', images[0]))

height, width, layers = frame.shape

video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc('P', 'I', 'M', '1'), 30, (width,height))

for x,image in enumerate(natural_sort(images)):
    video.write(cv2.imread(os.path.join('results/H/', image)))
    print(f'Frame:{x} from {image}')

cv2.destroyAllWindows()
video.release()