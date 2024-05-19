
try :
    file = open("data/names_price.txt","r",encoding="UTF-8")
    
    text = file.read() #파일 전체 읽기
    text_lines = text.split("\n")

    # print(text_lines)
    # print(text_lines[0])
    
    # name = text_lines[0].split(",")[0]
    # price = text_lines[0].split(",")[1]
    # print(name,price)

    #list구조에 있는 데이터를 한꺼번에 읽어오기
    for list_data in text_lines:
        # print(list_data)
        name = list_data.split(",")[0]
        price = list_data.split(",")[0]

        print("상품이름:{}, 상품가격:{}".format(name, price))


except Exception as e:
    print(e)
finally:
    file.close()