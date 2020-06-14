import cv2
import os
cwd = os.getcwd()
print(cwd)
videofile = []
for x in os.listdir(os.path.join(cwd, 'video')):
    if x.endswith(".MOV"):
        videofile.append(x)

if input("The video is {0} type y to continue: ".format(videofile)) == "y":
    print("Starting...")

else:
    print("Quiting...")
    quit()

for id, vide in enumerate(videofile):
    video = cv2.VideoCapture('video/' + vide)
    playback,image = video.read()
    playback = True
    frame = 0

    while playback:
        image = cv2.resize(image, (858, 480), interpolation = cv2.INTER_AREA)
        cv2.imwrite(f"dataset/test/real/{id}frame{frame}.jpg", image)
        playback,image = video.read()
        if frame % 30 == 0:
            print ("frame {0}".format(frame))
        frame += 1

    print(vide)