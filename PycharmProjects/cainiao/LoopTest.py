for i in range(1,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))

count = 0
while True :
    print('repeat')
    count  = count + 1
    if count > 5:
        break

for i,j in zip(range(1,10),range(1,10)):
    print('{} + {}'.format(i,j))