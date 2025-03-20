from http.server import BaseHTTPRequestHandler
import json

from utils.predict import predict

class handler(BaseHTTPRequestHandler):

    def get_song_id(self) -> str: 
        return self.path.split("/")[-1]

    def do_GET(self):
        song_id = self.get_song_id()

        if song_id:
            try: 
                result = predict(song_id)

                response = {
                    "result": result
                }

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
            except Exception:
                response = {
                    "error": "Spotify Endpoint has been deprecated"
                }

                self.send_response(500)
                self.send_header('Content-Type', "application/json")
                self.end_headers()
        else:
            self.send_response(400)
            self.send_header("Content-Type", 'application/json')
            self.end_headers()

            response = {
                "error": "Song ID not provided."
            }

        self.wfile.write(json.dumps(response).encode())

