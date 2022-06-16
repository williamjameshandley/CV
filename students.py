import datetime
from pandas import to_datetime

class Student(object):
    def __init__(self, name, start, end, level, email=None):
        self.name = name
        self.start = datetime.datetime.strptime(start,'%Y-%m-%d').date()
        try:
            self.end = datetime.datetime.strptime(end,'%Y-%m-%d').date()
        except TypeError:
            self.end = datetime.date.today()
        self.level = level
        self.email = email

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
        Student('David Yallup', '2021-01-10',None,'postdoc', 'david.yallup@gmail.com'),
        Student('Kamran Javid', '2018-10-01','2019-10-01','postdoc','linkedin'),
        Student('Kamran Javid', '2017-10-01','2018-09-30','phd','linkedin'),
        Student('Ayngaran Thavenesan', '2021-10-01',None,'phd', 'at735@cam.ac.uk'),
        Student('Adam Ormondroyd', '2021-10-01',None,'phd','ano23@cam.ac.uk'),
        Student('Thomas Gessey-Jones', '2020-10-01',None,'phd','tg400@cam.ac.uk'),
        Student('George Carter', '2020-10-01',None,'phd','gtc30@cam.ac.uk'),
        Student('Kilian Scheutwinkel', '2020-12-01',None,'phd','khs40@cam.ac.uk'),
        Student('Isidro Gomez Vargas', '2020-03-16','2020-12-04','phd','igomez@icf.unam.mx'),
        Student('Harry Bevins', '2019-10-01',None,'phd','htjb2@cam.ac.uk'),
        Student('Ian Roque', '2019-10-01',None,'phd','ilvr2@cam.ac.uk'),
        Student('Dominic Anstey', '2018-10-01',None,'phd','da401@cam.ac.uk'),
        Student('Thomas Mcaloone', '2020-06-10','2021-09-30','phd','thomas.mcaloone@polychord.co.uk'),
        Student('Fruzsina Agocs', '2017-10-01','2021-09-01','phd','fagocs@flatironinstitute.org'),
        Student('Will Barker', '2017-10-01','2021-08-25','phd','wb263@cam.ac.uk'),
        Student('Lukas Hergt', '2017-01-01','2021-01-08','phd','lthergt@phas.ubc.ca'),
        Student('Ed Higson', '2016-10-01','2017-10-01','phd','ejhigson@gmail.com'), 
        Student('Yoann Launay', '2021-10-01','2022-06-01','masters','yl844@cam.ac.uk'),
        Student('Oliver Normand', '2021-10-01','2022-06-01','masters','ocn22@cam.ac.uk'),
        Student('Xy Wang', '2021-10-01','2022-06-01','masters','yw491@cam.ac.uk'),
        Student('Carola Zanoletti', '2021-10-01','2022-06-01','masters','cmz22@cam.ac.uk'),
        Student('Yi Jer Loh', '2020-10-01','2021-06-01','masters','loh.yijer@live.com'),
        Student('Metha Prathaban', '2020-10-01','2021-06-01','masters','mrosep_10@hotmail.co.uk'),
        Student('Thomas Gessey-Jones', '2019-10-01','2020-06-01','masters','tg400@cam.ac.uk'),
        Student('Aleksandr Petrosyan', '2019-10-01','2020-06-01','masters','appetrosyan@icloud.com'),
        Student('Ayngaran Thavenesan', '2019-10-01','2020-10-01','masters','at735@cam.ac.uk'),
        Student('Emma Shen', '2019-10-01','2020-09-30','mphil','yhs24@cam.ac.uk'),
        Student('Allahyar Sahibzada', '2021-10-01',None,'mphil','smaa4@cam.ac.uk'),
        Student('Sam Leeney', '2022-04-11',None,'mphil','sakl2@cam.ac.uk'),
        Student('Deaglan Bartlett', '2018-10-01','2019-06-01','masters','deaglan.bartlett@physics.ox.ac.uk'),
        Student('Jamie Bamber', '2018-10-01','2019-06-01','masters','deaglan.bartlett@physics.ox.ac.uk'),
        Student('Ian Roque', '2018-10-01','2019-09-15','mphil','ilvr2@cam.ac.uk'),
        Student('Ward Haddadin', '2017-10-01','2018-06-01','masters','linkedin'),
        Student('Jessica Rigley', '2017-10-01','2018-06-01','masters','jkr40@cam.ac.uk'),
        Student('Panagiotis Mavrogiannis', '2017-10-01','2018-09-30','mphil','pmavrogi@physics.auth.gr'),
        Student('Fruzsina Agocs', '2016-10-01','2017-06-01','masters','fagocs@flatironinstitute.org'),
        Student('Robert Knighton', '2016-10-01','2017-06-01','masters','robertiknighton@gmail.com'),
        Student('Stephen Pickman', '2016-10-01','2017-06-01','masters','linkedin'),
        Student('Daniel Manela', '2016-10-01','2017-06-01','masters','danielmanela@gmail.com'),
        Student('Zak Shumaylov', '2021-06-21', '2021-09-30', 'summer','zakshum@gmail.com'),
        Student('Mattia Varrone', '2021-06-21', '2021-09-30', 'summer','mgv29@cam.ac.uk'),
        Student('Maxime Jabarian', '2019-06-01', '2019-09-01', 'summer','maximejabarian@gmail.com'),
        Student('Denis Werth', '2019-06-01', '2019-09-01', 'summer','denis.werth@ens-paris-saclay.fr'),
        Student('Maxime Jabarian', '2019-06-01', '2019-09-01', 'summer','maximejabarian@gmail.com'),
        Student('Liam Lau', '2019-06-01', '2019-09-01', 'summer', 'liam.lh.lau@physics.rutgers.edu'),
        Student('Elizabeth Guest', '2018-06-01', '2018-09-01', 'summer','elizabethrguest@gmail.com'),
        Student('Ward Haddadin', '2018-06-01', '2018-09-01', 'summer','linkedin'),
        Student('Shu-Fan Chen', '2018-06-01', '2018-09-01', 'summer','shufan_chen@g.harvard.edu'),
        Student('Mary Letey', '2022-06-24', '2022-08-17', 'summer','mil26@cam.ac.uk'),
        Student('Artyom Baryshnikov ', '2022-06-27', '2022-08-19', 'summer','ab2552@cam.ac.uk'),
        Student('Beichen Xu', '2022-06-27', '2022-09-02', 'summer','BXX002@student.bham.ac.uk'),
        Student('Metha Prathaban', '2022-10-01',None,'phd','mrosep_10@hotmail.co.uk'),
        Student('Wei-Ning Deng', '2022-10-01',None,'phd','weininden@gmail.com'),
        ]

students = sorted(students)
[(s.name, s.email) for s in students if s.end<datetime.date.today()]
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
date_labels = [datetime.date(i,1,1) for i in range(min_year+1,datetime.date.today().year+2)]
ax.set_xticks([d.toordinal() for d in date_labels])
ax.set_xticklabels([d.year for d in date_labels])

ax.set_xlim(min([student.start.toordinal() for student in students]), datetime.date.today().toordinal()+300)
ax.set_ylim(0,i+1)
ax.set_yticks([])
fig.tight_layout()

