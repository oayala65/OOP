from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

def analisis_sentimiento(texto):
    # Especificar el modelo
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"

    # Cargar el tokenizador y el modelo
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Cargar el pipeline de análisis de sentimiento
    sentiment_analysis = pipeline("sentiment-analysis",model=model,tokenizer=tokenizer)

    return sentiment_analysis(texto)

while True:
    print('\x1b[1;31m'+ f'\nIntroduzca 2 para salir')
    texto=input('\x1b[1;32m'+'\nDecime algo para analizar su sentimiento:  ')
    if texto==str(2):
        print('\nSaliendo del programa...\n')
        break
    print(f'{analisis_sentimiento(texto)}')

