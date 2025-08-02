# plc.py
import snap7
from snap7.util import get_bool, set_bool
import psycopg2

class SiemensPlc:
    def __init__(self, ip='192.168.0.1', rack=0, slot=1):
        self.ip = ip
        self.rack = rack
        self.slot = slot
        self.connected = False
        self.connect()

    def connect(self):
        try:
            self.plc = snap7.client.Client()
            self.plc.connect(self.ip, self.rack, self.slot)
            self.connected = True
            print(f"✅Connected to PLC at {self.ip}")
        except Exception as e:
            print(f"❌PLC connection failed: {e}")
            self.connected = False

    def log_event(self, event_type, db, start, byte, bit, value):
        try:
            conn = psycopg2.connect(
                dbname="plc_logs",
                user="postgres",
                password="postgres123",  #  PostgreSQL password
                host="localhost",
                port=5432
            )
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO plc_events (event_type, db_number, start, byte_offset, bit_offset, value)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (event_type, db, start, byte, bit, value))
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print(f"❌ Failed to log to DB: {e}")

    def read_bool(self, db_number, start, byte_offset, bit_offset):
        data = self.plc.db_read(db_number, start, 4)
        value = get_bool(data, byte_offset, bit_offset)
        self.log_event("read", db_number, start, byte_offset, bit_offset, value)
        return value

    def write_bool(self, db_number, start, byte_offset, bit_offset, value):
        data = self.plc.db_read(db_number, start, 4)
        set_bool(data, byte_offset, bit_offset, value)
        self.plc.db_write(db_number, start, data)
        self.log_event("write", db_number, start, byte_offset, bit_offset, value)
