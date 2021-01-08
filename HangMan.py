import random
def hangman():
    word=['hello','opretor','commen','help','stole','phone','mobile','switch','shirt','book','science','chair']
    get_word=random.choice(word)
    g=list(get_word)
    p=[]
    guassing_word=list(get_word)
    index_store=[]
    for i in range(len(get_word)//2):
        j=random.randint(0,len(get_word)-1)
        index_store.append(j)
        p.append(g[j])
        # print(p)
        guassing_word[j]='_'

    re=guassing_word
    print(">>> Guass the  word : "+"".join(guassing_word))
    while 1:
        guass_word=input(">>> Guass letter : ")
        if guass_word in p:
            print("<<< You guass correct leter >>>\n")
            index_of_letter=g.index(guass_word)

            if guass_word in p:
                for i in range(len(index_store)):
                    try:
                        if g[index_store[i]]==guass_word:
                            guassing_word[index_store[i]]=guass_word
                            index_store.remove(index_store[i])
                            # print(index_store)
                            print(">>> "+''.join(guassing_word))
                    except Exception as e:
                        pass
                if "".join(guassing_word)=="".join(g):
                    print("\n<<< Yeh!!! You guass the correct word >>>\n")
                    break
        else:
            print("\n<<< You the guass incorrect letter. try again >>>")
    restart=input("Do you want to continue again?(y\\n)")
    if restart=='y' or restart=="Y":
        hangman()
    else:
        pass

hangman()

