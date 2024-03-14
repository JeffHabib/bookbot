def main():
    with open("github.com/JeffHabib/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_words = file_contents.lower()
        letters_only = []
        for character in lowered_words:
            if character.isalpha():
                letters_only.append(character)

        result = {}
        for letter in letters_only:
            if letter in result:
                result[letter] += 1
            else:
                result[letter] = 1
        listed_dict = []

        for key, value in result.items():
            new_dict = {'char': key, 'count': value}
            listed_dict.append(new_dict)
        

        def sort_on(dict):
            return dict["count"]
        
        listed_dict.sort(key=sort_on, reverse=True)
        
        print("---Begin report of books/frankenstein.txt---")
        
        for character_dict in listed_dict:
            print(f"The '{character_dict['char']} character was found {character_dict['count']} times.")
        print("---End report---")

if __name__ == "__main__":
    main()

