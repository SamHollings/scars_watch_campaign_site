from flask import Flask, render_template, jsonify
from flask import render_template_string

app = Flask(__name__)

# Data: In a real app, this could come from a database
# Coordinates (y, x) are based on the image pixels
points_of_interest = [
    {
        "id": 1,
        "name": "The Core",
        "coords": [447, 424],
        "info": "This is the densest part of the nebula, where stars are born."
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>Red Scar Region Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        body { margin: 0; background: #0a0a0a; color: white; font-family: sans-serif; }
        #map { height: 80vh; width: 100%; background: #000; }
        #info-panel { padding: 20px; background: #1a1a1a; border-top: 2px solid #333; height: 20vh; }
        h1 { color: #ff4d4d; margin: 0 0 10px 0; font-size: 24px; }
    </style>
</head>
<body>

    <div id="map"></div>
    <div id="info-panel">
        <h1 id="poi-name">Red Scar Explorer</h1>
        <p id="poi-desc">Click on a point of interest to reveal data.</p>
    </div>

    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        // 1. Setup Map with Simple CRS
        var map = L.map('map', {
            crs: L.CRS.Simple,
            minZoom: -1,
            maxZoom: 2
        });

        // 2. Define Image Dimensions (1024x1024)
        var bounds = [[0, 0], [1024, 1024]];
        
        // 3. Load your local image
        // Note: url_for handles the spaces in the filename automatically
        var image = L.imageOverlay("{{ url_for('static', filename='red scar region.png') }}", bounds).addTo(map);

        // 4. Center the view
        map.fitBounds(bounds);

        // 5. Load POIs
        fetch('/api/poi')
            .then(res => res.json())
            .then(data => {
                data.forEach(poi => {
                    var marker = L.marker(poi.coords).addTo(map);
                    marker.on('click', function() {
                        document.getElementById('poi-name').innerText = poi.name;
                        document.getElementById('poi-desc').innerText = poi.info;
                    });
                });
            });

        // HELPER: Log coordinates to console when clicking
        // Use this to find the exact [y, x] for your POIs!
        map.on('click', function(e) {
            console.log("Clicked Coordinates: [" + e.latlng.lat.toFixed(0) + ", " + e.latlng.lng.toFixed(0) + "]");
        });
    </script>
</body>
</html>"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/poi')
def get_poi():
    return jsonify(points_of_interest)

if __name__ == '__main__':
    app.run(debug=True)