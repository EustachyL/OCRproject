import chromadb
def chat_system(collection):
    print("Witaj w systemie czatowym! Zadaj pytanie lub napisz 'exit', aby zakończyć.")

    while True:
        # Pobranie pytania od użytkownika
        query = input("Ty: ")

        # Jeśli użytkownik chce zakończyć rozmowę
        if query.lower() == 'exit':
            print("Zakończenie czatu. Do widzenia!")
            break

        # Wyszukiwanie podobnych dokumentów
        similar_documents, distances = search_similar_texts(query, collection)

        # Jeśli znaleziono jakiekolwiek podobieństwa
        if similar_documents:
            print("Bot: Odpowiedź na Twoje pytanie:")
            print(similar_documents[0])  # Zwracamy najbardziej podobny dokument
        else:
            print("Bot: Nie mogę znaleźć odpowiedzi na to pytanie.")


# Przykład użycia
# Zakładając, że masz już zainicjowaną bazę danych i kolekcję
client = chromadb.Client()
collection = client.get_collection(name="document_embeddings")

# Uruchomienie systemu czatowego
chat_system(collection)
