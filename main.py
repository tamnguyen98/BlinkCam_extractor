from blinkpy import blinkpy
import datetime

USER = '' # User name to your blink account
PASS = '' # Password to your blink account
print('Downloader running...')

# Location to store the videos
blink_dir = 'PATH/TO/STORAGE' # Location to store the videos
date = datetime.datetime

try: # check out directory for file
    dir_status = open(blink_dir+'last_record', 'r+')
    info = dir_status.readline()
except IOError:
    dir_status = open(blink_dir+'last_record', 'w')
    info = "2019/12/14 00:00"
try:
    old_time =  int(info.split(' ')[1].split(':')[0])
except ValueError:
    old_time = int(date.now().strftime("%H"))

dir_status.close()

while(True):
    timer = int(date.now().strftime("%H"))
    if (timer != old_time): # check if an hr has passed
        dir_status = open(blink_dir+'last_record', 'r+')
        print("Time difference detected. Old time: ", old_time)
        # log into blink
        try:
            blink = blinkpy.Blink(username=USER, password=PASS)
            blink.start()
        except AttributeError:
            print("Error logging in, retrying...")
            blink = blinkpy.Blink(username=USER, password=PASS)
            blink.start()


        blink.refresh()             # Get new information from server

        blink.download_videos('F:/Blink_cam/', since=info)
        info = date.now().strftime("%Y/%m/%d %H:%M") # Update last save state
        dir_status.seek(0)
        dir_status.write(info)
        dir_status.truncate()
        dir_status.close()
        old_time = timer
