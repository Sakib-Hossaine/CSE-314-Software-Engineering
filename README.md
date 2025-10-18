# Django Project with WebRTC Integration

A Django web application with WebRTC functionality for real-time communication.

## ✨ Features

-  🛠 Django backend with user authentication
-  📹 WebRTC integration for real-time video/audio communication
-  📱 Responsive frontend design
-  🖼 Project showcase section with image upload capability
-  🔒 Secure signaling server with Node.js

## 🚀 Prerequisites

Before you begin, ensure you have met the following requirements:

-  Python 3.6+
-  Node.js (LTS version)
-  npm (comes with Node.js)
-  Git

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sakib-Hossaine/DJANGO-Project.git
cd DJANGO-Project

2. Set up Python environment
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
or conda activate ll2

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

3. Set up Django
# Apply database migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Follow prompts to create admin account

4. Set up WebRTC Node.js server
cd webrtc-node-app
npm install
node server.js

🏃 Running the Project

Django Development Server:
python manage.py runserver

WebRTC Signaling Server (in separate terminal):
cd webrtc-node-app
node server.js
```
