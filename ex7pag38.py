a=input("Introdu sirul de caractere: ")
s = a.upper()
#a)	 numărul de apariţii ale caracterului ’A’ în şirul S;
sm = 0
for i in s:
    if ord(i) ==65:
        sm+=1
print(sm)
#b) şirul obţinut prin substituirea caracterului ’A’ prin caracterul ’*’;
print(s.replace('A', '*'))
#c) şirul obţinut prin radierea din şirul S a tuturor apariţiilor caracterului ’B’
c = s.replace("B" , "")
print(c)
#d)	 numărul de apariţii ale silabei MA în şirul S;
print(s.count("MA"))
#e) şirul obţinut prin substituirea tuturor apariţiilor în şirul S a silabei MA prin silaba TA;
e = s.replace("MA", "TA")
print(e)
#f) şirul obţinut prin radierea din şirul S a tuturor apariţiilor silabei TO;
f = s.replace("TO", "")
#g)	 scrierea inversă a şirului S;
print(s[::-1])