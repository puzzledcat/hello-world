num = 1
string = '1'
print(num + int(string))

words = 'words' * 3
print(words)

word = 'a looooooong word'
num = 12
string = 'Bang!'
total = string * (len(word) - num)
print(total)

#slide
name = 'My name is Wally'
print(name[0])
print(name[-4])
print(name[11:14])
print(name[5:])
print(name[:5])

#method
phone_number = '186-1832-3810'
hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
print(hiding_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(search + ' is at ' + str(num_a.find(search)) + ' to num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to num_b')

print('{} a word she can get what she {} for'.format('with','come'))
print('{p} a word she can get waht she {v} for'.format(p='with', v='come'))
print('{0} a word she can get waht she {1} for'.format('with', 'come'))
