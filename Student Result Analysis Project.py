#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[7]:


df = pd.read_csv("Students_Scores_csv")


# In[8]:


print (df.head())


# In[9]:


df.describe


# In[10]:


df.info()


# In[11]:


df.isnull().sum()


# In[12]:


df = df.drop("Unnamed: 0", axis=1)
print(df.head())


# In[13]:


#df.[WklyStudyHours] = df.[WklyStudyHours].str.replace("5 Oct","%-10")
#df.head()


# # Gender Distribution

# In[33]:


plt.figure(figsize = (5,5))
ax = sns.countplot(data = df, x = 'Gender')
plt.title("Gender's Distribution")
ax.bar_label(ax.containers[0])
plt.show()


# In[15]:


#from above chart we have analysed that the number of females is more than that of male


# In[16]:


gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)


# In[30]:


plt.figure(figsize = (5,5))
sns.heatmap(gb, annot = True)
plt.title("Relationship between Parent's Education and Student's Score")
plt.show()


# In[ ]:


#from the above chart we have concluded that the education of the parents have a good impact on the scores


# In[27]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)


# In[31]:


plt.figure(figsize = (5,5))
sns.heatmap(gb1, annot = True)
plt.title("Relationship between Parent's Marital Status and Student's Score")
plt.show()


# In[ ]:


#from the above chart we have concluded that there is no/negligible impact on scores due to marital status od parent


# In[35]:


sns.boxplot(data = df, x = "MathScore")
plt.show()


# In[36]:


sns.boxplot(data = df, x = "ReadingScore")
plt.show()


# In[37]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Groups

# In[42]:


groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "group E")].count()


l = ["group A","group B","group C","group D","group E"]
mlist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
print(mlist)
plt.pie(mlist, labels = l, autopct = "%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()


# In[43]:


ax = sns.countplot(data = df, x = 'EthnicGroup')
ax.bar_label(ax.containers[0])


# In[49]:


gb2 = df.groupby("PracticeSport").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb2)


# In[51]:


plt.figure(figsize = (5,5))
sns.heatmap(gb2, annot = True)
plt.title("Relationship between Practice Sports and Student's Score")
plt.show()


# In[53]:


gb3 = df.groupby("TransportMeans").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb3)


# In[55]:


plt.figure(figsize=(5,5))
sns.heatmap(gb3, annot = True)
plt.title("Relationship Between Transport Means and Student's Score")
plt.show()


# In[ ]:




