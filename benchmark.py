import speedtest
import time
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
uSpeed = []
dSpeed = []
times = []
user = input("Welcome to Benchmark 2.0:\n1:Test transmission speed\n2:Test upload and download speed\n")
i=0.0
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
if int(user)==1:
    connection = input("Enter your connection name: ")
    execute = "awk '/:/ { print($1, $10) }' < /proc/net/dev | grep "+connection+" > speeds.txt"
    os.system(execute)
    print("Running... ctrl-c to stop")
    try:
        while True:
            text_file = open("speeds.txt", "r")
            lines = text_file.read().split(' ')
            if i == 0.0:
                old=lines
            dSpeed.append((float(lines[1])-float(old[1]))/(1<<20))
            times.append(i)
            i+=1.0
            time.sleep(1)
            old = lines
            os.system(execute)
    except KeyboardInterrupt:
        now=datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('Generating graph')
        plt.xlabel('Time (s)')
        plt.ylabel('Transmission (mbits/s)')
        #plt.text(-5, 60, str(np.mean(dSpeed)), fontsize = 22)
        plt.plot(times,dSpeed, marker='o', color = 'r')
        plt.show()
        plt.savefig('graph'+str(now)+'.png')
        print(np.mean(dSpeed))
        print('Graph generated')
        quit()
else:
    print("Running a speed test...")
    st = speedtest.Speedtest()
    mbitsU=st.upload()/1000000.0
    mbitsD=st.download()/1000000.0
    print("Upload Speed: ", mbitsU, "Mbp/s")
    print("Download Speed: ", mbitsD, "Mbp/s")
        
