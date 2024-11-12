from django.http import HttpResponse
import os
from datetime import datetime
import pytz

def htop(request):
    name = "ANAPANA KARTHIK REDDY"  # Replace with your actual full name
    username = os.environ.get("USER", "Unknown User")  # Fetch username or default to "Unknown User"
    server_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
    top_output = os.popen("top -b -n 1").read()
    
    return HttpResponse(
        f"Name: {name}<br>Username: {username}<br>Server Time: {server_time}<br>Top Output: <pre>{top_output}</pre>"
    )
