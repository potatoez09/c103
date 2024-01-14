import os
import shutil
import sys
import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/pasup/OneDrive"
to_dir = "C:/Users/pasup/downloads"

dir_tree = {
    "Image_Files":['.gif','png','.jpg','.jpeg','.jfif'],
    "Video_Files":['.mpg','.mp2','.mpeg',',mpe','.mpv','.mp4','.m4p','.avi','.mov'],
    "Document_Files":['.ppt','.xls','.xlsx','.csv','.pdf','.txt'],
    "Setup_Files":['.exe','.bin','.cmd','.msi','.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("downloeded" + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/ ' + key
                path3 = to_dir + '/' + key + "/" + file_name

                if os.path.exists(path2):
                    print("directory exists.....")
                    print("moving " + file_name + ".....")
                    shutil.move(path1,path3)
                    time.sleep(1)

                else:
                    print ("making directory...")
                    os.makedirs (path2)    
                    print("moving " + file_name + ".....")
                    shutil.move(path1,path3)   
                    time.sleep(1)

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running.....")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()