D={'food':'Spam','quantity':4,'color':'pink'}
print D['food']

D['quantity']+=1
print D

rec={'name':{'first':'Bob','last':'Smith'},
     'job':['dev','mgr'],
     'age':40.5
    }

print rec['name']
print rec['name']['last']
print rec['job'][-1]
rec['job'].append('janitor')
print rec

squares=[x**2 for x in [1,2,3,4,5]]
print squares

squares=[]
for x in [1,2,3,4,5]:
    squares.append(x**2)

print squares

if not D.has_key('f'):
    print 'missing'

T=(1,2,3,4,5)
print len(T)

T+(5,6)
print T
