def function(one):
    with open('one.txt','r') as file:
        lines=file.readlines()
    a=lines[0].split(",")
    lst=[]
    d={}
    f=len(lines)
    for i in range(1,f):
                for j in range(3):
                       b=lines[i].split(",")
                       d.setdefault(a[j],b[j])
                       s=d.copy()
                lst.append(s)
                d.clear()
    return lst

