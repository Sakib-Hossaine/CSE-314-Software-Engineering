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

````bash
git clone https://github.com/Sakib-Hossaine/DJANGO-Project.git
cd DJANGO-Project

2. Set up Python environment
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
or conda activate ll2

# Activate (macOS/Linux)
# Django Project with WebRTC Integration

A Django web application with WebRTC functionality for real-time communication. This repository contains the Django backend, a minimal Node.js signaling server used for browser-to-browser connections, and front-end templates and static assets for demonstration and development.

## ✨ Features

- 🛠 Django backend with user authentication and admin
- 📹 WebRTC integration for real-time video/audio communication (signaling via Node.js)
- 📁 Course and notes management (create, update, delete)
- 🖼 Image upload support for course/profile assets
- 🔐 Example payment views and templates for demonstration

## 🚀 Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- Node.js (LTS version)
- npm (comes with Node.js)
- Git

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
````

## Usage

After starting both servers (Django and the Node.js signaling server), open your browser and go to:

-  http://127.0.0.1:8000/ — main Django site

The WebRTC pages are available from the courses or webrtc-related templates; the client code that connects to the signaling server lives under `webrtc-node-app/` and `templates/`.

Typical workflow:

1. Create an account or sign in using the Django auth pages.
2. Create or join a course/class from the `courses` section.
3. Use the provided WebRTC pages to start a call — the browser client will connect to the Node.js signaling server (`webrtc-node-app/server.js`).

## Configuration

-  Django settings live in `MyProject/settings.py`. For local development, confirm `DEBUG = True` and that `ALLOWED_HOSTS` includes `localhost` if necessary.
-  Media files are stored in `media/` (course images, profile pics). The `MEDIA_ROOT` and `MEDIA_URL` settings control this.
-  The Node.js signaling server is in `webrtc-node-app/server.js` and listens on the port defined there (default: 3000). Update client-side connection URLs if you change the port.

## Running tests

This project includes some tests in the app folders (for example: `courses/tests.py`, `notes/tests.py`, `users/tests.py`). Run Django tests with:

```powershell
python manage.py test
```

Add or update tests as you modify behavior. Aim for small, focused unit tests for models and views.

## Contributing

Contributions are welcome. A simple workflow:

1. Fork the repository.
2. Create a feature branch (git checkout -b my-feature).
3. Make changes and add tests where relevant.
4. Run the test suite locally (python manage.py test).
5. Submit a pull request with a clear description of your changes.

Please follow these guidelines:

-  Keep changes focused and well-tested.
-  Use existing style and naming conventions in the project.
-  Don't commit secrets or production credentials.

## Development notes

-  Static assets are in `static/` and templates in `templates/`.
-  The Node.js signaling server is intentionally minimal for demo use. For production, consider adding authentication, HTTPS/WSS, and better error handling.

## Known issues

-  The WebRTC signaling server does not provide authentication out of the box — use only for local development or behind a secure network.
-  Some templates and forms may be simplified for the course demo and can be hardened for production.

## License

This project doesn't include an explicit license in the repository. If you plan to share or accept contributions, consider adding an open-source license (for example, MIT or Apache-2.0). Add a `LICENSE` file at the project root.

## Contact

If you have questions or want to report issues, open an issue on the repository or contact the maintainer.
