# utils/helpers.py
import os

def log_event(event_message):
    log_directory = 'logs'
    log_file_path = os.path.join(log_directory, 'events.log')
    
    # Check if the logs directory exists; if not, create it
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    with open(log_file_path, 'a') as log_file:
        log_file.write(event_message + '\n')
