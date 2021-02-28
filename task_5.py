from random import choice
from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_joke(num_j, repeat=False):
    """
    Creates a tuple with sentence from random words of other tuples
    :param num_j: Number of sentence
    :param repeat: Repeat or not the words from tuples
    :return: Tuple with sentence of random words
    """

    r_list = []
    for i in range(0, num_j):
        if repeat and len(nouns) == 0:
            break
        _buf_nouns = nouns
        _buf_adverbs = adverbs
        _buf_adjectives = adjectives
        if repeat:
            r_list.append(f"{_buf_nouns.pop(randrange(0, len(_buf_nouns)))} "
                          f"{_buf_adverbs.pop(randrange(0, len(_buf_adverbs)))} "
                          f"{_buf_adjectives.pop(randrange(0, len(_buf_adjectives)))}")
        else:
            r_list.append(f"{choice(_buf_nouns)} {choice(_buf_adverbs)} {choice(_buf_adjectives)}")

    return r_list


print(get_joke(2, True))
