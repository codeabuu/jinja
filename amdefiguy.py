import time
time = time.time()

ts = time

file = open("amdefiguy.txt", 'w')
file.write("Time of run | ")
file.write(str(ts))
file.close()
