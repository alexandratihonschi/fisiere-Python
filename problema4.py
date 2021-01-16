with open('input.txt','r') as f:
    a=f.readline()
    n=int(a)-2
    d=int(a)-1
    r=int(a)+1
    e=int(a)+2
with open('output.txt','w') as f:
    f.write(str(n))
    f.write("  ")
    f.write(str(d))
    f.write("  ")
    f.write(str(a))
    f.write("  ")
    f.write(str(r))
    f.write("  ")
    f.write(str(e))