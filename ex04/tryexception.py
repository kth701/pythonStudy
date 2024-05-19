# try exception

 
enum = 100
try:
    num2 = num / 0
except Exception as e:
    print('Error: ',e)

print('end')