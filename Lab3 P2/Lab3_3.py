from abc import ABC, abstractmethod


class ICourse(ABC):

    @property
    @abstractmethod
    def course_name(self):
        pass

    @course_name.setter
    @abstractmethod
    def course_name(self, course_name):
        pass

    @property
    @abstractmethod
    def course_teachers(self):
        pass

    @property
    @abstractmethod
    def course_topics(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass


class ILocalCourse(ICourse, ABC):

    @property
    @abstractmethod
    def local_lab(self):
        pass

    @local_lab.setter
    @abstractmethod
    def local_lab(self, local_lab):
        pass


class IOffsiteCourse(ICourse, ABC):

    @property
    @abstractmethod
    def offsite_lab(self):
        pass

    @offsite_lab.setter
    @abstractmethod
    def offsite_lab(self, offsite_lab):
        pass


class ITeacher(ABC):

    @property
    @abstractmethod
    def teacher_name(self):
        pass

    @teacher_name.setter
    @abstractmethod
    def teacher_name(self, teacher_name):
        pass

    @property
    @abstractmethod
    def field(self):
        pass

    @field.setter
    @abstractmethod
    def field(self, field):
        pass


class ICourseFactory(ABC):

    @abstractmethod
    def new_teacher(self, name, field):
        pass

    @abstractmethod
    def new_local_course(self, course_name, local_lab):
        pass

    @abstractmethod
    def new_offsite_course(self, course_name, offsite_lab):
        pass


class LocalCourse(ILocalCourse):

    def __init__(self, course_name, local_lab):
        self.course_name = course_name
        self.local_lab = local_lab
        self.course_teachers = []
        self.course_topics = []

    @property
    def local_lab(self):
        return self.__local_lab

    @local_lab.setter
    def local_lab(self, local_lab):
        if not isinstance(local_lab, str):
            raise TypeError
        self.__local_lab = local_lab

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, course_name):
        if not isinstance(course_name, str) and  not course_name:
            raise TypeError
        self.__course_name = course_name

    @property
    def course_teachers(self):
        return self.__course_teachers

    @course_teachers.setter
    def course_teachers(self, teachers):
        self.__course_teachers = []

    @property
    def course_topics(self):
        return self.__course_topics

    @course_topics.setter
    def course_topics(self, topics):
        self.__course_topics = []

    def __add__(self, other):
        if isinstance(other, Teacher) and other not in self.course_teachers:
            self.course_teachers.append(other)
            return self
        if isinstance(other, str) and other not in self.course_topics:
            self.course_topics.append(other)
            return self

    def __iadd__(self, other):
        if isinstance(other, Teacher) and other not in self.course_teachers:
            self.course_teachers.append(other)
            return self
        if isinstance(other, str) and other not in self.course_topics:
            self.course_topics.append(other)
            return self

    def __sub__(self, other):
        if isinstance(other, Teacher) and other in self.course_teachers:
            self.course_teachers.remove(other)
            return self
        if isinstance(other, str) and other in self.course_topics:
            self.course_topics.remove(other)
            return self

    def __isub__(self, other):
        if isinstance(other, Teacher) and other in self.course_teachers:
            self.course_teachers.remove(other)
            return self
        if isinstance(other, str) and other in self.course_topics:
            self.course_topics.remove(other)
            return self

    def __str__(self):
        return f'{self.course_teachers[0]}'


class OffsiteCourse(IOffsiteCourse):
    def __init__(self, course_name, offsite_lab):
        self.course_name = course_name
        self.offsite_lab = offsite_lab
        self.course_teachers = []
        self.course_topics = []

    @property
    def offsite_lab(self):
        return self.__offsite_lab

    @offsite_lab.setter
    def offsite_lab(self, offsite_lab):
        if not isinstance(offsite_lab, str):
            raise TypeError
        self.__offsite_lab = offsite_lab

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, course_name):
        if not isinstance(course_name, str) and  not course_name:
            raise TypeError
        self.__course_name = course_name

    @property
    def course_teachers(self):
        return self.__course_teachers

    @course_teachers.setter
    def course_teachers(self, course_teachers):
        self.__course_teachers = []

    @property
    def course_topics(self):
        return self.__course_topics

    @course_topics.setter
    def course_topics(self, course_topics):
        self.__course_topics = []

    def __add__(self, other):
        if isinstance(other, Teacher) and other not in self.course_teachers:
            self.course_teachers.append(other)
            return self
        if isinstance(other, str) and other not in self.course_topics:
            self.course_topics.append(other)
            return self

    def __iadd__(self, other):
        if isinstance(other, Teacher) and other not in self.course_teachers:
            self.course_teachers.append(other)
            return self
        if isinstance(other, str) and other not in self.course_topics:
            self.course_topics.append(other)
            return self

    def __sub__(self, other):
        if isinstance(other, Teacher) and other in self.course_teachers:
            self.course_teachers.remove(other)
            return self
        if isinstance(other, str) and other in self.course_topics:
            self.course_topics.remove(other)
            return self

    def __isub__(self, other):
        if isinstance(other, Teacher) and other in self.course_teachers:
            self.course_teachers.remove(other)
            return self
        if isinstance(other, str) and other in self.course_topics:
            self.course_topics.remove(other)
            return self


    def __str__(self):
        result = self.course_name + '\nTeachers:\n'
        for teacher in self.course_teachers:
            result += str(teacher) + '\n'
        result += 'Topics:\n'
        for topic in self.course_topics:
            result += str(topic) + '\n'
        return result


class Teacher(ITeacher):

    def __init__(self, teacher_name, field):
        self.teacher_name = teacher_name
        self.field = field

    @property
    def teacher_name(self):
        return self.__teacher_name

    @teacher_name.setter
    def teacher_name(self, teacher_name):
        if not isinstance(teacher_name, str) and not teacher_name:
            raise TypeError
        self.__teacher_name = teacher_name

    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field):
        if not isinstance(field, str) and not field:
            raise TypeError
        self.__field = field

    def __str__(self):
        return f'{self.teacher_name} is God in {self.field} '


class CourseFactory(ICourseFactory):

    def new_offsite_course(self, course_name, offsite_lab):
        return OffsiteCourse(course_name, offsite_lab)

    def new_local_course(self, course_name, local_lab):
        return LocalCourse(course_name, local_lab)

    def new_teacher(self, name, field):
        return Teacher(name, field)


x = CourseFactory()
teacher1 = x.new_teacher('Mykyta', 'Math')
teacher2 = x.new_teacher('Bob', 'Python')

lnd_course = x.new_offsite_course('Python', 'London')
lnd_course += teacher1
lnd_course += teacher2
lnd_course += 'OOP'

print(lnd_course)







