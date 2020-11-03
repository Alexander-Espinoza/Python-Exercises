def to_camel_case(text):
    text=text.replace('_',' ').replace('-', ' ').split(' ')
    words=[text[0]]
    print(text[1::])
    for t in text[1::]:
        words.append(t.capitalize())
    return "".join(words)

a=to_camel_case("hola-como_estas")
print(a)