from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = round(sentiment.polarity, 2)
    subjectivity = round(sentiment.subjectivity, 2)
    
    if polarity > 0:
        category = "Positive"
    elif polarity < 0:
        category = "Negative"
    else:
        category = "Neutral"
    
    return category, polarity, subjectivity

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = ""
    polarity = ""
    subjectivity = ""

    if request.method == "POST":
        text = request.form.get('text', '')  # Corrected form retrieval
        if text:  # Ensure text is not empty
            sentiment, polarity, subjectivity = analyze(text)

    return render_template('index.html', sentiment=sentiment, polarity=polarity, subjectivity=subjectivity)

if __name__ == '__main__':  
    app.run(debug=True)
