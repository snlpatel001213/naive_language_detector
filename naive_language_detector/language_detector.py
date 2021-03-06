import json
import nltk

# Load the data file into memory
f = open("data.json")
j_data = json.loads(f.read())
LANGUAGE_SETS = {}
for language in j_data.keys():
    LANGUAGE_SETS[language] = set(j_data[language])
f.close()


# Split the text into sentences
def split_text(text):
    text = text.decode("utf-8")
    sentences = nltk.sent_tokenize(text)
    stripped_sentences = []
    for sentence in sentences:
        stripped_sentences.append(sentence.strip())
    return stripped_sentences

# Split a sentence into tokens
def tokenize_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens

# Detect language
def detect_language(text):

    # Convert the text into a set of unique tokens
    all_tokens = []
    sentences = split_text(text)
    for sentence in sentences:
        all_tokens += tokenize_sentence(sentence)
    all_tokens_set = set(all_tokens)

    # Find the language with the maximal intersection
    max_value = 0
    max_language = None
    for language in LANGUAGE_SETS.keys():
        local_value = len(all_tokens_set & LANGUAGE_SETS[language])
        if local_value > max_value:
            max_value = local_value
            max_language = language
    return max_language


# Test Code
def test():
    test_langs = ['en', 'de', 'tr', 'he']
    for lang in test_langs:
        f = open("tests/test_%s.txt" % lang)
        text = f.read()
        f.close()
        if lang == detect_language(text):
            print "%s OK" % lang
        else:
            print "%s ERROR" % lang







