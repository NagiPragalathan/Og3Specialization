import subprocess
import os
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb+srv://nagi:nagi@cluster0.ohv5gsc.mongodb.net/nagidb')
db = client['Og3Collection']
collection = db['Og3']

def do_line(num=0):
    SIZE = os.get_terminal_size()
    COL = SIZE.columns
    return "-"*(COL-num) if num != 0 else "-"*(COL)

# JavaScript code to be executed
def upload(js_code, upload_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    temp_js_path = os.path.join(parent_dir, 'temp_script.js')
    with open(temp_js_path, 'w') as temp_js_file:
        temp_js_file.write(js_code)

    try:
        result = subprocess.run(['node', temp_js_path], capture_output=True, text=True)
        file_root_hash = result.stdout.strip()
        error_message = result.stderr.strip()

        print(f"\n \n{do_line()}\nFile Root Hash: {file_root_hash}\n{do_line(1)}")
        if error_message:
            print(f"File Upload error: {error_message}")

        # Insert relevant data into MongoDB
        collection.insert_many([{
            "file_path": upload_file,
            "file_root_hash": file_root_hash,
            "error_message": error_message
        }])
    finally:
        os.remove(temp_js_path)
