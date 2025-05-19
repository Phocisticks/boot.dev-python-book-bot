def count_words(string):
    return len(string.split())

def order_dictionary_by_count(u_dict):
    s_dict = dict(sorted(u_dict.items(), key=lambda item: item[1], reverse=True))
    return s_dict

def count_characters(string):
    character_dict = {}
    
    for c in string:
        character =  c.lower()
        if character not in character_dict:
            character_dict[character] = 0
        character_dict[character] += 1

    return character_dict