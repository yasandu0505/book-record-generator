import json
import uuid
from faker import Faker

fake = Faker()

books = []

for _ in range(200):
    book = {
        "bookId": str(uuid.uuid4()),
        "authorId": str(uuid.uuid4()),
        "publisherId": str(uuid.uuid4()),
        "title": fake.sentence(nb_words=3),
        "publicationDate": fake.date(),
        "isbn": fake.isbn13(),
        "pages": fake.random_int(min=100, max=1000),
        "genre": fake.word(ext_word_list=["Adventure", "Romance", "Sci-Fi", "Dystopian", "Fantasy", "Historical"]),
        "description": fake.text(max_nb_chars=200),
        "price": round(fake.random_number(digits=4) / 100, 2),
        "quantity": fake.random_int(min=1, max=20),
    }
    books.append(book)

# Save the generated records to a JSON file
with open("extended_books.json", "w") as file:
    json.dump(books, file, indent=2)

print("Generated JSON file with 200+ book records!")
