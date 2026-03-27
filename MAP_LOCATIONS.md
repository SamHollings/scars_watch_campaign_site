# Red Scar Region - Interactive Map Locations

This document describes all locations available on the interactive map and their associated lore.

## Map Locations

### 1. 🏰 Scars Watch
**Type:** Deathwatch Fortress Fleet
**Position:** Center-West (0.49, 0.53)
**Status:** Imperial Control

**Description:**
The primary military stronghold in the Red Scar Region and headquarters of the Deathwatch Watch Fortress Fleet. A refitted Hecate Class Heavy Cruiser with escort vessels serving as operational bases.

**Key Facts:**
- Recommended by Lord Roboute Guilliman and Commander Dante
- Under command of Watch Master Sanguone
- Fleet comprises seasoned veterans
- Recently upgraded with new void shields

**Notable Events:**
- 899.M41 - Founded during Imperial expansion
- 956.M41 - Defended against Ork invasion
- 987.M41 - Hosted peace summit
- 999.M41 - Redesignated as Deathwatch Fortress
- 012.M42 - Void shield upgrades completed

---

### 2. ☠️ Phlegmus (Plague Planet)
**Type:** Chaos Stronghold
**Position:** Northeast (0.65, 0.35)
**Status:** Hostile - Nurgle Corruption

**Description:**
A hellish world saturated with disease and corruption. Ruled by the Apostles of Contagion, a warband of biologian cults devoted to Nurgle. The pools on this world create portals to the Garden of Nurgle itself.

**Key Facts:**
- Ruled by a caste of biologian engineers
- Creates new and varied plagues for biological warfare
- Warp portals to the Garden of Nurgle
- Nearly impenetrable due to toxic conditions
- Source of plague vectors spreading through the region

**Notable Events:**
- 987.M41 - Fell to Chaos forces
- 995.M41 - Organized as Apostles of Contagion warband
- 001.M42 - Plague vectors released to other worlds
- 011.M42 - Warp portal activity increasing

---

### 3. 🦠 Khajikes V (Plague World)
**Type:** Contaminated World
**Position:** South (0.52, 0.68)
**Status:** Hostile - Quarantine Zone

**Description:**
A once-minor Imperial colony transformed into a plague-ravaged death world through deliberate biological warfare. Plague victims from across the Red Scar accumulate here, their corpses creating overwhelming miasma of contamination.

**Key Facts:**
- Deliberately targeted by Apostles of Contagion
- Massive plague pits with thousands of corpses
- Toxic conditions prevent conventional intervention
- Living testament to Nurgle's "blessing"
- Source of secondary plague vectors

**Notable Events:**
- 956.M41 - Started as minor Imperial colony
- 998.M41 - First plague outbreak recorded
- 002.M42 - Overwhelmed by plague victims
- 010.M42 - Declared permanent quarantine zone

---

### 4. 🌫️ Weepmire
**Type:** Plague World / Biolab
**Position:** Northeast (0.72, 0.48)
**Status:** Hostile - Secondary Chaos Stronghold

**Description:**
A secondary plague world and experimental biolab under Nurgle's influence. The marshy terrain creates ideal conditions for disease proliferation and mutation. Functions as both proving ground for new bioweapons and fallback position for Chaos forces.

**Key Facts:**
- Marshy terrain ideal for plague development
- Experimental biologian cults operate here
- Linked to Phlegmus via Warp portal
- Contains archeotech and xenos biological materials
- Less contaminated than Phlegmus but equally dangerous

**Notable Events:**
- 989.M41 - Fell to Chaos corruption
- 996.M41 - First plague experiments begin
- 004.M42 - Warp portal to Phlegmus established
- 009.M42 - Xenos artifacts detected

---

### 5. 🩸 Baal
**Type:** Chapter Homeworld
**Position:** Northwest (0.35, 0.25)
**Status:** Imperial Control (Beyond Red Scar)

**Description:**
Sacred homeworld of the Blood Angels Space Marine Chapter, located beyond the immediate Red Scar Subsector. Its proximity and strategic importance make it vital to regional stability. Recently endured siege by Hive Fleet Leviathan.

**Key Facts:**
- Homeworld of the Blood Angels Chapter
- Commanded by Commander Dante
- Recently survived catastrophic Tyranid siege
- Tyranid splinter fleets still active in region
- Justified Deathwatch presence in Red Scar

**Notable Events:**
- 999.M41 - Besieged by Hive Fleet Leviathan
- 999.M41 - Blood Angels achieved victory at great cost
- 000.M42 - Commander Dante authorized Red Scar operations
- Current - Ongoing Tyranid splinter incursions

---

## Navigation on the Map

### Hovering Over Locations
When you hover over a location on the map:
1. A **golden circle** appears around the location
2. A **tooltip popup** shows:
   - **Location name** (bold title)
   - **Description** (one-line summary)

### Clicking on Locations
Clicking on any location opens its **Detail Page**, which includes:
- Full **backstory** narrative
- **Timeline of key events** with dates and descriptions
- Visual styling matching the campaign's Warhammer 40k aesthetic
- Navigation back to map and to fluff generator

### Adding More Locations

To add a new location to the map:

1. **Update `templates/red_scar_overview.html`:**
   ```javascript
   {
       id: 'location-id',          // Unique identifier (lowercase-dash)
       name: 'Location Name',       // Display name
       x: 0.50,                    // X position (0.0 to 1.0)
       y: 0.50,                    // Y position (0.0 to 1.0)
       radius: 25,                 // Hover circle size in pixels
       description: 'One-line description',
       backstory: 'Full backstory text...',
       events: [
           {date: '999.M41', title: 'Event title', details: 'Event details...'}
       ]
   }
   ```

2. **Update `app.py` locations_db:**
   Add corresponding location data in the `locations_db` dictionary with full details.

3. **Test by hovering and clicking:**
   - Hover should show tooltip
   - Click should navigate to detail page

## Lore Context

The Red Scar Subsector is a relatively lawless region of space around the Baal system. It experiences:
- High levels of poisonous stellar radiation
- Difficult colonization conditions
- Known archeotech caches
- Post-Siege of Baal Tyranid activity
- Recent Chaos expansion (Nurgle cults)

The establishment of the Deathwatch Watch Fortress was designed to:
- Protect Baal and Imperial interests
- Counter Tyranid remnants
- Combat Chaos expansion
- Stabilize the region

## Campaign Integration

Players can:
- ✅ View location backstory
- ✅ Understand historical events
- ✅ Learn about faction presence
- ✅ Generate battle fluff tied to locations
- ⏳ Submit battle reports for specific locations
- ⏳ See campaign progress affect location control

---

## Future Enhancements

Planned features:
- [ ] Battle report tracking by location
- [ ] Dynamic location control indicators
- [ ] Faction influence on locations
- [ ] Location-specific rumors/intelligence
- [ ] Mission briefings from locations
- [ ] Database backend for persistent data
