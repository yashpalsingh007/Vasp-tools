f= open('POSCAR_mod', 'r')

s1= f.readline()
s2= f.readline()
s3= f.readline()
s4= f.readline()
s5= f.readline()
s6= f.readline()
atom= s6.split()
kinds= len(atom)

s7= f.readline()
num_atom= s7.split()
s8= f.readline()

s= f.readlines()

f.close()

#charge allocation
chg= ['','','Vc']
cnt= 1
k= 1
i= 1

while k <= kinds:
        cnt = 1

        while cnt <= int(num_atom[k-1]):
			print s[i-1].rstrip('\n')
			s[i-1]= s[i-1].rstrip('\n')+' %s' % (chg[k-1])+ '\n'
			print s[i-1]
			i+= 1
			cnt+= 1
        k+= 1

#remake POSCAR
j=1
s_l= ''
while j <= len(s):
        s_l += s[j-1]
        j+= 1
   

s_str= s1+ s2+ s3+ s4+ s5+ s6+ s7+ s8+ s_l

f= open('POSCAR_mod', 'w')
f.write(s_str)
f.close()
