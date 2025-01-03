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
            
    # sort the counted characters by the count desc
    def sort_on(d):
        return d["num"]
    
    sorted_list = []
    for c in characters:
        sorted_list.append({"char": c, "num": characters[c]})
    sorted_list.sort(reverse=True, key=sort_on)
        
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print()
    
    for item in sorted_list:
        print(f"The {item['char']} character was found {item['num']} times")

    print("--- End report ---")

main()
