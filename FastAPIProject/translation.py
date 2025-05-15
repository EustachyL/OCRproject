from googletrans import Translator
import re
# Funkcja tłumaczenia z czeskiego na angielski
def translate_czech_to_english(text):
    translator = Translator()
    translated = translator.translate(text, src='cs', dest='en')
    return translated.text
# Przykład przetwarzania tekstu OCR
def clean_ocr_text(ocr_text):
    # Usunięcie zbędnych spacji i znaków specjalnych
    ocr_text = ocr_text.replace("’", "'")  # Zamiana apostrofów, które mogą być błędnie rozpoznane
    ocr_text = ocr_text.replace("\\", " ")  # Zamiana apostrofów, które mogą być błędnie rozpoznane
    ocr_text = re.sub(r'[^A-Za-z0-9\s]', '', ocr_text)
    return ocr_text
english_texts = []
# Przykład użycia,
for idx, czech_text in enumerate(texts):
    cleaned_text = clean_ocr_text(czech_text)
    english_text = translate_czech_to_english(cleaned_text)
    english_texts.append(english_text)
    print(f"Tłumaczenie \n: {english_text}")
with open('tłumaczenie.txt', 'w', encoding='utf-8') as f:
    for idx, text in enumerate(english_texts):
        f.write(text)