my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = (1, "Hello", 3.4,1)
print(my_tuple)

my_tuple = ('p','e','r','m','i','t')
print(my_tuple[0])   
print(my_tuple[5])   

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_tuple[0][3])       
print(n_tuple[2][2])    
print(n_tuple[1][1]) 

print("Sliced :", my_tuple[1:4])

for letter in n_tuple:
    print("Hello", letter)

t1=(10,20,20,50,80,50,20)
print(t1.count(20))    