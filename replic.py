import os
import sys
import shutil
import schedule
import time
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
    curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    print (curr_datetime)
    log_file = (r"c:\temp\sync_" + curr_datetime + ".log")
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')


    # Copy new or modified files
    for file_name in to_copy:
        
        source_path = os.path.join(source_folder, file_name)
        replica_path = os.path.join(replica_folder, file_name)
        print (source_path)
        print (replica_path)
        shutil.copy2(source_path, replica_path)
       
        #shutil.copy2(source_folder+file_name,replica_folder+file_name)
        print(f"Copied: {file_name}")

    # Remove files not present in the source folder
    for file_name in to_remove:
        file_path = os.path.join(replica_folder, file_name)
        os.remove(file_path)
        print(f"Removed: {file_name}")

    print("Synchronization complete.")


# Schedule synchronization every 1 hour
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