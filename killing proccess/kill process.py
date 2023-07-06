import psutil

print("running...")
process = filter(lambda p: p.name() == "firefox.exe", psutil.process_iter())
for i in process:
    print(i.name,i.pid)
    i.kill()


