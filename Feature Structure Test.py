#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[3]:


f1 = nltk.FeatStruct("""[NAME='lee', ADD=(1)[NUM=74, STREET='rue pascal'], AGE=33, SPOSE=[NAME='kim', ADD->(1)]]""")


# In[4]:


print(f1)


# In[5]:


f1 = nltk.FeatStruct("""[NAME='lee', ADD1=[NUM=74, STR='rue pascal'], AGE=33, SPOUSE=[NAME='kim', ADD2=[]]]""")


# In[9]:


f2 = nltk.FeatStruct("""[ADD1=?x, SPOUSE=[ADD2=?x]]""")


# In[10]:


print(f2.unify(f1))


# In[11]:


f1 = nltk.FeatStruct("""[NAME='lee', AGE=33, ADD=(1)[NUM=2, STR='green ave'], CHILD=[NAME='kim', ADD->(1)], SPOUSE=[NAME='sara', ADD->(1)]]""")


# In[12]:


print(f1)


# In[14]:


f1 = nltk.FeatStruct("""[NAME='lee', AGE=33, ADD1=[NUM=2, STR='green ave'], CHILD=[NAME='kim', ADD2=[]], SPOUSE=[NAME='sara', ADD3=[]]]""")


# In[15]:


f2 = nltk.FeatStruct("[ADD1=?x, CHILD=[ADD2=?x], SPOUSE=[ADD3=?x]]")


# In[16]:


print(f2.unify(f1))


# In[ ]:




