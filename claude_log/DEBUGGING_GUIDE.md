# Debugging Guide - Map Issues

## Issue: Map tooltips and sidebar not working in GitHub Codespaces

### What Was Fixed

1. **Event Data Format** - Fixed events array to use proper object format
   - Before: `['String event 1', 'String event 2']`
   - After: `[{date: '999.M41', title: 'Event', details: 'Description'}, ...]`

2. **Error Handling** - Added try-catch and fallback for mixed event formats

3. **Debugging Logging** - Added console.log statements throughout the code

### How to Debug in Codespaces

#### Step 1: Open Browser Developer Tools
1. Press `F12` or right-click → "Inspect"
2. Go to the **Console** tab
3. Look for log messages starting with "Map initialization..."

#### Step 2: Check Console Output

Expected output should show:
```
Map initialization started
Canvas element: <canvas>
Map locations: 5
Drawing clickable regions. Canvas size: 900 x 675
Location 0 (Scars Watch): pixel coords (441, 357.75)
Location 1 (Phlegmus): pixel coords (585, 236.25)
...
Canvas event listeners attached
Page fully loaded
All event listeners initialized
```

#### Step 3: Test Map Interaction

1. **Test Hover:**
   - Move mouse over a location circle on the map
   - Cursor should change from `crosshair` to `pointer`
   - Tooltip with location name should appear

2. **Test Click:**
   - Click on a location circle
   - Sidebar should slide in from the right
   - Sidebar should show location name, backstory, and events

3. **Open Developer Console while hovering:**
   - You should see distance calculations in console
   - When hovering over location, you'll see the tooltip position updates

### Debugging Specific Issues

#### Tooltips Not Showing
**Symptoms:** Cursor changes but no tooltip appears

**Debug steps:**
1. Open Console (F12)
2. Hover over a location
3. Check for errors in console
4. Look for `showLocationInfo` being called
5. Check `locationInfo` element exists:
   ```javascript
   console.log(document.getElementById('locationInfo'))
   ```

**Fix:**
- Make sure `#locationInfo` div exists in HTML
- Check CSS `.location-info` has `display: block` when visible

#### Sidebar Not Opening
**Symptoms:** Click works but sidebar doesn't slide in

**Debug steps:**
1. Open Console (F12)
2. Click on a location
3. Should see: `"Showing sidebar for location: [name]"`
4. Check if error message appears
5. Verify sidebar element:
   ```javascript
   console.log(document.getElementById('sidebar'))
   ```

**Fix:**
- Check `#sidebar` element exists in HTML
- Verify CSS has `.sidebar.open` class with `right: 0`
- Make sure location events are properly formatted

#### Console Shows Errors
**If you see errors, note the line number and check:**

1. **Syntax errors** - Check for missing quotes, brackets
2. **Reference errors** - Check DOM elements exist
3. **Type errors** - Check data types match expectations

### Manual Testing

**Test in Console:**
```javascript
// Check map data
console.log(mapData.locations[0])

// Manually show sidebar
showLocationSidebar(mapData.locations[0])

// Check canvas size
console.log('Canvas:', canvas.width, 'x', canvas.height)

// List all clickable regions
console.log(clickableRegions)
```

### Network Issues (Codespaces Specific)

If the map image fails to load:

1. Check browser console for image loading errors
2. Verify the image path is correct: `/static/red scar region.png`
3. In Codespaces, static files should be served correctly
4. If image fails, the map shows placeholder with circles

### Performance Issues

If the map is slow or unresponsive:

1. **Check canvas size:**
   ```javascript
   console.log('Canvas:', canvas.width, 'x', canvas.height)
   ```

2. **Monitor mouse events:** They fire on every movement - this is normal

3. **Check number of locations:** More locations = more distance calculations

### Codespaces-Specific Checks

1. **Port forwarding:**
   - Make sure port 5000 is forwarded in Codespaces
   - Check Ports tab shows "Flask App"

2. **Network latency:**
   - Codespaces may have slight delays
   - Hover/click should still work, just potentially slower

3. **Browser console access:**
   - Press `Ctrl+Shift+J` (Windows/Linux) or `Cmd+Option+J` (Mac)
   - Or F12 and click Console tab

### Reset / Force Refresh

If things seem stuck:

1. **Hard refresh:** `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
2. **Clear cache:** In DevTools → Application → Clear storage
3. **Restart Flask app:** Stop and restart `python app.py`

### Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| No tooltip on hover | Coordinates out of range | Check canvas size matches image |
| Sidebar won't close | CSS issue | Check `.sidebar.open` class and `right` property |
| Events not showing in sidebar | Wrong event format | Ensure events are objects with `date`, `title`, `details` |
| Canvas is blank | Image failed to load | Check `/static/red scar region.png` exists |
| Click not working | Event listeners not attached | Check `window.addEventListener('load', ...)` fires |

### Reporting Issues

When reporting issues, include:

1. **Console output** - Copy from DevTools Console tab
2. **Screenshot** - Show what appears on screen
3. **Steps to reproduce** - Exact actions taken
4. **Browser & OS** - What browser/operating system
5. **Error messages** - Any error text from console

### Live Code Inspection

In browser Console, you can:

```javascript
// Inspect a specific location
mapData.locations.find(l => l.name === 'Scars Watch')

// Check sidebar position
document.getElementById('sidebar').offsetLeft

// Force sidebar to open
document.getElementById('sidebar').classList.add('open')

// Force sidebar to close
document.getElementById('sidebar').classList.remove('open')

// Inspect clickable regions
clickableRegions.map(r => ({ name: r.location.name, x: r.x, y: r.y }))
```

### Getting Help

When stuck:
1. Open DevTools Console (F12)
2. Try the manual tests above
3. Look for any error messages (red text in console)
4. Check the log messages show proper initialization
5. Verify DOM elements exist with `document.getElementById()`
