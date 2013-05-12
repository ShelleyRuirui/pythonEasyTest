f=open('input1.txt','w')
f.write('Hello\n')
f.write('Ruirui\n')
f.close()

f=open('input1.txt')
bytes=f.read()
print bytes

print bytes.split()
