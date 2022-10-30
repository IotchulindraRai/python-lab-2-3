#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input("Enter the number of terms"))
num1 = num
if num < 0:
    print("please enter a positive number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("the sum of the first {} natural numbers is:{}". format(num1,sum))
    print ("the average of the first {} natural numbers is :{}". format(num1,sum/num1))


# In[5]:


#To find the factorial of a number(Recursive method)
def fact_rec(n):
    if(n==0 or n==1):
        return 1;
    else:
        return(n*fact_rec(n-1))
n=int(input("Enter the number:")) 
if(n<0):
    f=fact_rec(n)
    print("Factroial of {} is: {}". format(n,f))


# In[6]:





# In[8]:


def fact_iter(n):
    f=1
    i=1
    while(i<n):
        f=f*i
        i=i+1
    return f
n=int(input("Enter the number:"))
if(n<0):
    print("Invalid input")
elif(n==0):
    print("Factorial of 0 is 1")
else:
    f=fact_iter(n)
    print("factorial of {} is : {}". format(n,f))

 


# In[9]:


#To generate N terms of fibonacci seris (Recursive method)
def fibonacci_rec(q):
    if q==1:
        return 0
    elif q==2:
        return 1
    else:
        return fibonacci_rec(q-1) + fibonacci_rec(q-2)
m=int(input("Enter the number of terms:"))
for Num in range(1,m+1):
           print(fibonacci_rec(Num), end=' ')
    


# In[13]:


# To print all prime number betweenN and M.
num=int(input("Enter a number:"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            print(i,"times",num// i,"is", num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is a not prime number")
    


# In[15]:


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number"))
large= a
if(b> large):
    large=b
if(c>large):
    large=c
print("largest of {},{} and {} is : {}". format(a,b,c,large))


# In[16]:


#To find the GCD of two numbers input by user
def gcd(a,b):
    while(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    return a
a=int(input("Enter first number:"))
b=int(input("Enter second number"))
g=gcd(a,b)
print("GCD of {} and {} is:  {}". format(a,b,g))


# In[ ]:




