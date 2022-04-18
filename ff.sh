ffmpeg \
-thread_queue_size 2048 \
-f v4l2 -i /dev/video0 \
-c:v h264_nvmpi -preset:v ultrafast -g 8 -b:v 10000k -maxrate 10000k \
-fflags nobuffer \
-threads 4 -q:v 100 \
-r 30 \
-video_size 1280x720 \
-f flv rtmp://73.108.220.91/live/test

# Extra options:
#-pix_fmt yuv420p 
