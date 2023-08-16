from flask import Flask, render_template
import os
import time

app = Flask(__name__)

def is_recently_modified(file_path, threshold_seconds=3600):
    if os.path.exists(file_path):
        file_stats = os.stat(file_path)
        modification_time = file_stats.st_mtime
        current_time = time.time()
        time_difference = current_time - modification_time
        return time_difference <= threshold_seconds
    return False

@app.route('/')
def index():
    monitored_files = [
        {'name': 'file1.txt', 'path': 'C:\\Users\\Administrator\\rcdev\\100daysOfPython\\Files_dashboard_flask\\main.py'},
        {'name': 'file2.txt', 'path': 'C:\\Users\\Administrator\\rcdev\\100daysOfPython\\day25_pandas\\becas.csv'},
        # Add more files to the list
    ]
    threshold_seconds = 3600  # 1 hour
    
    updated_files = []

    for file in monitored_files:
        if is_recently_modified(file['path'], threshold_seconds):
            file['status'] = 'Updated'
        else:
            file['status'] = 'Not Updated'
        
        updated_files.append(file)

    return render_template('index.html', updated_files=updated_files)

if __name__ == '__main__':
    app.run(debug=True)
