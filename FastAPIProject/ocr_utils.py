import fitz  # PyMuPDF
import io
from PIL import Image
import pytesseract  # OCR dla ekstrakcji tekstu


# Funkcja do ekstrakcji obrazów i tekstu z PDF
def extract_images_and_text_from_pdf(pdf_path):
    images = []
    texts = []

    # Otwórz PDF
    pdf_document = fitz.open(pdf_path)

    # Przechodzimy przez wszystkie strony
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)

        # Ekstrakcja obrazów z każdej strony
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            images.append(image)  # Dodajemy obraz do listy

            # Ekstrakcja tekstu z obrazu za pomocą pytesseract (OCR)
            text = pytesseract.image_to_string(image)  # Zwraca tekst z obrazu
            texts.append(text)  # Dodajemy tekst do listy

    return images, texts


# Przykład użycia
pdf_path = 'skoda.pdf'
images, texts = extract_images_and_text_from_pdf(pdf_path)

# Pokazuje pierwszy obraz
images[0].show()
# Pokazuje tekst wyekstrahowany z pierwszego obrazu
for idx, text in enumerate(texts):
    print(f"Text from image {idx + 1}:")
    print(text)
    print("=" * 50)

