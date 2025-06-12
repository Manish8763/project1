# Step 1: Import required libraries
from nltk.chat.util import Chat, reflections

# Step 2: Define patterns and responses
pairs = [
    [r"(.*)my name is (.*)", ["Hello %2, How are you today?"]],
    [r"(.*)help(.*)", ["I can help you."]],
    [r"(.*) your name ?", ["My name is thecleverprogrammer, but you can call me Robot."]],
    [r"how are you (.*) ?", ["I'm doing very well", "I am great!"]],
    [r"sorry (.*)", ["It's alright", "It's OK, never mind."]],
    [r"i'm (.*) (good|well|okay|ok)", ["Nice to hear that", "Alright, great!"]],
    [r"(hi|hey|hello|hola|holla)(.*)", ["Hello", "Hey there!"]],
    [r"what (.*) want ?", ["Make me an offer I can't refuse."]],
    [r"(.*)created(.*)", ["Aman Kharwal created me using Python's NLTK library.", "Top secret ;)"]],
    [r"(.*) (location|city) ?", ["I am from New Delhi, India."]],
    [r"(.*)raining in (.*)", ["No rain in the past 4 days here in %2.", "In %2, there is a 50% chance of rain."]],
    [r"how (.*) health (.*)", ["Health is very important, but I don't worry about mine."]],
    [r"(.*)(sports|game|sport)(.*)", ["I'm a very big fan of Cricket!"]],
    [r"who (.*) (Cricketer|Batsman)?", ["Virat Kohli."]],
    [r"quit", ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]],
    [r"(.*)", ["That is nice to hear."]]
]

# (Optional) Custom reflections (you can replace or add to the default)
my_dummy_reflections = {
    "go": "gone",
    "hello": "hey there"
}

# Step 3: Display a welcome message
print("Hi, I'm thecleverprogrammer and I like to chat")
print("Please type lowercase English language to start a conversation.")
print("Type 'quit' to exit.\n")

# Step 4: Create and start the chatbot
chat = Chat(pairs, reflections)  # You can use 'my_dummy_reflections' if you want custom ones
chat.converse()
