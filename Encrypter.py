#This will show the encrypted data in a text format
print("JX ENCRYPTER GEN2")
def dTB(n):
	return bin(n).replace("0b", "")
import random
import pickle
import pyperclip as pc
o=[]
al=[]
while len(al)<73:
    while len(o)<9:
        k=random.randrange(4,1057)
        o.append(k)
    for x in o:
        for y in o:
            al.append(x+y)
            al.append(x*y)
al.sort()
al2=[]
for k in al:
    if k not in al2:
        al2.append(k)
al2=al2[0:63]
makel_d={}
bd=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '#', 'm', 'n', '/', '+', '-', 'r', 's', '^', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', '$', 'U', 'V', 'W', '%', 'Y', 'Z', '1', '2', '3', '4', '*', '6', '7', '8', '9', '0']
l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
for k in range(0,63):
    makel_d[al2[k]]=l[k]

f=input("Enter your text: ")

Keydic={}
for u in range(1,64):
    tp=''
    tp=tp+str(bd[random.randrange(0,62)])
    tp=tp+str(bd[random.randrange(0,62)])
    tp=tp+str(bd[random.randrange(0,62)])
    tp=tp+str(bd[random.randrange(0,62)])
    Keydic[l[u-1]]=tp
Non_conv_char=['X','@','l','T','%','t','&','5','(',')','o','q','p','=',';',':']
for y in makel_d.keys():
    makel_d[y]=Keydic[makel_d[y]]
for k in range(0,len(f)):
    if k in makel_d.keys():
        makel_d[k]=makel_d[k]+"."+Keydic[f[k]]
    else:
        makel_d[k]=Keydic[f[k]]
for k in range(0,max(makel_d.keys())):
    dmn=''
    if k not in makel_d.keys():
        dmn=dmn+str(Non_conv_char[random.randrange(0,16)])
        dmn=dmn+str(Non_conv_char[random.randrange(0,16)])
        dmn=dmn+str(Non_conv_char[random.randrange(0,16)])
        dmn=dmn+str(Non_conv_char[random.randrange(0,16)])
        makel_d[k]=dmn
for k in range(0,max(makel_d.keys())+1):
    if len(makel_d[k])==4:
        dmn=''
        dmn=dmn+str(bd[random.randrange(0,16)])
        dmn=dmn+str(bd[random.randrange(0,16)])
        dmn=dmn+str(bd[random.randrange(0,16)])
        dmn=dmn+str(bd[random.randrange(0,16)])
        makel_d[k]=makel_d[k]+"."+dmn
fnl=''
for g in al2:
    k=makel_d[g]
    f=''
    f=k[-4:]+"."+k[0:4]
    makel_d[g]=f
makel_d=dict(sorted(makel_d.items()))
k=list(makel_d.values())
for x in k:
    fnl=fnl+x
ftr=''
ftr1=''
for k in o:
    ftr=ftr+str(dTB(k))+"'"
ftr=ftr+'.'
o_n=['1','3','5','7','9']
e_n=['0','2','4','6','8']
for bruh in ftr:
    if bruh == '0':
        ftr1=ftr1+e_n[random.randrange(0,4)]
    elif bruh == '1':
        ftr1=ftr1+o_n[random.randrange(0,4)]
    else:
        ftr1=ftr1+bruh
fnl=ftr1+fnl

#pc.copy(fnl)
#print(fnl)
fname=input("Enter path and filename (without extension): ")
f=open(fname+".JE2F",'wb')
pickle.dump(fnl,f)
f.close()
