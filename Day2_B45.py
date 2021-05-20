#!/usr/bin/env python
# coding: utf-8

# In[ ]:


understanding the variables in python


# In[ ]:


x = 5
y = 3


# In[22]:


c= x + y
print(c)


# In[ ]:


Rules for declaring the variables in python:


# In[ ]:


1.No name spaces while declaring the variable name.


# In[16]:


first name = 'Hrishika'
print(first name)


# In[17]:


firstname = 'Hrishika'
print(firstname)


# In[18]:


first_name = 'Hrishika'
print(first_name)


# In[ ]:


Rule no 2: A variable should not start with a number


# 

# In[19]:


1name = 'raj'
print(1name)


# In[20]:


name1='raj'
print(name1)


# In[ ]:


Rule no 3: A variable should not have any special character


# In[21]:


name$='raj'
print(name$)


# In[ ]:


introduction to datatypes in python
1.string------------>str

2.Numbers----------->integers(int) and floats(decimals)

3.list--------------->list

4.tuple-------------->tuple

5.Dictionary---------->dict


# In[ ]:


classification of data types:
    
    datatypes are classified in to 2 diff categories :
        1.mutable datatype------> which we can edit or alter
        
        2.immutable datatype------>which we cannot edit or alter


# In[ ]:


introduction to string datatype

overview: A string is nothing but a series of characters declared in quotes
    
classification: it is classified as immutable datatype    
    
    
    how to declare the string datatype.....?
    1.single quote
    2.double quote
    3.triple quote


# In[2]:


name = 'krishna'  #single quotes

print(name)


# In[3]:


name1 = "hrishika"  #double quotes

print(name1)


# In[5]:


name2="""raj"""  #triple quotes
print(name2)


# In[ ]:


introduction to string methods:
    
    methods:these are nothing but builtin prograns and are available to use.


# In[ ]:


type------->it is use to validate and know the datatypes of the variables created..!


# In[6]:


type(name)


# In[7]:


type(name1)


# In[8]:


type(name2)


# In[9]:


fullname = 'santosh kumar'
print(fullname)


# In[ ]:


#req:i want to write name in capitals


# In[10]:


print(fullname.upper())


# In[ ]:


#req:i want to write name in correct way


# In[11]:


print(fullname.title())


# In[ ]:


#req:i want to write name in small letters


# In[12]:


print(fullname.lower())


# In[ ]:




