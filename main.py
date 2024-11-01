# 1. while siklining ishlash tartibini tushuntirib bering?
# while sikli for ga oxhsash faqat farqi while sikli True ga teng bolib qolsa break qilmaguncha toxtamasdan loop qiladi
# 2. List ma’lumot turidagi append() va expand() metodlari orasiddagi farq nimada?

# listning append()ning  expend()dan farqi append() int -> listga qosha oladi 
# extend() esa int-> qosha olmaydi faqat str
# list = [1,24]
# list.extend('a')
# list.append(12)
# print(list)

# 3. Dict ma’lumot turida dict ichidagi ma’lum bir elementni o’chirishning qanday usullari mavjud?

# dict = {
#     1: {'a'},
#     2: {'b'},
#     3: {'v'}}
# dict.pop(3)
# print(dict)

# 4. For orqali sonlarni teskari tartibda chiqarish uchun nima qilish kerak?
# for i in range(num,-1,-1) oxiridagi ikkita -1 orqali forni teskari aylansa boladi

# for i in range(100,-1,-1):
#     print(i)

# Students nomli bo’sh dict yaratilsin. While True orqali shu dictga element qo’shish, elementni chiqarish, elementni yangilash va elementni o’chirish buyruqlari bo’lsin. 
# Ya’ni whileni ichida savol nomli o’zgaruvchi inputda son qabul qiladi.
students = {
    1:{"name":'Abdulloh','school':100,"class":10,'age': 16},
    2:{"name":'Akmal','school':100,"class":11,'age': 17},
    3:{"name":'Sarvar','school':100,"class":9,'age': 14},
    4:{"name":'Sanjar','school':100,"class":8,'age': 13},
    5:{"name":'Ibrohim','school':100,"class":10,'age': 15}
}

for key,value in students.items():
    print(value)

while True:
    print()
    savol = int(input("1. Student qo’shish\n2. Studentlarni chiqarish\n3. Studentni chiqarish\n4. Studentni o’chirish\n"))
    if savol == 1:
        for i in range(1):
            studen_name = input('Name: ')
            studen_school = int(input('School: '))
            studen_class = int(input('Student class: '))
            students_age = int(input('Studen Age: '))
            students[len(students)+1] = {"name":studen_name,'school': studen_school,"class":studen_class,'age':students_age}
            for key,value in students.items():
                print(key,value)
    elif savol == 2:
        for key,value in students.items():
            for i,value in value.items():
                print(i,value)
    elif savol == 3:
        student_id = int(input('Student id: '))
        for key,value in students.items():
            if key == student_id:
                for i,value in value.items():
                    print(i,value)
    elif savol == 4:
        for key,value in students.items():
            print(key,value)
        delete_student = int(input('Remove student: '))
        students.pop(delete_student)
        for key,value in students.items():
            print(key,value)


            


        

    
            


