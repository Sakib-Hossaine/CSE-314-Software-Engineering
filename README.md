# Django Project with WebRTC Integration

A Django web application with WebRTC functionality for real-time communication.

## ✨ Features

-  🛠 Django backend with user authentication, admin site, and user/profile management
-  📹 WebRTC integration for real-time video/audio communication (browser clients + Node.js signaling server)
-  📁 Course and notes management (create, read, update, delete) with templates and forms
-  🖼 Image upload support for courses and profile pictures (media handling)
-  🔐 Example payment views and templates and guidance for evolving to a full, SSL‑secured ecommerce flow (see Full functional sslecommerce)
-  ✅ Basic test coverage included for core apps; encourages adding more unit/integration tests
-  📦 Static assets and templates included for quick local development
-  �️ Uses SQLite for local development; project can be configured to use PostgreSQL or another production-grade DB

## 🚀 Prerequisites

Before you begin, ensure you have met the following requirements (recommended):

-  Python 3.8+ (the project is compatible with Python 3.6+, but 3.8+ is recommended)
-  Node.js (LTS version) for the signaling server and any frontend tooling
-  npm (comes with Node.js)
-  Git
-  (Optional) mkcert or similar for local HTTPS testing when validating secure WebRTC/WSS and cookie behavior
-  (Recommended for production) PostgreSQL (or another production-grade database) and an object storage service for media (S3/Azure Blob)

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

## Full functional sslecommerce

This project contains example payment-related views and templates; the following guidance outlines how to evolve it into a full, SSL-secured ecommerce flow ("sslecommerce") suitable for production.

Key components you'll want to implement or verify:

-  TLS/SSL termination

   -  Use a trusted certificate (Let's Encrypt, commercial CA) on your public endpoint. If you deploy behind a reverse proxy (Nginx, Traefik) or a PaaS (Heroku, Azure Web Apps), terminate TLS there and proxy traffic to Django over HTTP on the internal network.
   -  For local testing, use mkcert or a dev proxy supporting HTTPS to exercise secure cookie flags and secure WebSocket (wss://) connections for WebRTC.

-  Payment gateway integration

   -  Choose a PCI-compliant gateway (Stripe, PayPal, Razorpay, etc.). Use their official SDK/server-side libraries inside Django to create payment intents and verify webhooks.
   -  Keep all sensitive keys out of source control. Use environment variables (for example via a `.env` file loaded by `django-environ`) or your deployment platform's secret management.

-  Django settings for ecommerce

   -  SECURITY
      -  Set `SECURE_SSL_REDIRECT = True` (only after properly configuring SSL in production).
      -  Set `SESSION_COOKIE_SECURE = True` and `CSRF_COOKIE_SECURE = True` so cookies are only sent over HTTPS.
      -  Set `SECURE_HSTS_SECONDS` (e.g., 63072000) and other HSTS settings once you confirm HTTPS is stable.
   -  Payment credentials
      -  Place API keys in environment variables and reference them in `MyProject/settings.py` (or use `django-environ`).
   -  Webhook endpoints
      -  Create a dedicated endpoint to receive and verify gateway webhooks (verify signatures). Keep it behind HTTPS and, if possible, restrict access by IP or use gateway-supplied signatures.

-  Media and static files

   -  Serve static files via CDN or the web server (Nginx). For media (user uploads), use a managed object store (S3, Azure Blob) for scalability and security. Ensure proper file validation when accepting uploads.

-  Secure WebRTC signaling

   -  Serve the signaling channel over WSS (secure WebSocket) so browsers will use secure transport when loaded over HTTPS. If the Node.js signaling server is behind a reverse proxy, enable proxying of WSS.

-  Testing and verification

   -  Run Django tests (`python manage.py test`) and add integration tests for checkout and webhook processing.
   -  Use the gateway's test mode and sample webhooks to verify end-to-end flows.
   -  Manually verify cookie flags, redirect behavior, and that all payment flows reject invalid data.

-  Deployment checklist
   -  Use environment-specific settings (separate production settings file or env var overrides).
   -  Ensure DEBUG=False in production and that `ALLOWED_HOSTS` is set correctly.
   -  Configure monitoring and alerting for payment failures and webhook processing errors.
   -  Perform a small canary rollout and review logs for errors before promoting to full traffic.

Security note: Payment systems are high-risk and regulated (PCI). For production deployments, prefer using the gateway's hosted checkout pages or follow their recommended methods to minimize PCI scope. If you accept card data on your servers, ensure you follow all compliance steps or consult a payment expert.

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
