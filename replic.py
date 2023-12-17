# Replicate files to another folder with time interval and generate a log file
# Usage : python + replic.py + folder from + folder to + interval(hours : ex 0.5, 1 ,12)
# Ex : python replic.py c:\teste\origem c:\teste\destino 0.001

import os
import sys
import shutil
import schedule
import time
import hashlib
import logging
from datetime import datetime


def synchronize_folders(source_folder, replica_folder):
    # Make sure source and replica folders exist
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return

    if not os.path.exists(replica_folder):
            os.mkdir(replica_folder)
            #print("Source or replica folder does not exist.")
            #return

    # Get the list of files in the source folder
    source_files = set(os.listdir(source_folder))

    # Get the list of files in the replica folder
    replica_files = set(os.listdir(replica_folder))

    # Files to be copied or updated
    to_copy = source_files - replica_files

    # Files to be removed from replica folder
    to_remove = replica_files - source_files
    

    print (curr_datetime)
    log_file = (r"c:\temp\sync_" + curr_datetime + ".log")
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

    #create log file activity
    with open(r"c:\temp\replicate.log_" + curr_datetime + ".log","a+") as outtext:
        # Copy new or modified files
        outtext.write("Starting Synchronization : " + curr_datetime + "\r\n")
        outtext.write("-----------------------------------------------\r\n")
        outtext.write(" Files copied to Replica folder                \r\n")
        outtext.write("-----------------------------------------------\r\n")
        for file_name in to_copy:
            source_path = os.path.join(source_folder, file_name)
            replica_path = os.path.join(replica_folder, file_name)
            shutil.copy2(source_path, replica_path)
            # extract MD5 hash start
            file_obj_source_path = open(source_path, 'rb')
            file_obj_replica_path = open(source_path, 'rb')
            source_path = file_obj_source_path.read()
            replica_path = file_obj_replica_path.read()
            md5_hash_source = hashlib.md5(source_path).hexdigest()
            md5_hash_replica = hashlib.md5(replica_path).hexdigest()
            file_obj_source_path.close()
            file_obj_replica_path.close()
            # extract MD5 hash end
            print(f"Copied: {file_name}")
            outtext.write("File : "+ file_name + " - MD5 source : " + md5_hash_source + " - MD replica : " + md5_hash_replica + "\r\n")
        

        # Remove files not present in the source folder
        outtext.write("-----------------------------------------------\r\n")
        outtext.write(" Files removed to Replica folder               \r\n")
        outtext.write("-----------------------------------------------\r\n")
        for file_name in to_remove:
            file_path = os.path.join(replica_folder, file_name)
            os.remove(file_path)
            print(f"Removed: {file_name}")
            outtext.write("File : "+ file_name + "\r\n")
        
        print("Synchronization complete.")
        outtext.write("Synchronization complete : " + curr_datetime + "\r\n")
        outtext.close()
    
# Schedule synchronization every 1 hour
curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')    
for value in sys.argv:
    print (sys.argv[0])
    print (sys.argv[1])
    print (sys.argv[2])
    print (sys.argv[3])
    path_from = sys.argv[1] 
    path_to = sys.argv[2]
    interval = sys.argv[3]
#path_from = input("From : ")
#path_to = input("To : ")
#interval = input ("Interval (hours) : ")

interval = float(interval)
schedule.every(interval).hours.do(synchronize_folders, path_from, path_to)


# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)