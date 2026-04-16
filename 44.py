#Generatorlar generatorlar jardeminde dastur codlarin kompilyatcya qiliw


#Iterator


sanlar = [1, 2, 3, 4, 5]


#Misal

sanlar = [1,2,3,4,5,6]

I = iter(sanlar)

print(next(I))





#Generator


sanlar = (1, 2, 3, 4, 5)




#Misal

sanlar = (1,2,3,4,5,6)

I = iter(sanlar)

print(next(I))



#==================================

sanlar = [1,2,3]

i = iter(sanlar)

print(next(i))
print(next(i))
print(next(i))

#==================================

g = (i for i in range(1, 4))

print(next(g))
print(next(g))
print(next(g))
