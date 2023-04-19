from django import template

register = template.Library()

@register.filter()
def censor(value):

    CENS_WORDS = ['блин','дурак','редиска']

    words = value.split()
    result = []
    for word in words:
        if word in CENS_WORDS:
            result.append(word[0] + "*" * (len(word) - 2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)

    # bw = CENS_WORDS
    # for b_word in bw:
    #     for word in text.split():
    #         if word.lower() in b_word:
    #             text = text.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    #     return text
