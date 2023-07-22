import psutil

# Maximum Threshold CPU Usage
threshold = 50
try:
    print("Monitoring CPU usage...")
    while True:
        cur_CPU_Usage = psutil.cpu_percent() # Storing the current CPU Usage at a give point of time
        if cur_CPU_Usage > threshold:
            print("Alert! CPU usage exceeds thershold:", cur_CPU_Usage, "%")
except:
    print("CPU Usage Monitor stopped...!")