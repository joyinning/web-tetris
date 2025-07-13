#!/usr/bin/env python3
"""
Web-based Tetris Game using Flask
"""

from flask import Flask, render_template, request, jsonify, session
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tetris_secret_key_2024'

class WebTetrisGame:
    def __init__(self):
        self.board_width = 10
        self.board_height = 20
        self.users_file = 'users.json'
        
    def load_users(self):
        """Load user data from JSON file"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_users(self, users):
        """Save user data to JSON file"""
        with open(self.users_file, 'w') as f:
            json.dump(users, f, indent=2)
    
    def create_i_block(self):
        """Create a simple I-block"""
        return [
            [1, 1, 1, 1]
        ]
    
    def create_o_block(self):
        """Create O-block"""
        return [
            [1, 1],
            [1, 1]
        ]
    
    def create_t_block(self):
        """Create T-block"""
        return [
            [0, 1, 0],
            [1, 1, 1]
        ]
    
    def create_l_block(self):
        """Create L-block"""
        return [
            [1, 0],
            [1, 0],
            [1, 1]
        ]
    
    def create_j_block(self):
        """Create J-block"""
        return [
            [0, 1],
            [0, 1],
            [1, 1]
        ]
    
    def create_s_block(self):
        """Create S-block"""
        return [
            [0, 1, 1],
            [1, 1, 0]
        ]
    
    def create_z_block(self):
        """Create Z-block"""
        return [
            [1, 1, 0],
            [0, 1, 1]
        ]
    
    def get_random_block(self):
        """Get a random Tetris block"""
        import random
        blocks = [
            self.create_i_block,
            self.create_o_block,
            self.create_t_block,
            self.create_l_block,
            self.create_j_block,
            self.create_s_block,
            self.create_z_block
        ]
        return random.choice(blocks)()

game = WebTetrisGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.get_json()
    username = data.get('username', '').strip()
    difficulty = data.get('difficulty', 'medium')
    
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    
    # Load or create user
    users = game.load_users()
    if username not in users:
        users[username] = {'scores': [], 'last_played': None}
    
    users[username]['last_played'] = datetime.now().isoformat()
    game.save_users(users)
    
    # Store in session
    session['username'] = username
    session['difficulty'] = difficulty
    
    return jsonify({
        'success': True,
        'username': username,
        'difficulty': difficulty,
        'previous_scores': users[username]['scores']
    })

@app.route('/save_score', methods=['POST'])
def save_score():
    data = request.get_json()
    score = data.get('score', 0)
    username = session.get('username')
    
    if not username:
        return jsonify({'error': 'No active user session'}), 400
    
    # Save score
    users = game.load_users()
    if username in users:
        users[username]['scores'].append(score)
        game.save_users(users)
    
    return jsonify({
        'success': True,
        'username': username,
        'all_scores': users[username]['scores']
    })

@app.route('/get_users')
def get_users():
    users = game.load_users()
    return jsonify(users)

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=3000) 