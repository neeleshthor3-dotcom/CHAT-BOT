import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import datetime

# Download necessary NLTK data
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

print("🤖 Advanced Chatbot: Hello! I'm now more intelligent. Type 'bye' to exit.")

# Expanded responses with more categories
responses = {
    "greeting": ["Hi there!", "Hello!", "Hey!", "Greetings!", "Howdy!"],
    "how_are_you": ["I'm doing great!", "All good ", "Feeling smart today!", "I'm fantastic, thanks for asking!"],
    "name": ["I'm an advanced Python chatbot.", "You can call me ChatBot AI.", "I'm your friendly AI assistant."],
    "help": ["Try saying hello, asking how I am, asking for the time, or typing bye.", "I can chat, tell time, and more!"],
    "time": ["The current time is " + datetime.datetime.now().strftime("%H:%M"), "It's " + datetime.datetime.now().strftime("%I:%M %p")],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"],
    "weather": ["I'm not connected to weather services yet, but I hope it's nice!", "Sorry, I can't check the weather right now."],
    "goodbye": ["Goodbye! 👋", "See you later!", "Take care!"]
}

# Keywords for intent classification
intents = {
    "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"],
    "how_are_you": ["how are you", "how do you do", "how's it going", "what's up"],
    "name": ["your name", "who are you", "what are you"],
    "help": ["help", "what can you do", "commands", "options"],
    "time": ["time", "what time", "current time", "clock"],
    "joke": ["joke", "funny", "laugh", "tell me a joke"],
    "weather": ["weather", "forecast", "rain", "sunny", "temperature"],
    "goodbye": ["bye", "goodbye", "see you", "exit", "quit"]
}

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word.isalnum()]
    return tokens

def classify_intent(user_input):
    tokens = preprocess_text(user_input)
    scores = {intent: 0 for intent in intents}

    for token in tokens:
        for intent, keywords in intents.items():
            if any(keyword in token or token in keyword for keyword in keywords):
                scores[intent] += 1

    # Return the intent with the highest score, or None if no match
    best_intent = max(scores, key=scores.get)
    return best_intent if scores[best_intent] > 0 else None

def get_response(user_input):
    intent = classify_intent(user_input)

    if intent:
        return random.choice(responses[intent])
    else:
        # Fallback responses
        fallbacks = [
            "Sorry, I don't understand that yet. Try asking for help!",
            "Hmm, I'm still learning. Can you rephrase that?",
            "I'm not sure about that. Ask me something else!",
            "That's interesting! Tell me more or ask for help."
        ]
        return random.choice(fallbacks)

# Simple conversation memory
conversation_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
        print("🤖 Advanced Chatbot: " + random.choice(responses["goodbye"]))
        break

    conversation_history.append(user_input)
    if len(conversation_history) > 5:  # Keep last 5 messages
        conversation_history.pop(0)

    reply = get_response(user_input)
    print(f"🤖 Advanced Chatbot: {reply}")
