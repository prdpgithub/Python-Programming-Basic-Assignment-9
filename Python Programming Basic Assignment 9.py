#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.	Write a Python program to check if the given number is a Disarium Number?


num = int(input())
rem = s = 0;    
len = len(str(num))
     
n = num;    
  
while(num > 0):    
    rem = num%10;    
    s += int(rem**len);    
    num = num//10;    
    len -= 1;    
    
if(s == n):    
    print( "disarium number");    
else:    
    print(" not a disarium number");    


# In[2]:


# 2.	Write a Python program to print all disarium numbers between 1 to 100?
 
def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
#sumOfDigits() will calculates the sum of digits powered with their respective position    
def sumOfDigits(num):    
    rem = sum = 0;    
    len = calculateLength(num);    
        
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     
#Displays all disarium numbers between 1 and 100    
print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):    
    result = sumOfDigits(i);    
        
    if(result == i):    
        print(i),    


# In[6]:


# 3.	Write a Python program to check if the given number is Happy Number?


num= int(input())
temp=num
while sum!=1 and sum!=4:
    sum=0
    while temp!=0:
        rem = int(temp%10)
        sum= sum+rem*rem
        temp = temp/10 
         
    temp = sum; 
      
if (sum == 1):  
    print(num,"is a happy number")
else: 
    print(num,"is a Unhappy number")


# In[10]:


#  4.	Write a Python program to print all happy numbers between 1 and 100?


def isHappyNumber(num):  
    rem = sum = 0;  
 
    while(num > 0):  
        rem = num%10;  
        sum = sum + (rem*rem);  
        num = num//10;  
    return sum;  
          
print("List of happy numbers between 1 and 100: ");  
for i in range(1, 101):  
    result = i;  
    while(result != 1 and result != 4):  
        result = isHappyNumber(result);  
      
    if(result == 1):  
        print(i),  
        print(" "),  


# In[11]:


# 5.	Write a Python program to determine whether the given number is a Harshad Number?


num = 156;    
rem = sum = 0;    
     
#Make a copy of num and store it in variable n    
n = num;    
     
#Calculates sum of digits    
while(num > 0):    
    rem = num%10;    
    sum = sum + rem;    
    num = num//10;    
     
#Checks whether the number is divisible by the sum of digits    
if(n%sum == 0):    
    print(str(n) + " is a harshad number");    
else:    
    print(str(n) + " is not a harshad number");    


# In[13]:


# 6.	Write a Python program to print all pronic numbers between 1 and 100?


def isPronicNumber(num):    
    flag = False;    
        
    for j in range(1, num+1):    
        #Checks for pronic number by multiplying consecutive numbers    
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;    
     
#Displays pronic numbers between 1 and 100    
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i),    
        print(" "),    


# In[ ]:




