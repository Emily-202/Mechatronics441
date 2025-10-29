from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import RPi.GPIO as GPIO
import urllib.parse
import time

GPIO.setmode(GPIO.BCM)

## Problem 1 ---------------------------------------------------------------------------------
ledPins = {'LED1': 17, 'LED2': 27, 'LED3': 22}
for p in ledPins.values():
    GPIO.setup(p, GPIO.IN)

pwms = {}
for name, pin in ledPins.items():
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 1000)  # 1 kHz PWM
    pwm.start(0)
    pwms[name] = pwm

brightness = {'LED1': 0, 'LED2': 0, 'LED3': 0}

def generateOneHTML():
    table_rows = "".join([
        f"<tr><td>{led}</td><td>{brightness[led]}%</td></tr>"
        for led in brightness
    ])
    html = f"""
        <html>
        <head><title>LED Brightness Control</title></head>
        <body style="font-family: Arial; margin: 30px;">
            <form action="/" method="POST">
                <p><b>Brightness level:</b><br>
                    <input type="range" name="brightness" min="0" max="100" value="50">
                </p>
                <p><b>Select LED:</b><br>
                    <input type="radio" name="led" value="LED1" checked> LED 1 <label>({brightness['LED1']}%)</label><br>
                    <input type="radio" name="led" value="LED2"> LED 2 <label>({brightness['LED2']}%)</label><br>
                    <input type="radio" name="led" value="LED3"> LED 3 <label>({brightness['LED3']}%)</label><br>
                </p>
                <input type="submit" value="Change Brightness">
            </form>
        </body>
        </html>
        """
    return html.encode("utf-8")


# Web Server Handler Class
class LEDRequestHandlerOne(BaseHTTPRequestHandler):
    def do_GET(self):
        # initial page load
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(generateOneHTML())

    def do_POST(self):
        # Handle POST data from form submission
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        params = urllib.parse.parse_qs(post_data.decode('utf-8'))

        # Extract LED name and brightness value
        selected_led = params.get('led', ['LED1'])[0]
        new_brightness = int(params.get('brightness', [0])[0])

        # Update PWM duty cycle and record brightness
        brightness[selected_led] = new_brightness
        pwms[selected_led].ChangeDutyCycle(new_brightness)

        # Send updated page back to client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(generateOneHTML())
    
    def runServer():
        try:
            print("Starting server on port 8080...")
            server_address = ('', 8080)
            httpd = HTTPServer(server_address, LEDRequestHandlerOne)
            print("Server running. Access from browser via http://<raspberrypi_ip>:8080")
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            print("Cleaning up GPIO...")
            for pwm in pwms.values():
                pwm.stop()
            GPIO.cleanup()

"""
# Running the program
if __name__ == "__main__":
    LEDRequestHandlerOne.runServer()
"""

## Problem 2 ---------------------------------------------------------------------------------

def generateTwoHTML():
    table_rows = "".join([
        f"<tr><td>{led}</td><td>{brightness[led]}%</td></tr>"
        for led in brightness
    ])
    html = f"""
        <html>
        <head><title>LED Brightness Control</title></head>
        <body style="font-family: Arial; margin: 30px;">
            <form action="/" method="POST">
                <p>
                    <input type="range" name="brightness1" min="0" max="100" value="50"> <label>({brightness['LED1']})</label>
                    <input type="range" name="brightness2" min="0" max="100" value="50"> <label>({brightness['LED2']})</label>
                    <input type="range" name="brightness3" min="0" max="100" value="50"> <label>({brightness['LED3']})</label>
                </p>
            </form>
        </body>
        </html>
        """
    return html.encode("utf-8")

class LEDRequestHandlerTwo(BaseHTTPRequestHandler):
    def do_GET(self):
        # initial page load
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(generateTwoHTML())

    def do_POST(self):
        # Handle POST data from form submission
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        params = urllib.parse.parse_qs(post_data.decode('utf-8'))

        # Extract LED name and brightness value
        selected_led = params.get('led', ['LED1'])[0]
        new_brightness = int(params.get('brightness', [0])[0])

        # Update PWM duty cycle and record brightness
        brightness[selected_led] = new_brightness
        pwms[selected_led].ChangeDutyCycle(new_brightness)

        # Send updated page back to client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(generateTwoHTML())
    
    def runServer():
        try:
            print("Starting server on port 8080...")
            server_address = ('', 8080)
            httpd = HTTPServer(server_address, LEDRequestHandlerTwo)
            print("Server running. Access from browser via http://<raspberrypi_ip>:8080")
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            print("Cleaning up GPIO...")
            for pwm in pwms.values():
                pwm.stop()
            GPIO.cleanup()

if __name__ == "__main__":
    LEDRequestHandlerTwo.runServer()