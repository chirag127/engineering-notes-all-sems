Chatbot: Develop a conversational agent (chatbot) that can handle customer queries, perform simple tasks and make recommendations. Technologies: Natural Language Processing (NLP), Python, Dialogflow, TensorFlow.

Sure, here's a basic code example to get you started:

```
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Pre-processing function to remove stopwords and punctuation
def preprocess(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^\w\s]','',sentence)
    tokens = word_tokenize(sentence)
    stop_words = set(stopwords.words("english"))
    filtered_sentence = [w for w in tokens if not w in stop_words]
    return filtered_sentence

# Function to respond to user input
def respond(sentence):
    preprocessed_sentence = preprocess(sentence)
    if "hello" in preprocessed_sentence:
        return "Hello! How can I help you today?"
    elif "recommend" in preprocessed_sentence:
        return "I recommend trying out our new product."
    else:
        return "I'm sorry, I don't understand what you're asking for."

# Main loop to keep the chatbot running
while True:
    user_input = input("You: ")
    if user_input == "quit":
        break
    else:
        print("Chatbot: " + respond(user_input))
```

This code uses the Natural Language Toolkit (NLTK) library to pre-process the user's input and remove stopwords and punctuation. It then uses a simple if-else structure to respond to the user's input based on keywords. Of course, this is just a basic example and you can expand on it to add more features and functionality as needed.
