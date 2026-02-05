# `x = [1, 2,3]
# y = x 

# a = 1000
# b = 10
# c = int('10')
# # print( a is b)
# # print( a == b)
# # print(b is c)
# print(b is c)
# print(b == c)`

# a = [1]
# print(id(a))

# a = [1, 2]
# print(id(a))

# x = [1, 2, 3]
# print(id(x))

# x.append(4)
# print(id(x))

# a = 10
# b = 4

# print(a & b)
# print(a | b)
# print(~a)
# print(a ^ b)

# ternary operator
# a, b = 10, 20
# min = a if a < b else b
# print(min)

# conditional statements
# age = 1
# if age >= 18:
#     print("Eligible")
# print("Sorry Not Eligibe")

# age = 25
# if age == 11:
#     print("child")
# elif(age == 19):
#     print("teenager")
# elif(age == 25):
#     print("adult")

# number = 2

# match number:
#     case 1:
#         print("one")
#     case 2 | 3 :
#         print("two or three")
#     case _:
#         print("unkown number")

# numb = 0
# while numb <= 3:
#     print(numb)
#     numb +=1

# while (True):
#     print("Hello World")

# a = 'Athif FAisal'
# for letter in a:
#     pass
# print(letter)

# a = [1, 2, 3]
# a.extend([4, 5])
# print(a)


# a = [1, 2, 3]
# a.append([4, 5])
# print(a)

# l = [1, 2, 3]
# a = l[::-1]
# print(a)

# t1 = (4,)
# print(type(t1))

# t = (1, 2, 3)
# a, b, c = t
# print(a)

# t = (1, 2, 3)
# print(id(t))
# t1 = (4,)
# t += t1
# print(id(t))
# print(t)

# l = (1, 2, 3, 4,5 ,6 )
# a, *b, c = l
# print(*b)

# emptry_set = set()
# print(emptry_set)
# emptry_set.add((1, 2, 3))
# print(emptry_set)

# a = {"name": 'Athif', "age": 21}

# # print(a["class"])
# a["c"] = 3
# print(a)

# lst = [1, 2, 2, 3]
# freq = {}
# for i in lst:
#     freq[i] = freq.get(i, 0) + 1

# print(freq)

# freq = {}
# for i in lst:
#     freq[i] = lst.count(i)
# print(freq)

# squares = {}
# for i in range(1, 6):
#     squares[i] = i * i

# squares = {i : i*i for i in range(1, 6)}

# print (squares)

# words = ["python", "java", "c"]

# w_l = {word: len(word) for word in words}
# print(w_l)

# result = {x: "even" if x %2 == 0 else "odd" for x in range(1, 11)}
# print(result)

# result = {x: "odd"  for x in range(1, 11) if x % 2 != 0}
# print(result)

# class Dog:
#     sound = "Bark"
# # dog1 = Dog() # Here dog 1 is the object created using the class Dog...
# # print(dog1.sound)

#     def __init__(self, name, type):
#         self.name = name
#         self.type = type

# dog1 = Dog("Toomy", "Canine")
# print(dog1.type)

# class EvenNumbers:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start > self.end:
#             raise StopIteration
#         value = self.start
#         self.start += 2
#         return value

# evens = EvenNumbers(2, 20)

# for i in evens:
#     print(i)
        

# l = [10, 20, 30, 40]

# class Fetch:
#     def __init__(self, l):
#         self.l = l

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         for i in self.l:
#             return i
    
# fetches = Fetch(l)
# for f in fetches:
#     print(f)


# lst = [10, 20, 30, 40]

# a = iter(lst)

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# def generator(i):
#     while i > 0:
#         yield i
#         i -= 1

# b = generator(5)

# for i in b:
#     print(i)

# def squares():
#     for i in range(1, 10):
#         yield i ** 2

# for s in squares():
#     print(s)

# names = ["Alice", "Bob", "Jonathan"]

# print(list(filter(lambda x: len(x) >= 5, names)))

# lst = ["1", "2", "3"]
# print(list(map(lambda x: int(x), lst)))

# from functools import reduce

# lst = [1, 2, 3]
# print(int(reduce(lambda x, y: x + y, lst)))

# keys = ["a", "b"]
# values = [1, 2]
# print(dict(zip(keys, values)))

# print(list(zip([1,2], [3,4], [5,6])))

# names = ["Alice", "Bob"]
# marks = [80, 90]

# for n, m in zip(names, marks):
#     print(n, m)



    







