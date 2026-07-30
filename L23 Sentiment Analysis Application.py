from transformers import pipeline                                     

def sentiment_analysis(texts):
    # Load the model
    sentiment_analysis = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
   
   if isinstance(texts, str):
    texts = [texts]  # Convert to list becauese semtiment_analysis analyzes doesn't support string input

    results = sentiment_analysis(texts)
    return results

def analyze_sentiment():
    text = input("Enter a sentence or multiple sentences (separated by |): ")
    sentences = text.split("|")  # Split input into sentences
    res = sentiment_analysis(texts)

    for i,sentiment in enumerate(res):
        print(f"Sentence: {sentences[i].strip()}")
        print(f"Sentiment: {sentiment['label']}, Score: {sentiment['score']:.4f}\n")

analyze_text_sentiment()