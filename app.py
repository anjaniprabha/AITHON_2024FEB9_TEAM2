from flask import Flask, render_template, request
import nltk
from nltk.corpus import wordnet

app = Flask(__name__)

# Download WordNet data (if not already downloaded)
nltk.download('wordnet')

def get_word_definition(word):
    synonyms = []
    definition = ""
    examples = []

    for syn in wordnet.synsets(word):
        definition = syn.definition()
        examples.extend(syn.examples())
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())

    return definition, examples, synonyms

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_word', methods=['POST'])
def process_word():
    word = request.form['word'].lower()
    definition, examples, synonyms = get_word_definition(word)

    return render_template('index.html', word=word, definition=definition, examples=examples, synonyms=synonyms)

if __name__ == "__main__":
    app.run(debug=True)
