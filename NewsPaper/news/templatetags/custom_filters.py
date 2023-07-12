from django import template

register = template.Library()

replaced_words = ['bed_word', 'bed_word_2']

@register.filter(name='censor')
def censor(value, arg='*replased*'):
    value = value.lower().split()
    for word in replaced_words:
        for i in range(len(value)):
            if word == value[i]:
                value[i] = '*replased*'
    return " ".join(value)