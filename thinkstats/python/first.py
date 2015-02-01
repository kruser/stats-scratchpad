'''
NOTE: I'm not writing good, performant or even organized code here. This isn't intended to be reused, it's just
a scratchpad

Created on Jul 16, 2013

@author: kruser
'''
import survey
import numpy
import matplotlib.pyplot as pyplot

table = survey.Pregnancies()
table.ReadRecords()
print('Number of pregnancies', len(table.records))

firstBabies = [] 
others= [] 
liveBirths = 0

for record in table.records:
    if record.outcome == 1:
        liveBirths += 1
        if record.birthord == 1:
            firstBabies.append(record.prglength)
        else:
            others.append(record.prglength)
    
print('Live Births:', liveBirths)
print('First: mean {0}\tstd {1}'.format(numpy.mean(firstBabies), numpy.std(firstBabies)))
print('Other: mean {0}\tstd {1}'.format(numpy.mean(others), numpy.std(others)))

pyplot.hist([firstBabies, others], bins=range(20,45), label=['First Babies', 'Others'])
pyplot.legend()
pyplot.show()

