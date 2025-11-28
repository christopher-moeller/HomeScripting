# HomeScripting

HomeScripting is a personal smart home automation platform that allows you to create, upload, and run Python scripts via a web interface. The platform provides a Flask backend API and a React + TypeScript frontend, enabling seamless interaction with smart home devices on your local network.

---

## Features

* **Python Backend (Flask)**: Serves API under `/api`, hosts the React frontend, executes user-uploaded Python scripts securely, and provides smart home interfaces (Philips Hue, Bosch, etc.) automatically.
* **Frontend (React + TypeScript)**: Intuitive web interface to upload and manage scripts, start, stop, and monitor scripts in real-time, and view/control smart home devices manually.
* **Smart Home Integration**: Automatic discovery and connection to supported devices; provides Python APIs to interact with devices directly in scripts.
* **Script Management**: Upload scripts via the web interface, run scripts on demand or schedule them, and define scripts in a structured format for execution.

---

## Project Structure

```
HomeScripting/
├── backend/             # Flask API and script execution logic
│   ├── app.py           # Main Flask application
│   ├── api/             # API endpoints
│   ├── scripts/         # Uploaded user scripts
│   └── smart_home/      # Device interfaces (Philips Hue, Bosch, etc.)
├── frontend/            # React + TypeScript app
│   ├── src/             # React source code
│   └── public/          # Static files like index.html
├── README.md
└── requirements.txt
```

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/christopher-moeller/HomeScripting.git
cd HomeScripting
```

2. **Backend setup**:

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

3. **Frontend setup**:

```bash
cd ../frontend
npm install
npm start
```

---

## Usage

1. Open the frontend in your browser (usually at `http://localhost:3000`).
2. Upload your Python scripts through the web interface.
3. Execute scripts directly from the interface.
4. Use the provided Python smart home interfaces (`home`) to control and interact with devices in your scripts.

---

## Script Structure

Each script should follow a defined structure to be executable by HomeScripting. Example:

```python
# my_script.py
def main(home):
    # `home` is a provided object with smart home device interfaces
    home.lights.turn_on("Living Room")
    home.bosch.thermostat.set_temperature(22)
```

* `main` function is the entry point.
* `home` object provides access to all connected smart home devices.

---

## Architecture Overview

```
+---------------------+
|     React Frontend  |
|  (TypeScript, UI)  |
+---------------------+
          |
          v
+---------------------+
|     Flask Backend   |
|  /api endpoints     |
|  Script Executor    |
+---------------------+
          |
          v
+---------------------+
| Smart Home Devices  |
| (Philips Hue, Bosch)|
+---------------------+
```

* The **frontend** communicates with the **Flask backend** via `/api`.
* Scripts uploaded by users are executed by the backend.
* Backend provides device interfaces automatically, allowing scripts to control smart home devices.

---

## Quick Start Example Script

```python
# turn_on_evening_lights.py
def main(home):
    if home.time.is_evening():
        home.lights.turn_on("Living Room")
        home.lights.set_brightness("Living Room", 50)
        home.bosch.thermostat.set_temperature(21)
```

* This script automatically turns on living room lights and sets the thermostat in the evening.
* You can upload it to HomeScripting via the web UI and execute it manually or schedule it.

---

## Contributing

Contributions are welcome! You can:

* Add new device interfaces.
* Improve script management or execution security.
* Enhance the frontend with additional features.

Please fork the repository, create a feature branch, and submit a pull request.

---

## License

[MIT License](LICENSE)
