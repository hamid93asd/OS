import psutil

appName = "firefox.exe"    # enter application name

print("running...")
process = filter(lambda p: p.name() == appName, psutil.process_iter())
for i in process:
    print(i.name,i.pid)
    i.kill()


