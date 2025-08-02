# Siemens-S7-1500-PLC-Web-Control
with Flask + Snap7 + PostgreSQL + PLCSIM Advanced (VM) Control a Siemens S7-1500 PLC virtually using a web interface built with Python Flask. Data is exchanged using Snap7, and all PLC read/write events are logged in a PostgreSQL database. Ideal for automation technicians and developers working with PLCs and SCADA systems.
✅ Features
🔌 Connect to S7-1500 PLC (real or simulated)

🧠 Read/Write booleans in PLC DB (data block)

🌐 Web interface with Start & Stop buttons

🗃️ PostgreSQL database logs each event (read/write)

⚙️ Works with Siemens PLCSIM Advanced in VMware!

| Tool                            | Role                                                 |
| ------------------------------- | ---------------------------------------------------- |
| 🧠 **Siemens S7-1200**          | PLC logic execution                                  |
| 🧪 **PLCSIM Advanced**          | PLC simulator running on VMware                      |
| 💻 **VMware**                   | Virtual machine for simulating PLC (bridged network) |
| 🌐 **Flask**                    | Backend web server (REST API + Web UI)               |
| 🔌 **Snap7**                    | Python library for S7 PLC communication              |
| 🗃️ **PostgreSQL**              | Database for logging read/write events               |
| 📮 **Postman**                  | API testing                                          |
| 🛠️ **Visual Studio Code**      | Code editor for Python & Flask development           |
| 🔁 **Virtual Ethernet Adapter** | From PLCSIM Advanced (bridged for communication)     |

🖥️ Architecture Overview
[Postman or Web UI]
       |
    [Flask API]
       |
   [Snap7 Client]
       |
  [VMware Network Adapter (Bridged)]
       |
 [PLCSIM Advanced PLC] ←→ S7-1200 Logic
       |
  [Log Read/Write in PostgreSQL]
  
📁 Project Structure
flask_snap7_project/
├── app.py              # Flask server (routes)
├── plc.py              # PLC connection & DB logger
├── templates/
│   └── index.html      # Web interface
└── README.md


⚙️ Installation & Setup
1. Install Software
On your host PC:

Python 3.10 ✅

Snap7 (python-snap7)

Flask (pip install flask)

PostgreSQL (create plc_logs DB)

Postman (for API testing)

Visual Studio Code (or any editor)

In your VMware (Windows VM):

PLCSIM Advanced

TIA Portal (with S7-1200 project)

Set network adapter to Bridged Mode

Use PLC Virtual Ethernet Adapter
2. Create the PostgreSQL Table

CREATE DATABASE plc_logs;

CREATE TABLE plc_events (
    id SERIAL PRIMARY KEY,
    event_type TEXT,
    db_number INT,
    start INT,
    byte_offset INT,
    bit_offset INT,
    value BOOLEAN,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

3. Run the Flask App
python app.py
🔁 API Usage
Read from PLC:
GET /read?db=10&start=0&byte=2&bit=0
Write to PLC:
POST /write
Content-Type: application/json

{
  "db": 10,
  "start": 0,
  "byte": 2,
  "bit": 0,
  "value": true
}

5. 
