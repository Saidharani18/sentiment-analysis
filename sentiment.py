from textblob import TextBlob

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

text = input("Enter your text: ")
sentiment, polarity, subjectivity = analyze(text) 

print(f"\nSentiment: {sentiment}")
print(f"Polarity Score: {polarity}")
print(f"Subjectivity Score: {subjectivity}")
