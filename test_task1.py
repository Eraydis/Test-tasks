#Имеется функция StringChallenge(strArr), использующая параметр StrArr, который содержит только один элемент, возвращая строку true, если это валидное число, которое содержит только цифры с правильно расставленными разделителями и запятыми, а обратном случае возвращает строку false



import re
def StringChallenge(strArr):
     pat = re.compile(r'^[0-9]*[.,]{0,1}[0-9]*$')

     for i in strArr:
             if pat.match(i):
                     return('true')
             else:
                     return('false')

             pass

a = input()

print(StringChallenge(a)