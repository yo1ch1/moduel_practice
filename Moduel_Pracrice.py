grades =  [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #оценки
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #студенты
students_1 = list(students)
students_1.sort()
average = ((sum(grades[0])/len(grades[0])) #средний балл
       ,(sum(grades[1])/len(grades[1]))
       ,(sum(grades[2])/len(grades[2]))
       ,(sum(grades[3])/len(grades[3]))
       ,(sum(grades[4])/len(grades[4])))
print(dict(zip(students_1, average)))