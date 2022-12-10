import emoji
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Boom!', end=' ')
print(emoji.emojize('\033[1;31m:fireworks:\033[m') * 3)
