from transformers import pipeline

def load_model():
    # Load the pre-trained HuggingFace pipeline for text classification
    # Explicitly set the famework to Pytorch to avoid Keras import issues
    model_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english", framework="pt")
    return model_pipeline

def classify_text(model, text):
    # Use the model to classify the input text
    result = model(text)
    return result
def main():
    # Load the model
    model = load_model()
    text = input("Enter a text to classify: ")

    result = classify_text(model, text)
    print(result)

if __name__ == "__main__":
    main()