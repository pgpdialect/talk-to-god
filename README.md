# talk-to-god

Random sentence generator that uses the King James Version bible as a wordlist, no edit required or txt download required before running, it fetches it from openbible.com


```
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


```

For me the sentence was:

words right Gamaliel purloining lots aliah accept coping cretes dam bay smelling. Oppressed numbering uncleanness kareah addition zephi sheth princesses perga partakest. Like forgat subverting isuah tormentors spearmen bethbirei alloweth harnessed sore. Jericho roller casluhim ruler moseroth flee treading drew bamoth bowls. Eagle differing stolen tabbaoth sickle darkish plantation pains shage droves.

Let me know if you got something more insightful
