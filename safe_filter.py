#comment filterer:

#open significant words
with open("C:/Users/antho/Desktop/felixa-main/backend/filterer/emotional_words.txt", "r") as f:
    content = set(f.read().splitlines())
#open dictionary
with open("C:/Users/antho/Desktop/felixa-main/backend/filterer/dictionary.txt", "r") as f:
    dictionary = set(f.read().splitlines())

def filter_cmt(comments):

    #filters  
    safe = []
    trash = []

    #filtering comments
    for cmt in comments:

        if isinstance(cmt, str): #if it there is a string
            
            words = cmt.split() #break it into individual words
            str_only = [s for s in words if not s.isdigit()] #only strings, no integers allowed when checked in dictionary
            real = [w for w in words if w.isalpha()] #only if it is a string
            
            #check if there are any words in cmt that are in the keyword list "content"
            if any(word in content for word in words): 
                if cmt not in safe:
                    safe.append(cmt)
                    continue
            #check if any of the words are real from the dictionary
            if any(word not in dictionary for word in str_only): #if the word in str_only is not in dictionary, trash it
                trash.append(cmt)
                continue
            #if it is one word only remove it
            if cmt in content:
                    if cmt not in safe:
                        safe.append(cmt)
            elif len(cmt.split()) == 1:
                    trash.append(cmt)

            #if it is two or more words excluding int's, append to safe
            if len(real) >= 2:
                if cmt not in safe:
                    safe.append(cmt) 
            elif any(w for w in real if w in content):
                if cmt not in safe:
                    safe.append(cmt)
            else:
                if cmt not in trash:
                    trash.append(cmt)

            #if it is only numbers remove it
                #if isinstance(cmt, int):
                    #trash.append(cmt)
            
            #making sure there are no duplicates that are in safe in trash
            trash = [t for t in trash if t not in safe]

    return safe