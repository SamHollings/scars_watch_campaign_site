import os
import json
from flask import Flask, request, url_for, render_template, redirect, session, jsonify
from markupsafe import escape
from langchain.messages import AIMessage, HumanMessage, SystemMessage

# Import fluff generator modules
from src import model_funcs, prompts, retrieval

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', b'_5#y2L"F4Q8z\n\xec]/')

# @app.route("/")
# def index():
#     name  = request.args.get("name", "Flask")
#     return f"<p>Hello {escape(name)}</p>"

@app.route('/')
def index():
    # if 'username' in session:
    #     return f'Logged in as {session["username"]}'
    
    username = session.get("username",None)
    return render_template('red_scar_overview.html', person=username, image_url='/static/red scar region.png')

@app.route('/scars_watch')
def scars_watch():
    return render_template('scars_watch.html')

@app.route('/characters')
def characters():
    return render_template('characters.html')

@app.route('/api/fluff/message', methods=['POST'])
def fluff_message():
    """API endpoint for fluff generator chat messages."""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        message_history = data.get('messages', [])

        if not user_message:
            return jsonify({'error': 'Empty message'}), 400

        # Initialize messages if empty
        if not message_history:
            message_history = [
                prompts.system_message,
                prompts.ai_message
            ]

        # Add user message
        message_history.append(HumanMessage(content=user_message))

        # Generate response
        try:
            model = model_funcs.gemini_model()
            relevant_history = retrieval.extract_relevant_history(user_message)

            response = model.invoke(
                message_history + [
                    HumanMessage(
                        content=f"The relevant history is: {relevant_history}"
                    )
                ]
            )
            response_text = response.content

        except Exception as e:
            response_text = f"Error generating response: {str(e)}"

        # Add assistant message
        message_history.append({"role": "assistant", "content": response_text})

        return jsonify({
            'response': response_text,
            'messages': message_history
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/fluff/reset', methods=['POST'])
def fluff_reset():
    """Reset the fluff generator conversation."""
    return jsonify({
        'messages': [
            prompts.system_message,
            prompts.ai_message
        ]
    })

@app.route('/location/<location_id>')
def location_detail(location_id):
    # Location data - can be moved to a database later
    locations_db = {
        'scars-watch': {
            'id': 'scars-watch',
            'name': 'Scars Watch',
            'backstory': 'Scars Watch is the primary military stronghold in the Red Scar Region, a Deathwatch Watch Fortress comprising a refitted Hecate Class Heavy Cruiser with escort vessels. Each member of the force is a seasoned veteran. The fortress was recommended by both Lord Roboute Guilliman and Commander Dante to maintain stability following the catastrophic Tyranid invasions in the sector, particularly after the Siege of Baal.',
            'description': 'Deathwatch Fortress Fleet. Strategic command center.',
            'events': [
                {'date': '899.M41', 'title': 'Founded during the Imperial campaigns', 'details': 'Scars Watch was established as a fortress and administrative center during the initial Imperial expansion into the Red Scar Region.'},
                {'date': '956.M41', 'title': 'Defended against Ork invasion', 'details': 'The garrison heroically defended against a massive Ork raid, holding the fortress walls for three weeks before reinforcements arrived.'},
                {'date': '987.M41', 'title': 'Peace summit held', 'details': 'Historic diplomatic negotiations between regional factions were hosted here, leading to a temporary ceasefire.'},
                {'date': '999.M41', 'title': 'Designated as Deathwatch Fortress', 'details': 'Following the Siege of Baal, the fortress was redesignated as a Deathwatch Watch Fortress under Watch Master Sanguone to counter ongoing Tyranid and xenos threats.'},
                {'date': '012.M42', 'title': 'Upgraded with new void shields', 'details': 'Recent renovations included the installation of new void shield generators, significantly enhancing the fortress defensive capabilities.'}
            ],
            'image': '/static/Scars Watch picture.jpeg'
        },
        'phlegmus': {
            'id': 'phlegmus',
            'name': 'Phlegmus',
            'backstory': 'Phlegmus, known throughout the sector as the Plague Planet, is a hellish world dominated by disease-saturated pools under the control of the Apostles of Contagion. The biologian caste, devoted to Nurgle, has transformed the planet into a nexus of contamination and mutation. The pools are so saturated with disease that they create portals to the Garden of Nurgle itself, allowing the Chaos forces to travel to other worlds and spread their blessed plagues. Invasion is nearly impossible due to the overwhelming toxic conditions.',
            'description': 'Plague Planet. Stronghold of the Apostles of Contagion.',
            'events': [
                {'date': '987.M41', 'title': 'Became a Chaos stronghold', 'details': 'Phlegmus fell to Chaos forces during a major Warp Breach event, allowing Nurgle\'s influence to take root.'},
                {'date': '995.M41', 'title': 'Spawned the Pestilent Brethren', 'details': 'The biologian cults on Phlegmus organized into the Apostles of Contagion warband, ruled by a casting of biological engineers intent on creating new and varied diseases.'},
                {'date': '001.M42', 'title': 'Disease vectors spread', 'details': 'Plague vectors created on Phlegmus were dispatched to nearby worlds, particularly Khajikes V, beginning the contamination of the region.'},
                {'date': '011.M42', 'title': 'Warp portal activity detected', 'details': 'Scans detect increasing Warp portal activity, suggesting the Apostles are preparing for expanded operations across the Red Scar.'}
            ],
            'image': None
        },
        'khajikes-v': {
            'id': 'khajikes-v',
            'name': 'Khajikes V',
            'backstory': 'Khajikes V has become a monument to the horrors of biological warfare waged by the Apostles of Contagion. Initially a minor Imperial colony, it was deliberately targeted by plague vectors from Phlegmus. Plague victims from across the Red Scar region are drawn to or sent to this world, where they succumb in mass plague pits. The accumulated corpses and disease create an overwhelming miasma of contamination, making conventional Imperial intervention nearly impossible. The world has become a living testament to Nurgle\'s "blessing."',
            'description': 'Plague-ravaged world. Primary victim of biological warfare.',
            'events': [
                {'date': '956.M41', 'title': 'Initially a minor Imperial colony', 'details': 'Khajikes V was a relatively stable agricultural world with modest population and Imperial presence.'},
                {'date': '998.M41', 'title': 'First plague outbreak recorded', 'details': 'Mysterious plague vectors began appearing, causing severe infections and rapid mortality. Origins initially unknown.'},
                {'date': '002.M42', 'title': 'Overwhelmed by plague victims', 'details': 'Mass casualties from the plague led to the world being declared a quarantine zone. Plague pits accumulated thousands of corpses.'},
                {'date': '010.M42', 'title': 'Declared a quarantine zone', 'details': 'Imperial forces cordoned off the world. Any attempt at aid or investigation is severely hampered by the toxic conditions.'}
            ],
            'image': None
        },
        'weepmire': {
            'id': 'weepmire',
            'name': 'Weepmire',
            'backstory': 'Weepmire serves as a secondary plague world under the influence of Nurgle, hosting experimental biologian cults loyal to the Apostles of Contagion. The planet\'s marshy terrain creates ideal conditions for disease proliferation and mutation. It functions both as a proving ground for new plagues and bioweapons, and as a fallback position for the Apostles\' operations. The world is less heavily contaminated than Phlegmus, but equally dangerous and unpredictable.',
            'description': 'Secondary Plague World. Experimental biolab.',
            'events': [
                {'date': '989.M41', 'title': 'Corrupted by Chaos forces', 'details': 'Weepmire fell to Chaos corruption, establishing a beachhead for Nurgle\'s influence in the Red Scar region.'},
                {'date': '996.M41', 'title': 'First biological experiments conducted', 'details': 'The biologian cults began their first major experiments with plague creation and mutation on the planet\'s surface.'},
                {'date': '004.M42', 'title': 'Linked to Phlegmus via Warp portal', 'details': 'A stable Warp portal was established between Weepmire and Phlegmus, allowing rapid transit of resources and personnel.'},
                {'date': '009.M42', 'title': 'Contains rumored xenos artifacts', 'details': 'Reconnaissance suggests the presence of archeotech and xenos biological materials used in the biologian experiments.'}
            ],
            'image': None
        },
        'baal': {
            'id': 'baal',
            'name': 'Baal',
            'backstory': 'Baal stands as the sacred homeworld of the Blood Angels Space Marine Chapter, though located beyond the immediate borders of the Red Scar Subsector. The proximity to the Red Scar region makes it strategically vital to regional stability. Baal has endured countless Tyranid assaults throughout history, culminating in a devastating siege by Hive Fleet Leviathan. The survival of Baal and its Chapter has direct implications for Imperial control of the Red Scar region. Commander Dante authorized Deathwatch operations in the Red Scar to protect this vital strategic asset.',
            'description': 'Sacred Homeworld of the Blood Angels. Beyond the Red Scar.',
            'events': [
                {'date': '999.M41', 'title': 'Survived the Siege of Baal', 'details': 'Baal endured the catastrophic siege by Hive Fleet Leviathan. Though victory was achieved, the cost was immense.'},
                {'date': '999.M41', 'title': 'Suffered catastrophic Tyranid invasion', 'details': 'Hive Fleet Leviathan brought unprecedented devastation. The Blood Angels were pushed to the brink but ultimately prevailed.'},
                {'date': '000.M42', 'title': 'Commander Dante authorized Red Scar operations', 'details': 'Recognizing that Tyranid threats remain in the Red Scar, Dante recommended establishing a Deathwatch presence to protect Baal and the sector.'},
                {'date': 'Current', 'title': 'Ongoing Tyranid splinter incursions', 'details': 'Remnant Tyranid fleets continue to probe the Red Scar region. The Deathwatch maintains constant vigilance.'}
            ],
            'image': None
        }
    }

    location = locations_db.get(location_id)
    if location is None:
        return f"Location '{escape(location_id)}' not found", 404

    return render_template('location_detail.html', location=location)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# @app.route('/hello')
# def hello():
#     return  'Hello, world'

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', person=name, image_url='/static/red scar region.png')

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'user {escape(username)}'

@app.route('/projects/')# doesn't work? perhaps needs pages under it...
def projects():
    return 'The projects page'


if __name__ == '__main__':
    # For Codespaces and local development
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', True)
    host = os.environ.get('FLASK_HOST', '0.0.0.0')

    with app.test_request_context():
        print(f"Routes available:")
        print(f"  {url_for('index')}")
        print(f"  {url_for('scars_watch')}")
        print(f"  {url_for('profile', username='sample')}")

    print(f"\nStarting Flask app on {host}:{port}")
    app.run(host=host, port=port, debug=debug)

