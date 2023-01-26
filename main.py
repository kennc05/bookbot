# 15. Count words
def num_words(text):  
    words = text.split()
    print(f"{len(words)} words found in the document \n")
    dict = num_characters(words)
    return dict

     

# 16 Count letters 
def num_characters(words):
    character_dict = {}
    for word in words:
        for letter in word: 
            letter = letter.lower()
            if letter in character_dict:
                character_dict[letter] += 1
            else: 
                character_dict[letter] = 1

    return character_dict   
    #print(character_dict)


with open("books/frankenstein.txt") as f: 
    file_context = f.read() 
    print("--- Begin report of books/frankenstein.txt ---") 
    characters_dict = num_words(file_context)
    characters_list = list(characters_dict.items())
    characters_list.sort(key=lambda x: x[1], reverse= True)
    for character in characters_list:
        if character[0].isalpha():
            print(f"The {character[0]} character was found {character[1]} times")
    print("--- End report ---")


