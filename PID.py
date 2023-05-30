import psutil

pid = psutil.pids()

for a in pid:
    p = psutil.Process(a)
    print('Name:',p.name(),'-','PID:',p.pid)