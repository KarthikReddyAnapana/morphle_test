from flask import Flask
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your actual full name
    username = os.environ.get("USER", "Unknown User")  # Fetch username or default to "Unknown User"
    server_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
    top_output = os.popen("top -b -n 1").read()
    
    return f"Name: {name}<br>Username: {username}<br>Server Time: {server_time}<br>Top Output: <pre>{top_output}</pre>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
