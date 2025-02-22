import os
import subprocess
import getpass
from datetime import datetime
from flask import Flask
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop_endpoint():
    # 1. Your full name
    full_name = "Kshitij Kashyap"  # e.g., "John Doe"

    # 2. System username
    username = getpass.getuser()

    # 3. Server Time in IST
    ist_timezone = pytz.timezone("Asia/Kolkata")
    server_time_ist = datetime.now(ist_timezone).strftime("%Y-%m-%d %H:%M:%S %Z")

    # 4. top output (one-time snapshot)
    #    '-b' = batch mode, '-n1' = run once
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")

    # Build the HTML response
    html_response = f"""
    <html>
    <head><title>HTOP Endpoint</title></head>
    <body>
        <h1>HTOP Endpoint</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time_ist}</p>
        <hr>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
