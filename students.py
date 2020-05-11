import datetime
from pandas import to_datetime

class Student(object):
    def __init__(self, name, start, end, level):
        self.name = name
        self.start = datetime.datetime.strptime(start,'%Y-%m-%d').date()
        try:
            self.end = datetime.datetime.strptime(end,'%Y-%m-%d').date()
        except TypeError:
            self.end = None
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

students = [
        Student('Kamran Javid', '2018-10-01','2019-10-01','postdoc'),
        Student('Lukas Hergt', '2017-01-01',None,'phd'),
        Student('Fruzsina Agocs', '2017-10-01',None,'phd'),
        Student('Will Barker', '2017-10-01',None,'phd'),
        Student('Dominic Anstey', '2018-10-01',None,'phd'),
        Student('Harry Bevins', '2019-10-01',None,'phd'),
        Student('Ian Roque', '2019-10-01',None,'phd'),
        Student('Ed Higson', '2016-10-01','2017-10-01','phd'), 
        Student('Thomas Gessey-Jones', '2019-10-01',None,'masters'),
        Student('Aleksandr Petrosyan', '2019-10-01',None,'masters'),
        Student('Ayngaran Thavanesan', '2019-10-01',None,'masters'),
        Student('Emma Shen', '2019-10-01',None,'masters'),
        Student('Deaglan Bartlett', '2018-10-01','2019-07-01','masters'),
        Student('Jamie Bamber', '2018-10-01','2019-07-01','masters'),
        Student('Ian Roque', '2018-10-01','2019-07-01','masters'),
        Student('Ward Haddadin', '2017-10-01','2018-07-01','masters'),
        Student('Jessica Rigley', '2017-10-01','2018-07-01','masters'),
        Student('Panagiotis Mavrogiannis', '2017-10-01','2018-07-01','masters'),
        Student('Fruzsina Agocs', '2016-10-01','2017-07-01','masters'),
        Student('Robert Knighton', '2016-10-01','2017-07-01','masters'),
        Student('Stephen Pickman', '2016-10-01','2017-07-01','masters'),
        Student('Daniel Manela', '2016-10-01','2017-07-01','masters'),
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
student = students[0]
for i, student in enumerate(students):
    start = student.start.toordinal()
    if student.end is not None:
        end = student.end.toordinal() 
    else:
        end = datetime.date.today().toordinal()
        
    rect = plt.Rectangle((start, i), end-start, 1, fc=student.color, ec='k') 
    print(rect)
    ax.add_artist(rect)
    ax.annotate(student.name, (start, i+0.5), va='center', ha='left')
    
ax.set_xlim(min([student.start.toordinal() for student in students]), datetime.date.today().toordinal())
ax.set_ylim(0,len(students)+1)

