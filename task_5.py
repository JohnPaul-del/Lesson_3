from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_joke (num_j, *j_list):
    r_list = []
    while num_j != 0:
        for word1, word2, word3 in zip(random.choice(j_list)):
            r_list.append([word1, word2, word3])
            num_j -= 1
    print(r_list)







num_j = int(input("kol-vo:"))
get_joke(num_j, nouns, adverbs, adjectives)
#print(zip(random.choice(nouns), random.choice(a)))