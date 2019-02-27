L=['samovar','vesna','leto']
import random
f=random.choice(L)
f1 = f.replace(random.choice(f), "?")
print(f1)
i=input("place answer here ")
if i==f:
    print('yup')
else:
    print('nope')
