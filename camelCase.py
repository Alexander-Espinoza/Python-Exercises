def to_camel_case(text):
    if text != "":
        letters = [text[i:i+1] for i in range(0, len(text), 1)]

        elementWords = []

        wordText = text.split("-")
        print(wordText)
        for subWordsText in wordText:
        
            subWords = subWordsText.split("_")
            print(subWords)
            if not subWords:
                elementWords.append(subWords)
            for element in subWords:
                elementWords.append(element)                    
                
        print(elementWords)
        wordsCapitalize = []
        i=0
        for word in elementWords:
            if i == 0:
                if word[0] != word[0].capitalize():
                    wordsCapitalize.append(word)
                else:
                    wordsCapitalize.append(word.capitalize())
                i += 1
                    
            else:
                wordsCapitalize.append(word.capitalize())

        textCamelCase = "".join(wordsCapitalize)
                          
    else:
        textCamelCase = text
    
    print(textCamelCase)  
    return(textCamelCase)
       

    
to_camel_case("hola-como_estas_dime")


