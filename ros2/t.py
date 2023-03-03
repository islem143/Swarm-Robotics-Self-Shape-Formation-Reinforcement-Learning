import signal
import psutil
import os
process_name = "gazebo"
pid = None

for proc in psutil.process_iter():
    if process_name in proc.name():
       pid = proc.pid
       break

print("Pid:", pid)
os.kill(pid, signal.SIGKILL)