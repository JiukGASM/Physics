import os
os.system("ffmpeg -f image2 -r 100 -i /Users/leejiuk1/Documents/lectureincau/3rd/1semester/computationalphysics/pendulum3/pendulum_%04d.png -vcodec"
          " mpeg4 -y /Users/leejiuk1/Documents/lectureincau/3rd/1semester/computationalphysics/pendulum3.mp4")