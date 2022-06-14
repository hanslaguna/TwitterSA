# Tweet pre-processing functions

import re
import emoji
from spellchecker import SpellChecker
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# Remove URLs
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

# Remove tweets
def remove_hashtags(text):
    hashtag_pattern = re.compile(r'#([^\s]+)')
    return hashtag_pattern.sub(r'', text)

# Remove usernames
def remove_users(text):
    username_pattern = re.compile(r'@[^\s]+')
    return username_pattern.sub(r'', text)

# Emojis to words
def emojiToWord(text):
    demoji = emoji.demojize(text, delimiters=("__", "__"))
    demoji = demoji.replace('__', ' ')
    demoji = demoji.replace('_', ' ')
    return demoji

# Remove non-word characters
def remove_nonword(text):
     nonword_pattern = re.compile(r'[^A-Za-z0-9 ]+')
     return nonword_pattern.sub(r'', text)

# Remove extra whitespace
def remove_extraws(text):
    return " ".join(text.split())

# Spell checker
spell = SpellChecker()
def correct_spellings(text):
    corrected_text = []
    misspelled_words = spell.unknown(text.split())
    for word in text.split():
        if word in misspelled_words:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    return " ".join(corrected_text)
    
# Remove stopwords
def remove_sw(text):
    filtered_text = []
    for w in text:
        if w not in stop_words:
            filtered_text.append(w)
    return filtered_text
