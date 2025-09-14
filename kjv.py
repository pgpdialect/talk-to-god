import random
import re
import requests

SENTENCE_LENGTH = 10   
NUM_SENTENCES = 5      

print("Downloading KJV Bible text (may take a few seconds)...")
url = "https://openbible.com/textfiles/kjv.txt"
response = requests.get(url)
if response.status_code != 200:
    print("Error: Could not download KJV text.")
    exit()

text = response.text.lower()

words = re.findall(r"\b[a-z]+\b", text)
unique_words = sorted(set(words))

if not unique_words:
    print("Error: No words extracted.")
    exit()

print(f"Loaded {len(unique_words)} unique words.")

def generate_sentence(length):
    sentence_words = [random.choice(unique_words) for _ in range(length)]
    return " ".join(sentence_words).capitalize() + "."

for _ in range(NUM_SENTENCES):
    print(generate_sentence(SENTENCE_LENGTH))
