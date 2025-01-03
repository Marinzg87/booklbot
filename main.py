def main():
    book_path = "books/frankenstein.txt"
    
    with open(book_path) as f:
        file_contents = f.read()
        
    # count the words
    words = file_contents.split()
    words_count = len(words)
    
    # change the alpha characters to lower case and count    
    lower_case = file_contents.lower()
    characters = {}
    for character in lower_case:
        if character in characters:
            characters[character] += 1
        elif character.isalpha():
            characters[character] = 1
        
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print()
    
    for item in characters:
        print(f"The {item} character was found {characters[item]} times")

    print("--- End report ---")

main()
