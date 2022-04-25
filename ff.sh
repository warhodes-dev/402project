ffmpeg \
-f v4l2 -i /dev/video0 \
-c:v h264_nvmpi -preset:v ultrafast -profile:v high -level:v 4.0 \
-b:v 1000k \
-fflags nobuffer \
-r 30 \
-f flv rtmp://73.108.220.91/live/jetson

# Extra options:
#-pix_fmt yuv420p 
#-b:v 10000k \
#-video_size 2304x1536
