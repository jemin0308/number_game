import random
from number_utils import *


while True:
    guess = get_number('1~100 사이의 수 : ', 1, 100)
    tries += 1
    if guess < answer:
        print('UP!')
    elif guess > answer:
        print('DOWN!')
    else:
        print('정답!', tries, '번 만에 맞혔습니다.')
        break
 
if best == 0 or tries < best:
    save_best('best.txt', tries)
    print('최고 기록 갱신! best.txt에 저장했습니다.')

