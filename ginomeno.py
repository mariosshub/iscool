n= int(input("δωσε ενα αριθμο")) #eisagogh ari8mou
def pr(n):
    p=n
    gin=1
    i=1
    t=1
    paragontes=[]
    taksi=[]
    # analysh se paragntes
    while gin<p :
        i+=1
        din=0
        while (p % i)==0 :
            p=p//i
            din+=1
        if din>0 :
            t+=1
            paragontes.append(i)
            taksi.append(din)
    for j in range(0,t+1):
            print("1 *",paragontes[j],"**",taksi[j])
pr(n)
