from datetime import datetime

now = datetime.now()
log = open('Log.txt', 'a')

#current_time = now.strftime("%H:%M:%S")
current_time = now.strftime("%c")
log.write("Test file was opened on " + current_time + "\n")
log.close()
