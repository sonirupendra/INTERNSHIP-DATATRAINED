#!/usr/bin/env python
# coding: utf-8

# In[34]:


num = int(input('Enter Number :'))

for i in range(2,num):
    if num%i ==0:
        print('{} is composite number'.format(num))
        break
else:
    print('{} is Prime'.format(num))


# In[ ]:





# In[ ]:




