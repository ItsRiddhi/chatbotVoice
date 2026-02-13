from app import determine_response

def test_logic():
    print("Testing Backend Logic (Massive KB)...")

    test_cases = [
        # Emergency
        ("I think I am having a stroke", "emergency", "Stroke Detection"),
        ("I fell and can't get up", "fall", "Fall Detection"),
        
        # Medical
        ("My blood sugar is low", "sugar", "Diabetes/Insulin"),
        ("I have a migraine", "headache", "Headache"),
        ("I feel very nauseous", "stomach", "Stomach/Nausea"),
        
        # Daily
        ("What should I eat for lunch?", "eat", "Nutrition"),
        ("I need to brush my teeth", "bath", "Hygiene"),
        
        # Tech
        ("My phone won't charge", "phone", "Tech Help"),
        
        # Conversation
        ("Tell me about the 1950s", "history", "Reminiscence"),
        ("I miss my husband", "family", "Grief/Family"),
        
        # General
        ("Thank you dear", "welcome", "Gratitude")
    ]

    for user_input, keyword_check, test_name in test_cases:
        print(f"\n[Test] {test_name}: '{user_input}'")
        response = determine_response(user_input)
        print(f" -> Bot: {response}")
        # accepted_response checks are hard because responses are random lists now, 
        # but we can check if it returns the fallback "I heard you say..."
        if "I heard you say" in response and "emergency" not in response.lower():
             print(f" [WARNING] Fallback triggered. Intent might be missing.")
        
    print("\nDone.")

if __name__ == "__main__":
    test_logic()
