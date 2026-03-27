# Sidebar Location Details & Characters Page

Summary of the latest UI improvements for the Red Scar campaign interface.

## ✨ What's New

### 1. **Location Sidebar (Instead of New Page)**

**Before:** Clicking a location opened a new page
**After:** Location details appear in a slide-out sidebar

**Features:**
- 📍 Location name in header
- 📖 Full backstory text
- ⏰ Timeline of key events
- Smooth slide animation from right
- Close with × button or Escape key
- Works on mobile (full width)

**How to Use:**
1. Click any location on the map
2. Sidebar slides out from the right
3. Read backstory and events
4. Click × or press Escape to close

### 2. **Baal Moved to Edge**

The Baal location (Blood Angels homeworld) has been repositioned:
- **Old Position:** Center-left (0.35, 0.25)
- **New Position:** Far left edge (0.08, 0.15)
- Now clearly shows it's beyond the Red Scar region
- Still clickable and accessible

### 3. **Characters of the Red Scar Page**

**New Route:** `/characters`
**Button:** Purple button on map labeled "👥 Characters of the Red Scar"

**Characters Included:**

#### Imperial Forces 🦅
- **Watch Master Sanguone** - Commander of Scars Watch
  - Deathwatch leader
  - Former Watch Captain at Talasa Prime
  - Expert in Tyranid warfare

- **Commander Dante** - Chapter Master of Blood Angels
  - Legendary defender of Baal
  - Recommended Deathwatch presence

- **Lord Roboute Guilliman** - Lord Commander of Imperium
  - Primarch and strategic visionary
  - Co-recommended Watch Fortress creation

#### Chaos Forces ☠️
- **The Apostles of Contagion** - Nurgle Warband
  - Plague-focused Chaos faction
  - Rules Phlegmus
  - Conducts biological warfare

- **The Biologian Collective** - Masters of Plague
  - Leadership caste of Apostles
  - Creates new diseases
  - Operates laboratories across region

#### Xenos Threats 🐛
- **Hive Fleet Leviathan** - Tyranid Swarm
  - Besieged Baal in 999.M41
  - Splinter fleets still active
  - Primary justification for Deathwatch

**Page Features:**
- Grid layout of character cards
- Organized by faction
- Each card includes:
  - Character/faction name
  - Title/role
  - Faction badge
  - Description
  - Background information
- Responsive design (stacks on mobile)
- Back button to return to map

## 🎨 Visual Design

### Sidebar
- **Color:** Dark background with gold header
- **Animation:** Slides in from right (0.3s)
- **Width:** 450px desktop, 100% mobile
- **Scrollable:** Full event list visible
- **Z-Index:** 999 (above everything but modals)

### Characters Page
- **Grid Layout:** Auto-fit columns (300px min)
- **Colors:**
  - Imperial: Gold/Blue theme
  - Chaos: Orange/Red theme
  - Xenos: Purple theme
- **Cards:** 3D hover effect with shadow
- **Responsive:** Single column on mobile

## 🔧 Implementation Details

### Modified Files
- `templates/red_scar_overview.html`
  - Added sidebar HTML and CSS
  - Updated location click handler
  - Added character button
  - Modified JavaScript event handlers

- `app.py`
  - Added `/characters` route

- `templates/characters.html` (NEW)
  - Full character gallery page
  - Faction-based organization
  - Detailed character descriptions

### CSS Classes

**Sidebar:**
- `.sidebar` - Container
- `.sidebar.open` - Active state
- `.sidebar-header` - Title bar
- `.sidebar-content` - Main content
- `.sidebar-event` - Event card
- `.sidebar-event-date` - Event date
- `.sidebar-event-title` - Event title
- `.sidebar-event-details` - Event description

**Character Cards:**
- `.character-card` - Main card container
- `.character-name` - Character name
- `.character-title` - Role/position
- `.role-badge` - Faction badge
- `.character-faction` - Faction info box
- `.character-description` - Main description
- `.character-background` - Background info

## 📱 Responsive Behavior

### Desktop (1024px+)
- Sidebar: 450px width, slides from right
- Characters: 3-column grid
- Full detail display

### Tablet (768px-1024px)
- Sidebar: 350px width
- Characters: 2-column grid
- Adjusted padding

### Mobile (< 768px)
- Sidebar: Full width (100%)
- Characters: Single column
- Touch-friendly spacing

## 🎯 User Flow

### Viewing Location Details
```
Map page
  ↓ (click location)
Sidebar opens with:
  - Location name
  - Full backstory
  - Event timeline
  ↓ (click ×, Escape, or click map)
Sidebar closes
```

### Viewing Characters
```
Map page
  ↓ (click "Characters" button)
Characters page
  ↓ (read character info)
  ↓ (click back button)
Return to map
```

## ✅ Features

✨ **Sidebar Benefits**
- Non-intrusive (doesn't leave page)
- Quick access without navigation
- Mobile-friendly
- Keyboard accessible (Escape to close)
- Auto-scrolls through events

✨ **Characters Page Benefits**
- Comprehensive faction overview
- Context for story and map
- Detailed character backgrounds
- Visual hierarchy with colors
- Mobile responsive

✨ **UX Improvements**
- Location click → sidebar (faster, cleaner)
- Dedicated characters section
- Better content organization
- Consistent styling
- Improved accessibility

## 🔮 Future Enhancements

Possible additions:
- [ ] Character relationships/alliances visualization
- [ ] Faction color-coding on map
- [ ] Character search/filter
- [ ] Mission briefings from characters
- [ ] Character stats/abilities
- [ ] Dynamic faction control display
- [ ] Character dialogue/quotes

## 📝 Notes

- Location detail page (`/location/`) still exists but is no longer used
- Can be kept for direct linking or removed if not needed
- Sidebar position responsive: desktop right, tablet right (smaller), mobile full width
- All character information from `ongoing_story.txt`
- Baal positioned at map edge to visually indicate it's outside main region
