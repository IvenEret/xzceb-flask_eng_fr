from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    Translated_text_fr = translator.english_to_french(textToTranslate)
    return Translated_text_fr

@app.route("/french_to_english")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    Translated_text_eng = translator.french_to_english(textToTranslate)
    return Translated_text_eng

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
