def generate_response(emotion, culture="Indian"):
    responses = {
        "sadness": {
            "Indian": "I understand you're feeling low. Take some time to rest. Maybe a walk or some chai can help."
        },
        "joy": {
            "Indian": "That's wonderful! Keep smiling and spread the happiness!"
        },
        "anxiety": {
            "Indian": "Try some deep breathing. You're not alone. Maybe listening to some calming music helps?"
        },
        "fear": {
            "Indian": "You're safe right now. It's okay to feel afraid—maybe talk to someone you trust."
        },
        "anger": {
            "Indian": "Take a moment to breathe. Anger is valid, but managing it helps bring peace."
        },
        "love": {
            "Indian": "Love makes life beautiful. Cherish the moments."
        },
        "surprise": {
            "Indian": "Surprises can be exciting! Enjoy the moment."
        }
    }
    return responses.get(emotion, {}).get(culture, "I'm here to listen, whatever you're feeling.")
