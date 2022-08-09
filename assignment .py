#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# 

# #### Import NumPy as np

# In[2]:


import numpy as np


# #### Create an array of 10 zeros 

# In[3]:


z=np.zeros(10)
z


# #### Create an array of 10 ones

# In[4]:


z=np.ones(10)
z


# #### Create an array of 10 fives

# In[5]:


z=np.array([5,5,5,5,5,5,5,5,5,5])
z


# #### Create an array of the integers from 10 to 50

# In[15]:


z=np.linspace(10,50,30)
z


# #### Create an array of all the even integers from 10 to 50

# In[21]:


z=np.linspace(10,50,21)
z


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[87]:


z=np.arange(0,9).reshape(3,3)
z


# #### Create a 3x3 identity matrix

# In[36]:


z=np.identity(3)
z


# #### Use NumPy to generate a random number between 0 and 1

# In[43]:


z=np.random.rand(10)
z


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[46]:


z=np.random.normal(0,1,25)
z


# #### Create the following matrix:

# In[61]:


z=np.linspace(0,1,101)

z


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[65]:


z=np.linspace(0,1,20)
z


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[66]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[39]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[40]:





# In[77]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
z1=np.arange(12,16)
z2=np.arange(17,21)
z3=np.arange(22,26)
z=np.vstack((z1,z2))
zz=np.vstack((z,z3))
zz


# In[41]:





# In[78]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
20


# In[42]:





# In[80]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
z=np.array([[2],[7],[12]])
z


# In[46]:





# In[81]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
z=np.arange(21,26)
z


# In[49]:





# In[88]:


z=np.arange(16,26).reshape(2,5)
z


# ### Now do the following

# #### Get the sum of all the values in mat

# In[50]:





# In[91]:


z=np.array([[2,3,4],[1,2,6],[8,3,9]])
z.sum()


# #### Get the standard deviation of the values in mat

# In[92]:


z.std()


# #### Get the sum of all the columns in mat

# In[53]:





# # Great Job!
