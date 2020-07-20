def kids(sentence_func):
    def kids_sentence(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f"{original_sentence} by the kids"
    return kids_sentence

@kids
def laundry():
    return "The dirty laundry was cleaned"

def garbage():
    return "The garbage was taken out"
@kids
def dust():
    return "The house was dusted"

def groom():
    return "The dog was brushed"


print(laundry())
print(garbage())
print(dust())
print(groom())