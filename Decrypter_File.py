bd=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '#', 'm', 'n', '/', '+', '-', 'r', 's', '^', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', '$', 'U', 'V', 'W', '%', 'Y', 'Z', '1', '2', '3', '4', '*', '6', '7', '8', '9', '0']
lbw=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
print("JX DECRYPTER GEN2")
import pickle
fname=input("Enter encrypted file path (with name and extension): ")
 #For binary file
#print(fname)
f=open(fname,'rb')
data=pickle.load(f)
f.close()

'''
f=open(fname)
data=f.readlines()
f.close()
'''
#print(data)
#data=data[0]
o=data.partition('.')[0]
o=o.split("'")
o=o[0:len(o)-1]
o2=[]
for l in o:
    t=''
    for k in str(l):
        if int(k) % 2 == 0:
            t=t+'0'
        else:
            t=t+'1'
    o2.append(int(t,2))
d=[]
for x in o2:
    for y in o2:
        d.append(x+y)
        d.append(x*y)
al2=[]
for k in d:
    if k not in al2:
        al2.append(k) 
al2.sort()
al2=al2[0:63]
MD=data.partition('.')[2]
#print(MD)
Non_conv_char=['X','@','l','T','%','t','&','5','(',')','o','q','p','=',';',':']
datalist=[]
for k in range(0,len(MD),9):
    datalist.append(MD[k:k+9])
Keydic={}
k=0
for j in al2:
    f=datalist[j].split('.')
    Keydic[f[1]]=lbw[k]
    k+=1
FINALVAL=''
for jas in datalist:
    f=jas.split('.')[0]
    if f in Keydic.keys():
        FINALVAL=FINALVAL+Keydic[f]
print("Decrypted Data: ")
print("-------------")
print(FINALVAL)
f=input(" Press Enter to quit ")
