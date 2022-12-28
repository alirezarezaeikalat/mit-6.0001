1. new Computers are machines that: 

    a. can store sequence of instructions
    b. can execute the sequence of instructions
    c. we can change the sequence of instructions

2. Basic machine architecture:

      Memory (contains bunch of data, and the sequence of instructions)

      CPU (interaction with ALU, is a instruction counter, loads instruction from memory and send it ALU)                 
      
      ALU(do primitive operations like addition, subtraction, ... it might get data from memory or store data in memory)
        ALU can do set of --primitives--
          a. arthmetic and logic
          b. simple tests
          c. moving data
          
      Input         Output

3. Alan Turnin showed that you can compute anything with 6 --primitives-- and piece of tape: 

        a. move left
        b. move right
        c. read
        d. write
        e. scan
        f. do nothing

  all programming languages created more convenient set of --primitives-- like in pythons we have numbers, strings, simple operators


4. in python everything is a --object--, and each object has a type, and this type tell python what operations you can do on this object.

5. There are two kind of objects in python:

      a. --scalar objects--- : can not be subdivided

          int, float, bool, NoneType (special and has one value None),

          you can use type conversion in pythone:
            float(3) convert int 3 to 3.0
            int(3.9) convert float 3.9 to integer 3 

      b. --non scalar objects-- : can be subdivided


[ATTENTION] [VERY IMPORTANT] [This is true for non mutable objects]
in python everything is a object, so for example when you have (radius = 2) radius is a object, and if you assign a new value to radius
like (radius = 3) you actually gives new address for radius pointer, and you lost the handle for 2 in the memory, but 2 is still in 
memory, and in some time, garbage collector will collect this 2 value in the memory that has no handle.


6. using , in print function add space between separate inputs

7. to get input from the user in python we use input function: 

      text = input("please write something")       // text is a string
      num = int(input("please write something"))

8. you can not compare strings with int or float in python

       x = "a" > 5            (you will get an error)

9. (and or) are logical operators in python

10. codeblocks in python define by indentation:

      if <condition>:
            <expression>
            <expression>
      elif <condition>:
            <expression>
      else:
            <expression>

11. while loop:

      while <condition> :
            <expression>

12. for loops:

      (variable starts at 0)
      for <variable> in range(<sum>):     range(start, stop, step)
            <expression>

13. Strings in python:

      a. s = "sdfa"
            len(s)

      b. you can use indexing in strings (negative or positive)

      s[0] => s
      s[-1] => a
      s[-2] => f

      c. you can use slice of strings in python:

            s[start:stop:step]
            s[1:3]       "df"
            s[::]       same as [0:len(s):1]
            s[::-1]     same as [-1: -(len(s + 1)): -1]

[ATTENTION]
14. strings are immutable:
      s = "hello"
      s[0] = "y"  => this gives an error
      s = "y" + s[1:len(s)] => is allowed, because now s is bound to new object

15. for loops used in python as for loops and foreach:

      (strings)
      for char in s:
            if char == "i" or char == "u":
                  print("There is i or u in this string")

16. investigating three algorithms to for finding cube root:

      a. guess and check method:

            cube = 8

            for guess in range(cube + 1):
                  if guess**3 >= cube
                        break
            
            if guess**3 != cube :
                  print("The cube is not a perfect cube")
      
            else:
                  if cube < 0:
                        guess = -guess
                  print("cube root of " + str(cube) + " is " + str(guess))
      
      b. good enough answers:

            cube = 27
            #cube = 8120601
            #cube = 10000
            epsilon = 0.1
            guess = 0.0
            increment = 0.01
            num_guess = 0

            while abs(guess**3 - cube) >= epsilon and guess <= cube :
                  guess += increment
                  num_guess += 1
            print("num_guess =", num_guess)
            if(abs(guess**3 - cube) >= epsilon) :
                  print("Failed on cube root of", cube, "with these parameters")
            else:
                  print(guess, "is close to the cube root of", cube)
      
      c. bisection search:

            cube = 27
            epsilon = 0.1
            num_guesses = 0
            low = 0
            high = cube
            guess = (high + low) / 2
            while abs(guess**3 - cube) >= epsilon :
                  if guess**3 < cube
                        low = guess
                  else :
                        high = guess
                  guess = (high + guess) / 2
                  num_guess += 1
            
            print("num_guess", num_guess)
            print(guess, "is close to the cube root of", cube)

17. we can define function in python, each function has:

      a. name
      b. parameters(0 or more)
      c. doc string
      d. body

      def is_even(i)
            """
            Input: i is a positive int
            Returns true, if i is even, otherwise false
            """
            print("inside is_even")
            return i%2 == 0

[ATTENTION]
If you don't specify the return type, python will make it for you, it is NoneType, and its value is None.

18. Everything in python is object, so, functions are objects too, and you can treat functions like other objects, for example you can
      use them as arguments in other functions

[VERY IMPORTANT]
19. In python you can access global variables in functions, but you can't modify global variables inside functions.

20. In python every function has a seperate scope, and when you pass a argument to a function, the function makes new variable 
      in the function scope (call by value)

[ATTENTION]
21. the scope of function is completely separated from the main program, and this scope created when you --call-- the function

22. Compound data types:

      a. tuples: tuples are the sequence of types, 
            [ATTENTION]
            tuples are immutable, and if you try to change the value of the element you will gets an error

            te = ()   empty tuple
            t = (2, "mit", 3)

            t[0]   will gets 2
            (2, "mit", 3) + (5, 6)   -> (2, "mit", 3, 5, 6)
            t[1:2]  gives ("mit",)  the last comma is neccessary, because without comma it is just a string not tuple
            t[1:3]  gives ("mit", 3)
            len(t)      gives 3
            t[0] = 4          will gives an error because tuples are --immutable--

            -use case of tuples: 
                  1. for example if you want to swap the value of x and y, with out tuples you have to use temp variable but with tuple
                  you can use this:
                        (x, y) = (y, x)
                  
                  2. return more than one object from functions
            
            -example of using tuples: 

                  the input to the function should be ((string, int), (), ..., ())

                  def get_data(aTuple) :
                        nums = ()
                        words = ()

                        for t in aTuple:
                              nums = nums + (t[0],)
                              if t[1] not in words:
                                    words = words + (t[1],)
                        min_n = min(nums)
                        max_n = max(nums)
                        unique_words = len(words)
                        return (min_n, max_n, unique_words)
            
      b. Lists: they are just like tuples, but lists are mutable (you can change the value of elements)

            le = []
            l = [2, 'a', 4, ['a', 4]]
            len(l)  gives 4
            l[0]   gives 2
            l[1] = 5     doesn't give an error 
                  [ATTENTION]
                  this operation doesn't create new space in the memory for the list, it just change the element
            
            add elements to the list with .append()
            this way we mutate the list, in tuples we make new space when we add element to the tuple

            l.append(6)       (mutate the list)

            l3 = l1 + l2      (this operation does not mutate the list)

            l1.extend(l2)     (extend mutate the l1 function)

            del(l1[4])        (deletes the element at position 4)

            l1.remove(3)      (remove the value 3 from the list) (remove the first ocurrance of 3)

            l1.pop()          (remove the last element)         

            s = "I<3 cs"
            list(s)     will return       ['I', '<', '3', ' ', 'c', 's']
            s.split('<')      will return ['I', '3 cs']
            L = ['a', 'b', 'c']
            ''.join(L)  will return 'abc'
            '_'.join(L)       will return "a_b_c"

            L1 = sorted(L)         will return the sorted list, does not mutate the L

            L.sort()          will sort the L, and mutate the list

      [ATTENTION] [VERY IMPORTANT]
      you can have more than one pointer only to mutable objects. so for example you can have two pointer that pointing to one list.
      but in tuples:

            x = y   (it makes a copy of y and assign it the x)
      
      if you want to copy a list you have to use cloning

            x = y[:]
      
      [VERY IMPORTANT]
      example: 
            warm = ["yellow", 'orange']
            hot = ['red']
            brightcolors = [warm]         brightcolor is a list of pointer
            brightcolors.append(hot)      add another pointer to brightcolors
            print(brightcolors)           // [["yellow", "orange"], ["red"]]
            hot.append("pink")
            print(hot)                    // ["red", "pink"]
            print(brightcolors)           // [["yellow", "orange"], ["red", "pink"]]

23. recursion is taking a problem and reducing it to a smaller version of the same problem

      Algorithmcally: a way to design a solution to a problems by divide and conquer
                        reduce a problem to a simpler versions of the same problem.
      
      semantically: a programming technique where a function calls itself
            in programming, goal is to not have infinite recursion

            must have a 1 or more base cases that are easy to solve

      
      example: 

            multiplying by just using adding:

            first way: 

                  def mult_iter(a, b) :
                        result = 0
                        while b > 0:
                              result += a
                              b -= 1
                        return result
            
            second way(recursion):

                  (this is the idea)
                  a = a * b = a + a * (b - 1)

                  def mult(a, b):
                        if b == 1:
                              return a
                        else:
                              return a + mult(a, b - 1)

            
      example 2:

            def factorial(a):
                  if a == 0:
                        return 1
                  else: 
                        return a * factorial(a-1)
      
      [ATTENTION] [VERY IMPORTANT]
      a. each recursive call to a function creates its own scope
      b. flow of control passes back 

      example 3: move stacks of tower to another tower

            def print_move(from, to):
                  print('move from ' + str(from) + ' to ' + str(to))
            
            def towers(n, from, to, spare):
                  if n == 1:
                        print_move(from, to)
                  else:
                        towers(n-1, from, spare, to)
                        towers(1, from, to, spare)
                        towers(n-1, spare, to, from)
      
      example 4: 
      at first there are two rabits, the female, and the male, and after a month the rabits will gets mature, and the female rabit will
      be pregnant, after the second month the female rabit, produces the pair, what is the count of female rabits after n month?

      fib(n) = fib(n-1) + fib(n-2)  

      def fib(n):
      """ assume n int >= 0
      returb fib of n"""
            if n == 1 or n == 2:
                  return 1
            else:
                  return fib(n-1) + fib(n-2)
      
      example 5:
      find out if the string is palindrome:

      def is_palindrome(s):
            def to_chars(s):
                  ans = 
                  for c in s:
                        if c in "abcdefghijklmnopqrstiuvwxyz":
                              ans += c
                  return ans
            
            def is_pal(s):
                  if len(s) <= 1:
                        return True
                  else:
                        return s[0] == s[-1] and is_pal(s[1:-1])
            
            return is_pal(to_chars(s))

24. Dictionaries in python:

      my_dict = {}   empty dictionary
      grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A'}

      grades['Ana']     will give 'B'

      grades['ghasem']        will give key error

      grades['abbas'] = C     add to dictionary

      'ahmad' in grades       returns False

      del(grades['Ana'])      will delete Ana

      grades.keys()           will return an --iterable-- something like tuples, but order is not gauranteed

      grades.values()         will return an --iterable-- but order is not gauranteed

      [ATTENTION]
      dictionary itself is mutable
      values can be anything, any type, mutable or immutable
      but the keys should be unique and immutable types

      example 1:
            def lyrics_to_frequencies(lyrics):
                  """ lyrics is the list of strings ""
                  myDict = {}
                  for word in lyrics:
                        if word in myDict:
                              myDict[word] += 1
                        else:
                              myDict[word] = 1
                  return myDict

      example 2:
            def efficient_fib(n, d):
                  
                  if n in d:
                        return d[n]
                  else:
                        ans = efficient_fib(n-1) + efficient_fib(n-2)
                        d[n] = ans
                        return ans
            
            d = {1:1, 2:1}
            print(efficient_fib(6, d))

25. To make a test, you have to have program that runs, and you can test the program with sets of inputs and expected output.

      There are three classes of tests that you can do:
      
      a. Unit testing: for example if you write a function, unit testing just make sure each function runs according to its specification

      b. Regression testing: adds test for the set of inputs that found bugs in them, and fix the bugs, and run tests for all 
            of your inputs to makes sure that when you fixed the bugs, you don't add new bugs to the systems
      
      c. Integration testing: test your program as a whole.

26. There multiple approaches to testing:  

      a. --intuition-- about natural boundries to the problem

      b. if the problem has no natural boundries, you can do --random testing--

      c. --black box tesing-- : explore paths through specification (doc string), you don't have to code

      d. --glass box testing--: explore paths through the code

      example of black box testing: 

            def sqrt(x, eps):
                  """ Assumes x, eps float, x>=0 , eps > 0
                  Returns res such that x-eps<= res*res <x+eps """
            
            case                    x                       eps

            boundry                 0                       0.0001
            perfect square          25                      0.0001
            less than 1             0.05                    0.0001
            irrational square root  2                       0.0001
            extreme                 2                       1.0/2.0**64.0
            extreme                 1.0/2.0**64.0           1.0/2.0**64.0
            extreme                 2.0**64                 1.0/2.0**64.0
            extreme                 1.0/2.0**64.0           2.0**64
      
      example of glass testing:
            we use code directly to design a test case.

            called --path-complete-- if every potential path through code is tested at least once.

            drawbacks glass box testing:
                  a. can go through loops arbitrary many times
                  b. missing paths

            there are some --guidelines-- for glass box testing:

                  branches: excersice all parts of a conditional
                  loops: loop not entered/body of loops executed only once/body of loops executed more than once
                  while: same as loops, cases that are catch always exit loop
            
            def abs(x):
                  """ Assumes x is an int
                  Return x if x>=0 and -x otherwise """
                  if x < -1:
                        return -x
                  else: 
                        return x
            
            [ATTENTION]
            path-complete test set could miss a bug, for example in this example, -1 returns -1,
            so, it is very important that in path-complete test, we examine the boundries.

            [ATTENTION]
            A very important point in debugging is to be --systematic--

27. There are some tools that you can use for debugging:

      a. for example python tutor is very good
      b. print statement (a good use case of print statement is using bisection method for using print)


28. Do and Don't and testing and debuging:

      Don't                                                       Do
      write entire program                                  write a function
      test entire program                                   Test a function, debug a function
      debug entire program                                  write another function
                                                            test function, debug function
                                                            .....
                                                            do integration test

29. some type of errors (exceptions)

      a. SyntaxError: python can't parse program

      b. NameError: local or global name not found

      c. AttributeError: attribute reference fails

      d. TypeError: operand doesn't have correct type

      e. ValueError: operand type okay, but value is illegal

      f. IOError: IO system reports malfunction (e.g. file not found)

      example:
      try:
            a = int(input("tell me one number"))
            b = int(input("tell me another number")) // it is possible to produce value error
            print(a/b)
      except:
            print("bug in user input")
      
      example 2: 
      
      try:
            a = int(input("tell me one number"))
            b = int(input("tell me another number")) // it is possible to produce value error
            print(a/b)
      except ValueError:
            print("could not convert to int")
      
      except ZeroDivisionError:
            print("can't divide by zero")
      
      except:
            print("Something went wrong")

30. there are other exceptions blocks:

      else:
            will execute if the try block doesn't produce any error
      

      finally:
            body of this --always executed-- after try, else, and except blocks even if they raised another error or execute the 
            break, continue, or return 

31. you can raise your exception in python:
      
      raise Exception("")

      raise ValueError("")

      example 1:

      def get_ratios(L1, L2):
            """ Assume L1 and L2 are the list of equal length of numbers
                  Returns a list containing (L1(i)/L2(i)) """
            ratios = []
            for i in rang(len(L1)):
                  try:
                        ratios.append(L1(i)/L2(i))
                  except ZeroDivisionError:
                        ratios.append(float("nan"))   #nan: not a number
                  except:
                        raise ValueError("problem with the args")
            return ratios      


32. Assertion:
      example 1:

            def avg(grades):
                  assert not len(grades) == 0, 'no grades data'
                  return sum(grades)/len(grades)
            
            if the grades is empty, it will gives AssertionError

33. Object oriented programming in python:

      // object is the parent class
      class Coordinate(object):
            # attributes of the class
            def __init__(self, x, y):     # the first parameter, is always the instance
                  self.x = x              # self is naming convention
                  self.y = y
            def distance(self, other):
                  """ other is another 
                  Coordinate instance"""
                  x_diif_sq = (self.x - other.x)**2
                  y_diff_sq = (self.y - other.y)**2
                  return (x_diif_sq + y_diff_sq)**0.5
            def __str__(self):
                  return "<" + str(self.x) + "," + str(self.y) + ">"

      c = Coordinate(4, 3)
      zero = Coordinate(0, 0)

      dis = c.distance(zero)        // this equivalant to Coordinate.distance(c, zero)

34. when you print(c), you will get a message like this:

      <__main__.Coordinate object at 0x7fa918510488>

      you can change the print value of c, by definin __str__ function that returns string in your class:
      
      print(c)          # will return <3,4>

      print(type(c)) and print(Coordinate)      # will print <class __main__.Coordinate>

[ATTENTION]
__main__ is the scope of the running program, when you run a program file directly first python fill the __name__ variable with "__main__"
but if you import the module to another python file, the __name__ variable in imported file will be the file name

35. There are other special functions in a class that we can use to overload operators or special functions, for examine:

      __add__(self, other)    -> self + other (or we can use it like c.__add__(c2))

      __sub__(self, other)    -> self - other   

      __eq__(self, other)     -> self == other

      __lt__(self, other)     -> self < other

      __len__(self)           -> len(self)      (or we can use it like c.__len__())     


36. Inheritance in python:

      # you can add methods and data to child class or override the methods of parent class

      class Animal(object):
            def __init__(self, age):
                  self.age = age
            
            def set_name(self, name = ""):
                  self.name = name

            def __str__(self):
                  return "Animal with a" + self.name + ""
      class Person(Animal):
            def __init__(self, name, age):
                  Animal.__init(self, age)
                  self.set_name(name)
                  self.friends = []

37. class variables:

      you can access class variables with class name

      class Rabit(Animal):
            tag = 1
            def __init__(self, name):
                  self.name = name
                  self.Rid = Rabit.tag
                  Rabit.tag += 1
      

38. In other lectures we will talk about efficiency:

      There are three problem that we want to solve:

            a. how can we reason about --an-- algorithm in order to predict the amount of time it will need to solve a problem of a 
                  particular size.
            
            b. how can we relate choices in algorithm design to the time efficiency of the resulting algorithm

            c. are there any fundamental limits on the amount of time that we need to solve a problem.

      
39. There are some ways that we can measure algorithm efficiency:

            1. we can use scientific approach, run the algorithm and time the run time.

                  import time 
                  
                  def c_to_f(c):
                        return c*9.5 + 32
                  
                  t0 = time.clock()
                  c_to_f(1000)
                  t1 = time.clock() - t0

            this approach:
                  a. times vary between different algorithm (this ok)
                  b. running time varys between impelementation, for example for loop vary with while loop (this is not ok)
                  c. running time varys between computers (this is not ok)
                  d. running time is not predictable on small inputs

            2. we can count the opertation, like counting mathematical operations, retrieving data, settign variables, ...

                  assume these operations take --constant time-- :

                        a. mathematical operations
                        b. comparisons
                        c. assignments
                        d. accessing objects in memory
                  
                  -it is depends on algorithm (this is ok)
                  -running time varys between impelementation, for example for loop vary with while loop (this is not ok)
                  -running time does not vary between computers (this is ok)

            3. abstract the second approach to the order of the growth:
                  the efficiency of the algorithm is depend on the input.

                  def search_for_elmt(L, e):
                        for i in L:
                              if i == e:
                                    return True
                        return False
                  
                  for example in this example the --base case scenario-- is 1 and the --worst case scenario-- is n

                  [VERY IMPORTANT]
                  we focus on the --worst case scenario-- because it gives the --upper bound to the amount of the time-- that is needed for
                        the program
                  
                  and in the --worst case-- we look for the larget factor in the run time (which piece of the code, take more time)
                  and by counting the worst case and counting on the largest factor, we gets the upper bound for the program run time

                  (we call the big o notation)

40. to analyze the order of growth of the code, we have analyze each chunk of code separetely:

      a. law of --addition--: 
            law of addition used with sequential statements
            
            O(f(n)) + O(g(n)) = O(f(n) + g(n))

            example:
            
            for i in range(n):
                  print('a')              # this one is O(n)
            for i in rang(n*n):
                  print('a')              # this one is O(n^2)

                                          # O(n) + O(n*n) => O(n*n)
      
      b. law of --multiplication--:

            law of multiplication is used for --nested statements--

            example:

            for i in range(n):
                  for j in range(n):
                        print('a')

            O(n) * O(n) = O(n*n)

41. Complexity classes:

      O(1): denotes constant runtime
      O(logn): denotes logarthmic runtime (produce problem in half each time)
      O(n): denotes linear runtime (simple iterative or recursive)
      O(n logn): denotes log-linear runtime 
      O(n ^ c): denotes polynomial runtimes (nested loops or recursive calls)
      O(c ^ n): denotes exponential runtime (multiple recursive calls at each level)

41. example of complexity calculation:

      a. Linear search on Unsorted list

            def linear_search(L, e):
                  found = False
                  for i in range(len(L)):
                        if L[i] == e:
                              found = True
                  return found
      
      This example takes linear time O(n), but there is hidden assumption in this, and this hidden assumption is that, retrieving data
      from a list takes constant time.

      [VERY IMPORTANT]
      If you have list of integer, all the spaces are the same amount, and you can get to the any element in constant time, but what if
      you have list that are hetrogenous, but python in the list, doesn't store the actual value, it stores the pointer to the memory
      that stores that actual value, so even in hetrogenous list, we can retrieve data in constant time.


      b. linear search on sorted list:

            def linear_search(L, e):

                  for i in range(len(L)):
                        if L[i] == e:
                              return True
                        if L[i] > e:
                              return False
      
      the average run time is faster, because it is possible that you don't have to search for e in all the list elements, but the order
      of growth is again linear, because in worst case, you have to search for e in all list elements.

      c. bisection search on sorted list:

            def bisection_search(L, e):

                  if len(L) == 0:
                        return False            # here is constant time
                  elif len(L) == 1:
                        return L[0] == e        # here is constant time
                  else:
                        half = len(L) / 2       # here is constant time
                        if L[half] > e:
                              return bisection_search(L[:half], e)      # but here we copying the list with the size of n, n/2, n/4, ...
                        else: 
                              return bisection_search(L[half:], e)

            
            here we have O(logn) call for the function, but each function has a copying, so O(logn) * O(n) = O(logn * n)


            [ATTENTION]
            it is possible to avoid copying the list and make the bisection search logarthmic.

            def bisection_search(L, e):
                  def bisection_search_helper(L, e, low, high):
                        if high == low:
                              return L[low] == e
                        mid = (low + high) // 2       #// means divide with integral result 
                        if L[mid] == e:
                              return True
                        elif L[mid] > e:
                              if mid == low:
                                    return False
                              else:
                                    return bisection_search_helper(L, e, low, mid - 1)
                        else:
                              return bisection_search_helper(L, e, mid + 1, high)
                  
                  if len(L) == 0:
                        return False
                  else: 
                        return bisection_search_helper(L, e, 0, len(L) - 1)
      
      d. convert int to string:

            def int_to_string(i):
                  digits = '0123456789'
                  res = ''
                  while i > 0:
                        res = digits[i%10] + res
                        i = i // 10
                  return res
            
            # all the operations are constant time, and the loop is logarthmic, so the complexity of this algorithm is O(logn)
      
      e. factorial function in direct way and recursive way

            def factorial(n):
                  prod = 1
                  for i in range(1, n+1):
                        prod *= i
                  
                  return prod
            
            # there is constant time inside loop, and we loop through it n times, so the time complexity is O(n)
      

            def factorial(n):
                  """ assume n >= 0 """
                  if n<= 1:
                        return 1
                  else:
                        return n * factorial(n-1)
            
            # all the operations are constant time, and we call the function n time, so the time complexity is O(n)
      
      f. polynomial order of growth usually happens when we have loop inside another loops that all of them depends on the problem size


      g. example of exponential order of growth:

            recursive functions where more than one recursive call for each size of problem
                  tower of Hanoi

                  complexity of the tower of Hanoi:

                        tn: denotes time to solve the tower of size n

                        tn = 2tn-1 + 1
                           = 2(2tn-2 + 1) + 1
                           = 4tn-2 + 2 + 1
                           = 8tn-3 + 4 + 2 + 1
                           = 2^k tn-k + 2^(k-1) + 2^(k-2) + ... + 2 + 1
                           = 2^(n-1) + 2^(n-2) + ... + 2 + 1
                           = 2^n - 1  
                        

      h. generate subsets of set:

            def genSubsets(L):
                  if len(L) == 0:
                        return [[]]
                  
                  smaller = genSubsets(L[:-1])  # all subsets without last element
                  # this recursive call will be calling n times
                  extra = L[-1:]          # generate a list with only last element
                  new = []
                  for small in smaller:
                        new.append(small+extra)
                  
                  return smaller+new


            analyzing the time complexity of this algorithm:

            
             def genSubsets(L):
                  if len(L) == 0:               # this is constant time
                        return [[]]
                  
                  smaller = genSubsets(L[:-1])  # this will call itself n times
                  extra = L[-1:]  # this is constant        
                  new = []          # this is constant
                  for small in smaller:               # time of the problem is to solve smaller problem + time to make a copy of smaller
                                                                                                            solution (this is exponentialy)
                                                                                                            2^k
                        new.append(small+extra) # this is constant
                  
                  return smaller+new


                  tn: denotes time to solve problem of size n

                  sn: denotes the size of solution of for problem of size n

                  tn = tn-1 + sn-1 + c
                     = tn-1 + 2^(n-1) + c 
                     = tn-2 + 2^(n-2) + c + 2(n-1) + c
                     = tn-k + 2^(n-k) + ... + 2^(n-1) + kc
                     = t0 + 2^0 + ... + 2^(n-1) + nc
                     = 1 + 2^n + nc
      
      i. fibonacci:

            def fib_iter(n):
                  if n == 0:
                        return 0          # this is linear
                  elif n == 1
                        return 1
                  else:
                        fib_i = 0
                        fib_ii = 1
                        for i in range(n-1):
                              tmp = fib_i
                              fib_i = fib_ii
                              fib_ii = temp + fib_i
                        returb fib_ii

42. Searching and sorting:

      linear search:
            the complexity of this is O(n)
      
      bisection search:
            the list must be sorted, to give the correct answer.
            There are two different implementation of this algorithm, one of them is O(logn)

      
            [ATTENTION]
            you can not sort the list, with less than O(n), because at least, you have to see each element of the list once.
            but sometimes, if you want to operate multiple search in a list, you can sort it once, and then use bisection search multiple
            times, so in this way it is more effficient to use bisection search on a unsorted list that linear search
      
      a. bubble sort:
            in this sort, you go through the list, and takes the bigger element to the end of list in turn:

            def bubble_sort(L):
                  swap = false
                  while not swap:
                        swap = true
                        for j in range(n-1):
                              if L[j-1] > L[j]:
                                    swap = false
                                    tmp = L[j-1]
                                    L[j-1] = L[j]
                                    L[j] = tmp
            
            The complexity of this algorithm is O(n^2)
      
      b. Selection sort:

            first step: 
                  swap elements with index 0 to find the min
            
            subsequent step:
                  in remaining sublist, extract the minimum
                  swap it with the element at position 1
            
            Proof that selection sort will sort the list:

            loop invariant: given prefix of L[0:i] and suffix L[i+1: len(L)] then prefix is sorted and no element in the prefix
            is larger that smallest element in the prefix

            proof by induction:

                  base case: the prefix is empty so the base case is true.
                  
                  inductive step: P(n): prefix L[0:n] is sorted and no element in the prefix is larger than the smallest element
                  in the suffix

                  P(n+1): move minimum element in the suffix and append it to the prefix, since P(n) is true, so the prefix is 
                        still sorted, and because we append the minimum element of the suffix, no element in the prefix is larger
                        than the smallest element in the suffix.
            
            def selection_sort(L):
                  suffixSt = 0
                  while suffixSt != len(L):
                        for j in range(suffixSt, len(L)):
                              if L[j] < L[suffixSt]:
                                    L[suffixSt], L[j] = L[j], L[suffixSt]
                        
                        suffixSt += 1
            
            the complexity is quadratic
      
      c. merge sort:

            this is based on divide and conquer solution: divide the list until you have list with 1 element, and merge
            two list to have sorted lists with two elements and so on ...

            def merge(left, right):
                  i, j = 0, 0
                  result = []
                  while i < len(left) and j < len(right):         
                        if left[i] < right[j]:
                              result.append(left[i])
                              i += 1
                        else: 
                              result.append(right[j])
                              j += 1
                  while i < len(left):
                        result.append(left[i])
                        i += 1
                  while j < len(right)
                        result.append(right[j])
                        j += 1
            
            O(len(left) + len(right)) copied elements
            O(len(longer list)) comparison


            def merge_sort(L):
                  if len(L) < 2:
                        return L[:]
                  else:
                        middle = len(L) // 2
                        left = merge_sort(L[:middle])
                        right = merge_sort(L[middle:])
                        return merge(left, right)

            [ATTENTION]
            There are logn level in merge sort (each time we divide problem into half) and in each step, we use n copying of elements
            so the complexity is O(nlogn)
                    n
            
            n/2         n/2
      
      n/4       n/4  n/4     n/4
                  .
                  .
                  .
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 

43. Last but not least:

      computational thinking is all about:

            abstraction      algorithms        and automation


44. Things that I've learned from working with python:

      a. you can change the setting of vs code, using interface or setting.json file. you can set User setting or 
            workspace setting, There is option that if you make it true you can see default settings beside user setting:
            
             "workbench.settings.useSplitJSON": true,
      
      b. you can choose your python interpreter bellow the vs code.

      c. you can findout which python or pip you are running by using:

            which python      or which pip

            [ATTENTION]
            but if you are using alias, you have to use:

            type python (to find the alias, then use type <alias>)
      
      d. useful string functions:

            'A'.lower()   //this returns 'a'
            '4'.isalpha() //this returns false

            import string
            print(string.ascii_lowercase)  // this returns all the lowercase letters

45. Working with dictionaries in python: 

      a. you can use get function with a dictionary to get a value for a certain key in dictionary.

            sampleDic.get(key, defaultValue)          if you don't specify the default value, it will retrun None


--------------- Very important concept in python and in OS -----------

46. you can see the folders that your terminal commands looks for executable binaries:

      >> echo $PATH

47. First you can see the actual python and pip you are using, This even shows aliases:

      >> type python
      
      >> type pip

48. you can run python and see the places that this version of python looking for importing 
      import sys
      print(sys.path)

49. you can see your install packages: 
      
      >> pip list

      then you can use one of the packages to see the location where pip install its packages:
      
      >> pip show <packagename>