def separation_of_words(text):
    return text.split()

def number_of_words(words):
    return len(words)

def number_of_characters(text):
    count = {}
    for character in text:
        lowered = character.lower()
        if lowered in count:
            count[lowered] += 1
        else:
            count[lowered] = 1
    return count
        
def sort_on(item):
    return item["num"]

def character_list(count):
    pairs = [{"cha": ch, "num": n} for ch,n in count.items()]
    pairs.sort(reverse=True, key=sort_on)
    return pairs