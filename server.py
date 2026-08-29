#!/usr/bin/env python3
"""
HourSpot - Smart AI-Powered Parking Platform Server
Provides static web hosting and RESTful API endpoints for AI parking recommendation & demand prediction.
"""

import http.server
import socketserver
import json
import urllib.parse
import os
import sys

PORT = int(os.environ.get("PORT", 8000))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# In-memory database of mock parking spaces
SPACES = [
    {
        "id": "sp-1",
        "name": "Sri Venkateswara Temple North Gate - Sharma Villa",
        "type": "house",
        "address": "Plot 14, Hill Shrine Road, Temple North Gate",
        "zone": "temple",
        "lat": 13.6833,
        "lng": 79.3475,
        "distanceMeters": 140,
        "walkTimeMin": 2,
        "pricePerHour": 40,
        "originalPrice": 40,
        "vehicleTypes": ["car", "bike"],
        "rating": 4.95,
        "reviewsCount": 128,
        "totalSlots": 4,
        "availableSlots": 2,
        "facilities": {"cctv": True, "guard": True, "covered": True, "ev": True},
        "hostName": "Mr. R. Sharma (House Owner)",
        "photoUrl": "https://images.unsplash.com/photo-1584463699039-444454790b8f?auto=format&fit=crop&w=600&q=80",
        "aiScore": 98,
        "aiReasons": ["140m walk to Temple entry", "Covered roof + 24/7 CCTV", "30% cheaper than public lot"]
    },
    {
        "id": "sp-2",
        "name": "Green Pines House Driveway",
        "type": "house",
        "address": "42 Misty Pine Lane, Upper Hill Station",
        "zone": "hillstation",
        "lat": 13.6860,
        "lng": 79.3510,
        "distanceMeters": 280,
        "walkTimeMin": 4,
        "pricePerHour": 35,
        "originalPrice": 35,
        "vehicleTypes": ["car", "bike"],
        "rating": 4.88,
        "reviewsCount": 94,
        "totalSlots": 3,
        "availableSlots": 1,
        "facilities": {"cctv": True, "guard": False, "covered": True, "ev": False},
        "hostName": "Anita Menon",
        "photoUrl": "https://images.unsplash.com/photo-1590674899484-d5640e854abe?auto=format&fit=crop&w=600&q=80",
        "aiScore": 94,
        "aiReasons": ["Scenic mountain view", "Zero waiting queue", "Spacious SUV parking"]
    }
]

class HourSpotHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        # API: Get spaces
        if parsed.path == '/api/spaces':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "data": SPACES}).encode('utf-8'))
            return
            
        # API: Demand prediction
        elif parsed.path == '/api/ai/demand':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            forecast = {
                "zone": "temple",
                "demandLevel": "PEAK",
                "surgeMultiplier": 1.25,
                "peakHour": "18:00",
                "occupancyRate": 0.94,
                "hourlyForecast": [
                    {"hour": 6, "demand": 25},
                    {"hour": 9, "demand": 60},
                    {"hour": 12, "demand": 45},
                    {"hour": 15, "demand": 70},
                    {"hour": 18, "demand": 98},
                    {"hour": 20, "demand": 85},
                    {"hour": 22, "demand": 40},
                    {"hour": 24, "demand": 15}
                ]
            }
            self.wfile.write(json.dumps({"status": "success", "data": forecast}).encode('utf-8'))
            return
            
        # Default fallback to static file serving
        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len) if content_len > 0 else b'{}'
        
        try:
            payload = json.loads(post_body.decode('utf-8'))
        except Exception:
            payload = {}

        if parsed.path == '/api/bookings':
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {
                "status": "success",
                "bookingId": f"HS-{os.urandom(2).hex().upper()}",
                "message": "Booking reserved successfully",
                "qrToken": f"QR-{os.urandom(4).hex()}"
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return

        elif parsed.path == '/api/spaces':
            payload["id"] = f"sp-{len(SPACES)+1}"
            SPACES.append(payload)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "data": payload}).encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()


def run_server():
    print(f"🚀 Starting HourSpot Platform Server on http://localhost:{PORT}")
    print(f"📁 Serving static files & APIs from {DIRECTORY}")
    with socketserver.TCPServer(("", PORT), HourSpotHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server gracefully...")
            httpd.server_close()

if __name__ == '__main__':
    run_server()
