from operator import attrgetter

class Student:

    def __init__(self, name_val, surname_val, rb_number_val, grades_val):
        self.name = name_val
        self.surname = surname_val
        self.rb_number = rb_number_val
        self.grades = grades_val
        self.aver_points = self.average_grades()

    def average_grades(self):
        return sum(self.grades) / len(self.grades)

    def get(self):
        return self


class Group:
    name = None
    list = []
    number = 0

    def __init__(self, name_val):
        name = name_val

    def check(self, student: Student):
        isPresent = False
        for i in range(self.number):
            if student.get().surname == self.list[i-1].get().surname and student.get().name == self.list[i-1].get().name:
                isPresent = True
                break
        return isPresent

    def add(self, student: Student):
        if self.number == 20 or self.check(student):
            print('Such student is already in the list')
        else:
            self.list.append(student)
            self.number += 1
            print('Student added')

    def best_stud(self):
        list_of_best = sorted(self.list, key=attrgetter('aver_points'), reverse=True)
        for i in range(5):
            print(list_of_best[i].get().surname, list_of_best[i].get().aver_points)


def main():
    grades_exmpl = [10,10,12,12,13,14,6,16,12,15]
    grades_exmpl2 = [16,9,12,12,1,14,5,16,15,15]
    grades_exmpl3 = [10,10,8,12,13,14,15,16,12,15]
    grades_exmpl4 = [10,10,12,7,13,14,15,16,4,15]
    grades_exmpl5 = [10,10,12,12,5,14,15,16,8,15]
    grades_exmpl6 = [10,10,2,12,13,4,15,16,12,15]

    group = Group('TV-13')
    group.add(Student('Mykyta', 'Rovinskyi', 1, grades_exmpl ))
    group.add(Student('Tolia', 'Romanin', 2, grades_exmpl2))
    group.add(Student('Roma', 'Pchelintsev', 3, grades_exmpl3))
    group.add(Student('Sofiia','Naumchenko', 4, grades_exmpl4))
    group.add(Student('Pervushen', 'Maksim', 5, grades_exmpl5))
    group.add(Student('Kozachenko', 'Denis', 6, grades_exmpl6))

    group.best_stud()
    print()

if __name__ == '__main__':
    main()