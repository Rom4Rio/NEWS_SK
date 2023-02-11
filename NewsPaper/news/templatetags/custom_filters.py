from django import template

register = template.Library()

@register.filter()
def censor(text):

    CENS_WORDS = ['блин','дурак','редиска']

    bw = CENS_WORDS
    for b_word in bw:
        for word in text.split():
            if word.lower() in b_word:
                text = text.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
        return text
