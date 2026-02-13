import os
import json
import random
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Paths
DB_PATH = 'medication_db.json'
KB_PATH = 'knowledge_base.json'

# --- Keep Mock DB Logic ---
def get_medication_status():
    if not os.path.exists(DB_PATH):
        return False
    with open(DB_PATH, 'r') as f:
        data = json.load(f)
    return data.get("user_id_1", {}).get("pills_taken", False)

# --- Load Knowledge Base ---
def load_knowledge_base():
    if not os.path.exists(KB_PATH):
        print("KB not found!")
        return {"intents": []}
    with open(KB_PATH, 'r') as f:
        return json.load(f)

KB = load_knowledge_base()

# --- Intelligence Engine ---
def score_similarity(user_text, pattern):
    """Simple inclusion check. Could be refined with NLP tokens later."""
    user_text = user_text.lower()
    pattern = pattern.lower()
    return 1 if pattern in user_text else 0

def determine_response(text):
    text = text.lower()
    best_intent = None
    best_score = 0
    
    # 1. Iterate through all intents in KB
    for intent in KB.get("intents", []):
        for pattern in intent["patterns"]:
            if pattern in text:
                # Basic priority scoring
                score = intent.get("priority", 1)
                # If longer match, slightly higher score to break ties? 
                # For now just use priority.
                
                if score > best_score:
                    best_score = score
                    best_intent = intent
    
    # 2. Logic Handler for "Dynamic" Responses
    if best_intent:
        responses = best_intent["responses"]
        chosen_response = random.choice(responses)
        
        # Dynamic Replacements
        if chosen_response == "__DYNAMIC_MEDICATION_CHECK__":
            taken = get_medication_status()
            if taken:
                return "Yes, you have already taken your pills today. Good job."
            else:
                return "No, you haven't taken your pills yet. Please take them now."
        
        return chosen_response

    # 3. Fallback
    return "I heard you say: " + text + ". But I'm not sure how to help with that yet."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/process_text', methods=['POST'])
def process_text():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    user_text = data['text']
    print(f"Received: {user_text}")

    bot_response = determine_response(user_text)
    print(f"Responding: {bot_response}")

    return jsonify({
        "text_input": user_text,
        "text_response": bot_response
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
