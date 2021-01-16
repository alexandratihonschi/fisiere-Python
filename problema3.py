with open('globulete.txt','r') as f:
    a=f.readline()
    r=int(a)+3
    b=(int(a)+int(r))-2
    s=int(a)+int(r)+int(b)
with open('bradut.txt','w') as f:
    f.write(str(s))
