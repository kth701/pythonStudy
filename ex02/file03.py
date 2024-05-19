# 파일 쓰기(파일생성,기록하기)

try:
    file = open("new_file.txt","w", encoding="UTF-8")

    file.write("orange")
    file.write("\n")
    file.write("melon")
    file.write("\n")
    file.write("길순이")
    file.write("\n")
    file.write("동길이")
    file.write("\n")

except Exception as e:
    print(e)
finally:
    file.close()
