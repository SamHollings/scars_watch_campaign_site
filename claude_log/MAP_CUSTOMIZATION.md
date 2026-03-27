# Map Customization Guide

## Adding New Interactive Locations

To add new clickable regions to the map, edit the `mapData.locations` array in `templates/red_scar_overview.html`.

### Location Object Format

```javascript
{
    name: 'Location Name',           // Display name shown on map
    x: 0.49,                         // X position as percentage (0.0 to 1.0)
    y: 0.53,                         // Y position as percentage (0.0 to 1.0)
    radius: 30,                      // Size of clickable area in pixels
    description: 'Hover text here',  // Text shown on hover
    action: 'fluff'                  // Action on click (currently 'fluff')
}
```

### Example: Adding Three Locations

```javascript
const mapData = {
    imageUrl: '{{ image_url }}',
    locations: [
        {
            name: 'Scars Watch',
            x: 0.49,
            y: 0.53,
            radius: 30,
            description: 'Strategic command center. Click to view battle reports.',
            action: 'fluff'
        },
        {
            name: 'Northern Outpost',
            x: 0.65,
            y: 0.25,
            radius: 25,
            description: 'Northern defense line. Monitor enemy positions.',
            action: 'fluff'
        },
        {
            name: 'Research Facility',
            x: 0.35,
            y: 0.75,
            radius: 28,
            description: 'Advanced weapons and technology development.',
            action: 'fluff'
        }
    ]
};
```

## Finding Correct Coordinates

### Method 1: Browser Developer Tools
1. Open the map in your browser
2. Right-click on the map canvas and select "Inspect"
3. Click on the canvas element in DevTools
4. In the console, type: `console.log('Canvas dimensions:', canvas.width, canvas.height)`
5. Move your mouse over the map and note the pixel positions
6. Calculate percentage: `x_percentage = pixel_x / canvas.width`

### Method 2: Trial and Error
1. Start with approximate percentages
2. Open the app in browser
3. Use browser DevTools console to monitor hover events
4. Adjust coordinates until they're in the right spot
5. Refresh to see changes (with debug enabled)

### Method 3: Image Editor
1. Open the map image in an image editor (Photoshop, GIMP, etc.)
2. Note the image dimensions
3. Use the eyedropper/measurement tools to find positions
4. Calculate percentages based on image dimensions

## Styling Customization

### Change Circle Color
In `templates/red_scar_overview.html`, find the circle drawing code:
```javascript
ctx.strokeStyle = '#ffd700';  // Change this to desired color
```

### Change Hover Tooltip Color
```javascript
ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';  // Background color
ctx.fillStyle = '#ffd700';               // Text color
```

### Adjust Circle Size
Increase the `radius` value in a location object:
```javascript
radius: 50  // Larger circle
```

### Change Theme Colors
Edit the CSS variables in `<style>` section:
- `#ffd700` - Gold color (primary)
- `#1a1a2e` - Dark background
- `#16213e` - Gradient color

## Adding Custom Actions

Currently, locations can only navigate to the fluff generator. To add other actions:

1. Modify the action handler in JavaScript:
```javascript
function handleLocationClick(location) {
    if (location.action === 'fluff') {
        navigateToFluff();
    } else if (location.action === 'map-detail') {
        window.location.href = '/location-detail/' + location.name;
    }
}
```

2. Add new action types to location objects:
```javascript
{
    name: 'New Location',
    x: 0.5,
    y: 0.5,
    radius: 30,
    description: 'Click for details',
    action: 'map-detail'
}
```

3. Create corresponding Flask routes in `app.py`

## Performance Tips

- Keep `radius` values between 20-50 pixels for best usability
- Limit to 10-15 locations for smooth performance
- Use descriptive names (they're visible on the map)
- Test on mobile devices to ensure touch areas are adequate

## Testing Your Changes

1. Edit `templates/red_scar_overview.html`
2. Save the file
3. Refresh the browser (Flask dev server auto-reloads)
4. Hover over new locations to test
5. Click to verify navigation works

## Troubleshooting

### Location Not Appearing
- Check coordinates are between 0.0 and 1.0
- Ensure `name` property is set
- Verify `radius` is greater than 0
- Check browser console for JavaScript errors

### Circle in Wrong Position
- Review calculated percentage values
- Remember: (0, 0) is top-left, (1, 1) is bottom-right
- Use browser DevTools to debug coordinates

### Hover Text Not Showing
- Check `description` property is set
- Verify CSS `display: none` isn't being overridden
- Check for JavaScript errors in console

## Advanced: Dynamic Locations

To load locations from a backend API:

```javascript
// In app.py
@app.route('/api/locations')
def get_locations():
    return jsonify([
        {'name': 'Scars Watch', 'x': 0.49, 'y': 0.53, ...}
    ])

// In HTML template
fetch('/api/locations')
    .then(r => r.json())
    .then(locations => {
        mapData.locations = locations;
        resizeCanvas();
    });
```
