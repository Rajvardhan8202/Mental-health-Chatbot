import random

def generate_response(sentiment):
    if sentiment == 'negative':
        responses = [
            "I'm really sorry you're feeling this way. You're not alone.",
            "That sounds difficult. I'm here to listen.",
            "It's okay to feel overwhelmed sometimes."
        ]
    else:
        responses = [
            "That's great to hear! Keep going!",
            "I'm glad you're feeling positive today.",
            "You're doing really well."
        ]
    return random.choice(responses)
