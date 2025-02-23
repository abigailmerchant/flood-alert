import os
import time
import subprocess
from datetime import datetime

# 🚀 GitHub Repository Setup
repo_path = "C:/flood-alert"  # Update this to your actual GitHub repo path
image_file = os.path.join(repo_path, "alert.png")  # Image file to push

# 🕒 Set time window for sending the alert
ALERT_START_HOUR = 8   # 8 AM
ALERT_END_HOUR = 20    # 8 PM

# 🌟 Condition for pushing alert
number = 1  # Change this dynamically in your code

def is_time_to_send_alert():
    now = datetime.now()
    return ALERT_START_HOUR <= now.hour < ALERT_END_HOUR

def create_blank_image():
    """Creates or updates alert.png to ensure Git detects a change."""
    with open(image_file, "wb") as f:
        f.write(b'\x89PNG\r\n\x1a\n')  # Minimal PNG header
    print(f"Created/Updated {image_file}")

def push_to_github():
    """Pushes alert.png to the GitHub repository only if changes exist."""
    os.chdir(repo_path)

    # Ensure Git identity is set
    subprocess.run(["git", "config", "--global", "user.name", "abigailmerchant"], check=True)
    subprocess.run(["git", "config", "--global", "user.email", "abigail.merchant123@gmail.com"], check=True)

    # Pull the latest changes to avoid merge conflicts
    subprocess.run(["git", "pull", "origin", "main", "--no-rebase"], check=True)

   
# 🔥 Check conditions and send the alert if needed
if number == 1 and is_time_to_send_alert():
    create_blank_image()
    push_to_github()
else:
    print("⏳ No alert sent. Either number != 1 or outside alert hours.")