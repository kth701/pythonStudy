

try :
    # file = open("data/names_price.txt","r",encoding="UTF-8")
    # width 블럭을 벗어나면 auto close()기능 
    with open("data/names_price.txt","r",encoding="UTF-8") as file:
        text = file.read()
        print(text)

    print("end ")
except Exception as e:
    pass
finally:
    pass