with open('data.txt') as file:
    a=0
    answer=file.readlines()
    for i in answer:
        if i == str(i):
            a+=1
print(f"Кількість слів у файлу:{a}")