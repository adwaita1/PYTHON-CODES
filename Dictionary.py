D={}
D['name']='Adwaita'
D['age']=22
D['color']='dusky'

print(D)
#{'name': 'Adwaita', 'age': 22, 'color': 'dusky'}
D['height']='5.2"'
print(D)
#{'name': 'Adwaita', 'age': 22, 'color': 'dusky', 'height': '5.2"'}

#sorting based on keys 

Ks=list(D.keys())
L=Ks.sort()
print(Ks)
for key in D:
    print(key, "==>" ,D[key] )
#name ==> Adwaita
#age ==> 22
#color ==> dusky
#height ==> 5.2"

#other way to sorting in one step using function sorted
print("*****************Using sorted function***********************")
for key in sorted(D):
    print(key,"==>",D[key])
#*****************Using sorted function***********************
#age ==> 22
#color ==> dusky
#height ==> 5.2"
#name ==> Adwaita

print(D['name'])
#Adwaita
print('name1' in D)
#false
value=D.get('name',0)
print(value)
#Adwaita
value=D.get('name1',0)
print(value)
#0
value=D['age'] if 'age' in D else 0
print(value)
#22
value=D['ageeeee'] if 'ageeeee' in D else 0
print(value)
#0

L={n:n **2 for n in [1,2,3,4]}
print(L)
#{1: 1, 2: 4, 3: 9, 4: 16}