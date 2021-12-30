import datetime
from pandas import to_datetime

class Student(object):
    def __init__(self, name, start, end, level):
        self.name = name
        self.start = datetime.datetime.strptime(start,'%Y-%m-%d').date()
        try:
            self.end = datetime.datetime.strptime(end,'%Y-%m-%d').date()
        except TypeError:
            self.end = datetime.date.today()
        self.level = level

    def __str__(self):
        string = '%s (%s): %s --' % (self.name, self.level, self.start) 
        if self.end is not None:
            string += ' %s' % self.end
        return string

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.start < other.start
        #return self.end > other.end

    @property
    def color(self):
        if self.level == 'masters':
            return 'C0'
        elif self.level == 'phd':
            return 'C1'
        elif self.level == 'postdoc':
            return 'C2'
        elif self.level == 'summer':
            return 'C3'
        if self.level == 'mphil':
            return 'C4'

students = [
        Student('David Yallup', '2021-01-10',None,'postdoc'),
        Student('Jianhui Lui', '2020-09-10','2021-01-31','postdoc'),
        Student('Kamran Javid', '2018-10-01','2019-10-01','postdoc'),
        Student('Kamran Javid', '2017-10-01','2018-09-30','phd'),
        Student('Ayngaran Thavenesan', '2021-10-01',None,'phd'),
        Student('Adam Ormondroyd', '2021-10-01',None,'phd'),
        Student('Thomas Gessey-Jones', '2020-10-01',None,'phd'),
        Student('George Carter', '2020-10-01',None,'phd'),
        Student('Kilian Scheutwinkel', '2020-12-01',None,'phd'),
        Student('Isidro Gomez Vargaz', '2020-03-16','2020-12-04','phd'),
        Student('Harry Bevins', '2019-10-01',None,'phd'),
        Student('Ian Roque', '2019-10-01',None,'phd'),
        Student('Dominic Anstey', '2018-10-01',None,'phd'),
        Student('Thomas Mcaloone', '2020-06-10','2021-09-30','phd'),
        Student('Fruzsina Agocs', '2017-10-01','2021-09-01','phd'),
        Student('Will Barker', '2017-10-01','2021-08-25','phd'),
        Student('Lukas Hergt', '2017-01-01','2021-01-08','phd'),
        Student('Ed Higson', '2016-10-01','2017-10-01','phd'), 
        Student('Yoann Launay', '2021-10-01',None,'masters'),
        Student('Oliver Normand', '2021-10-01',None,'masters'),
        Student('Xy Wang', '2021-10-01',None,'masters'),
        Student('Carola Zanoletti', '2021-10-01',None,'masters'),
        Student('Yi-Jer Loh', '2020-10-01','2021-07-01','masters'),
        Student('Metha Prathaban', '2020-10-01','2021-07-01','masters'),
        Student('Thomas Gessey-Jones', '2019-10-01','2020-07-01','masters'),
        Student('Aleksandr Petrosyan', '2019-10-01','2020-07-01','masters'),
        Student('Ayngaran Thavenesan', '2019-10-01','2020-10-01','masters'),
        Student('Emma Shen', '2019-10-01','2020-09-30','mphil'),
        Student('Allahyar Sahibzada', '2021-10-01',None,'mphil'),
        Student('Deaglan Bartlett', '2018-10-01','2019-07-01','masters'),
        Student('Jamie Bamber', '2018-10-01','2019-07-01','masters'),
        Student('Ian Roque', '2018-10-01','2019-09-15','mphil'),
        Student('Ward Haddadin', '2017-10-01','2018-07-01','masters'),
        Student('Jessica Rigley', '2017-10-01','2018-07-01','masters'),
        Student('Panagiotis Mavrogiannis', '2017-10-01','2018-09-30','mphil'),
        Student('Fruzsina Agocs', '2016-10-01','2017-07-01','masters'),
        Student('Robert Knighton', '2016-10-01','2017-07-01','masters'),
        Student('Stephen Pickman', '2016-10-01','2017-07-01','masters'),
        Student('Daniel Manela', '2016-10-01','2017-07-01','masters'),
        Student('Zak Shumaylov', '2021-06-21', '2021-09-30', 'summer'),
        Student('Mattia Varrone', '2021-06-21', '2021-09-30', 'summer'),
        Student('Maxime Jabarian', '2019-06-01', '2019-09-01', 'summer'),
        Student('Denis Werth', '2019-06-01', '2019-09-01', 'summer'),
        Student('Maxime Jabarian', '2019-06-01', '2019-09-01', 'summer'),
        Student('Liam Lau', '2019-06-01', '2019-09-01', 'summer'),
        Student('Elizabeth Guest', '2018-06-01', '2018-09-01', 'summer'),
        Student('Ward Haddadin', '2018-06-01', '2018-09-01', 'summer'),
        Student('Shu-Fan Chen', '2018-06-01', '2018-09-01', 'summer'),
        ]

students = sorted(students)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
student_names = [student.name for student in students]
unique_students = list(dict.fromkeys(student_names))

for student in students:
    start = student.start.toordinal()
    if student.end is not None:
        end = student.end.toordinal() 
    else:
        end = datetime.date.today().toordinal()
        
    i = unique_students.index(student.name)
    rect = plt.Rectangle((start, i), end-start, 1, fc=student.color, ec='k') 
    print(rect)
    ax.add_artist(rect)
    ax.annotate(student.name, (start, i+0.5), va='center', ha='left')
    
min_year = min([student.start.year for student in students])
date_labels = [datetime.date(i,1,1) for i in range(min_year+1,datetime.date.today().year+1)]
ax.set_xticks([d.toordinal() for d in date_labels])
ax.set_xticklabels([d.year for d in date_labels])

ax.set_xlim(min([student.start.toordinal() for student in students]), datetime.date.today().toordinal()+100)
ax.set_ylim(0,len(students)+1)

