#!/usr/bin/env python
# coding: utf-8

# In[8]:


num = int(input("Enter the number :"))
fact = 1

if num<0:
    print('Sorry for this number , factorial of this number is not find')
elif num ==0:
    print("Factorial of zero is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print("Factorial of",num,'Is',fact )
            


# In[ ]:




