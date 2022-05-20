#!/usr/bin/env python
# coding: utf-8

# In[5]:


string = input("Enter the string :")

new_str = string[ : : -1]

if new_str == string:
    print("{} is palindrome".format(string))
else:
    print("{} is not a Palindrome".format(string))


# In[ ]:




