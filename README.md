# Book Records Generator

This Python script generates a dataset of 200+ book records with randomly generated details using the `Faker` library. The generated data is stored in a JSON file named `extended_books.json`.

## Features
- Generates unique `bookId`, `authorId`, and `publisherId` for each book.
- Creates random book titles, publication dates, ISBN numbers, page counts, genres, descriptions, prices, and quantities.
- Saves the generated book records to a JSON file for further use.

## Requirements
Ensure you have Python installed on your system. This script requires the following Python libraries:
- `faker`

You can install the required library using:
```sh
pip install faker
```

## Usage
1. Clone or download this script.
2. Run the script using Python:
   ```sh
   python main.py
   ```
3. The generated book records will be saved to `extended_books.json` in the same directory.

## Example Output
```json
[
  {
    "bookId": "550e8400-e29b-41d4-a716-446655440000",
    "authorId": "123e4567-e89b-12d3-a456-426614174000",
    "publisherId": "789e4567-e89b-12d3-a456-426614174000",
    "title": "The Great Adventure",
    "publicationDate": "2023-08-15",
    "isbn": "978-3-16-148410-0",
    "pages": 350,
    "genre": "Fantasy",
    "description": "An epic journey through a mystical land...",
    "price": 19.99,
    "quantity": 10
  }
]
```

## License
This project is licensed under the MIT License.

