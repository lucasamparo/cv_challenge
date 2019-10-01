#!/usr/bin/env python
# coding: utf-8

# In[1]:


looping=True
while looping==True:
    n=input("Choose a number between 1 and 10000: ")
    try:
        while int(n)<1 or int(n)>10000:
            n=input("Choose a number between 1 and 10000: ")
        looping=False
    except:
        looping=True
        print("You should digit an integer value. Please, run the cell again!")
n=int(n)


# ### INPUTS

# After choosing the number of test cases, the coordenates of the stars were chosen. The threatment of exceptions was done based on the challenge conditions.  

# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[5]:


df_inputs=pd.DataFrame()
df_inputs['Test_Case']=[]
df_inputs['Points']=[]
df_inputs['X_coordenates']=[]
df_inputs['Y_coordenates']=[]
for i in range(n):
    loop_total=True
    while loop_total==True:
        print("Please, choose the coordenates of the first star at the first moment:")
        looping=True
        while looping==True:
            try:
                x1_1 = float(input("Choose a number between -1000.0 and +1000.0 to be the X-coordenate of the first star at the first moment: "))
                while x1_1< -1000.00 or x1_1 >1000.00:
                    x1_1 = float(input("Choose a number between -1000.0 and +1000.0 to be the X-coordenate of the first star at the first moment: "))
                string_number = ("{0:.2f}".format(x1_1))
                x1_1 = float(string_number)
                looping = False
            except:
                looping=True
                print("You should digit a float value with 2 decimal places. Please, run the cell again!")
    
        looping=True
        while looping==True:
            try:
                y1_1 = float(input("Choose a number between -1000.0 and +1000.0 to be the Y-coordenate of the first star at the first moment: "))
                while y1_1< -1000.00 or y1_1> 1000.00:
                    y1_1 = float(input("Choose a number between -1000.0 and +1000.0 to be the Y-coordenate of the first star at the first moment: "))
                string_number = ("{0:.2f}".format(y1_1))
                y1_1 = float(string_number)
                looping = False
            except:
                looping=True
                print("You should digit a float value with 2 decimal places. Please, run the cell again!")
    
        print("Please, choose the coordenates of the second star at the first moment:")
        looping=True
        while looping==True:
            try:
                x2_1 = float(input("Choose a number between -1000.0 and +1000.0 to be the X-coordenate of the second star at the first moment: "))
                while x2_1< -1000.00 or x2_1> 1000.00:
                    x2_1 = float(input("Choose a number between -1000.0 and +1000.0 to be the X-coordenate of the second star at the first moment: "))
                string_number = ("{0:.2f}".format(x2_1))
                x2_1 = float(string_number)
                looping = False
            except:
                looping=True
                print("You should digit a float value with 2 decimal places. Please, run the cell again!")
    
        looping=True
        while looping==True:
            try:
                y2_1 = float(input("Choose a number between -1000.0 and +1000.0 to be the Y-coordenate of the second star at the first moment: "))
                while y2_1< -1000.00 or y2_1> 1000.00:
                    y2_1 = float(input("Choose a number between -1000.0 and +1000.0 to be the Y-coordenate of the second star at the first moment: "))
                string_number = ("{0:.2f}".format(y2_1))
                y2_1 = float(string_number)
                looping = False
            except:
                looping=True
                print("You should digit a float value with 2 decimal places. Please, run the cell again!")
    
        print("Please, choose the coordenates of the first star at the second moment:")
        looping=True
        while looping==True:
            try:
                x1_2 = float(input("Choose a number between -1000.0 and +1000.0 to be the X-coordenate of the first star at the second moment: "))
                while x1_2< -1000.00 or x1_2> 1000.00:
                    x1_2 = float(input("Choose a number between -1000.0 and +1000.0 to be the X-coordenate of the first star at the second moment: "))
                string_number = ("{0:.2f}".format(x1_2))
                x1_2 = float(string_number)
                looping = False
            except:
                looping=True
                print("You should digit a float value with 2 decimal places. Please, run the cell again!")
    
        looping=True
        while looping==True:
            try:
                y1_2 = float(input("Choose a number between -1000.0 and +1000.0 to be the Y-coordenate of the first star at the second moment: "))
                while y1_2< -1000.00 or y1_2> 1000.00:
                    y1_2 = float(input("Choose a number between -1000.0 and +1000.0 to be the Y-coordenate of the first star at the second moment: "))
                string_number = ("{0:.2f}".format(y1_2))
                y1_2 = float(string_number)
                looping = False
            except:
                looping=True
                print("You should digit a float value with 2 decimal places. Please, run the cell again!")
    
        print("Please, choose the coordenates of the second star at the second moment:")
        looping=True
        while looping==True:
            try:
                x2_2 = float(input("Choose a number between -1000.0 and +1000.0 to be the X-coordenate of the second star at the second moment: "))
                while x2_2< -1000.00 or x2_2> 1000.00:
                    x2_2 = float(input("Choose a number between -1000.0 and +1000.0 to be the X-coordenate of the second star at the second moment: "))
                string_number = ("{0:.2f}".format(x2_2))
                x2_2 = float(string_number)
                looping = False
            except:
                looping=True
                print("You should digit a float value with 2 decimal places. Please, run the cell again!")
    
        looping=True
        while looping==True:
            try:
                y2_2 = float(input("Choose a number between -1000.0 and +1000.0 to be the Y-coordenate of the second star at the second moment: "))
                while y2_2< -1000.00 or y2_2> 1000.00:
                    y2_2 = float(input("Choose a number between -1000.0 and +1000.0 to be the Y-coordenate of the second star at the second moment: "))
                string_number = ("{0:.2f}".format(y2_2))
                y2_2 = float(string_number)
                looping = False
            except:
                looping=True
                print("You should digit a float value with 2 decimal places. Please, run the cell again!")
            
        print("Coordenates: ")
        print(" ")
        print("First star at the first moment: ",[x1_1,y1_1])
        print("Second star at the first moment: ",[x2_1,y2_1])
        print("First star at the second moment: ",[x1_2,y1_2])
        print("Second star at the second moment: ",[x2_2,y2_2])
       
        if [x1_1,y1_1]==[x1_2,y1_2] or [x2_1,y2_1]==[x2_2,y2_2] or [x1_1,y1_1]==[x2_1,y2_1] or [x1_2,y1_2]==[x2_2,y2_2]:
            print("The coordenates of the stars should be different and these stars should move.")
            loop_total=True
        else:
            loop_total=False
    
    df_i=pd.DataFrame()
    df_i['Points']=["First star at the first moment","Second star at the first moment","First star at the second moment","Second star at the second moment"]
    df_i['X_coordenates']=[x1_1,x2_1,x1_2,x2_2]
    df_i['Y_coordenates']=[y1_1,y2_1,y1_2,y2_2]     
    df_i['Test_Case']=str(i+1) 
    df_inputs=df_inputs.append(df_i)


# For not needing write the inputs again all coordenates, the inputs were load in "csv".

# In[8]:


df_inputs=df_inputs.reset_index()


# In[9]:


df_inputs.to_csv('df_inputs.csv')


# ### Outputs

# In[4]:


df_inputs=pd.read_csv('df_inputs.csv').iloc[:,2:]


# In[11]:


df_inputs


# For this part, we had to discover the center (C) where "dist C-First star at the first moment"=="dist C-First star at the second moment" and "dist C-Second star at the first moment"=="dist C-Second star at the second moment".
# 
# For doing this, a line was considered linking the points related to each star. In the middle of this line segment, 
# a transversal line was considered; in every point of this new line, the distances between the two points are the same.
# With this consideration, the center (C) of both arches was found by the interception of the perpendicular lines.

# The output solution considers all possibilities of having one Center for two circumferences. If both transversal lines 
# were vertical or horizontal, the solution would be impossible.  

# In[12]:


for i in range(n):
    df_t=df_inputs[df_inputs['Test_Case']==(i+1)]
    try:
        try:
            
            # Calculate transversal line of the first star
            a1=(df_t.iloc[0,3]-df_t.iloc[2,3])/(df_t.iloc[0,2]-df_t.iloc[2,2])
            if a1==0:
                #if dy/dx==0, the perpendicular line is vertical and if dy/dx is infinite, this line is horizontal. 
                x=(df_t.iloc[0,2]+df_t.iloc[2,2])/2
                # Transversal line of the second star
                try:
                    a11=(df_t.iloc[1,3]-df_t.iloc[3,3])/(df_t.iloc[1,2]-df_t.iloc[3,2])
                    a2=-1/a11
                    x_middle=(df_t.iloc[1,2]+df_t.iloc[3,2])/2
                    y_middle=(df_t.iloc[1,3]+df_t.iloc[3,3])/2
                    b2=y_middle-a2*x_middle
                    y=a2*x+b2
                except:
                    # There is an intersection between horizontal and vertical lines.
                    y=(df_t.iloc[1,3]+df_t.iloc[3,3])/2
            # Therefore, the Center of the two circumferences or the intersection of the two perpendicular lines is:
            #Output:
                print("Caso #",str(i+1),": ",x," ",y)
            
            else:
            
                # This situation considers an inclined perpendicular line.
                # The product of the angular coefficients of perpendicular lines is equal to -1. So:
                a=-1/a1
                # The middle of the line segment belongs to the new line. 
                x_middle=(df_t.iloc[0,2]+df_t.iloc[2,2])/2
                y_middle=(df_t.iloc[0,3]+df_t.iloc[2,3])/2
                b=y_middle-a*x_middle
                # Transversal line of the second star
                try:
                    #In this point, were written the three possibilities of transversal line related to the second star. 
                    #Here all the possibilities are viable.
                    a11=(df_t.iloc[1,3]-df_t.iloc[3,3])/(df_t.iloc[1,2]-df_t.iloc[3,2])
                    #if dy/dx==0, the perpendicular line is vertical and if dy/dx is infinite, this line is horizontal. 
                    if a11==0:
                        x=(df_t.iloc[1,2]+df_t.iloc[3,2])/2
                        y=a*x+b
                    else:
                        a2=-1/a11
                        x_middle=(df_t.iloc[1,2]+df_t.iloc[3,2])/2
                        y_middle=(df_t.iloc[1,3]+df_t.iloc[3,3])/2
                        b2=y_middle-a2*x_middle
                        # Therefore, the Center of the two circumferences or the intersection of the two perpendicular lines is:
                        x=(b2-b)/(a-a2)
                        y=a*x+b
                except:
                    y=(df_t.iloc[1,3]+df_t.iloc[3,3])/2
                    x=(y-b)/a
                #Output:
                print("Caso #",str(i+1),": ",x," ",y)
            
        except:
            
            y=(df_t.iloc[0,3]+df_t.iloc[2,3])/2
            a11=(df_t.iloc[1,3]-df_t.iloc[3,3])/(df_t.iloc[1,2]-df_t.iloc[3,2])
            if a11==0:
                x=(df_t.iloc[1,2]+df_t.iloc[3,2])/2
            else:
                a2=-1/a11
                x_middle=(df_t.iloc[1,2]+df_t.iloc[3,2])/2
                y_middle=(df_t.iloc[1,3]+df_t.iloc[3,3])/2
                b2=y_middle-a2*x_middle
                x=(y-b2)/a2
            #Output:
            print("Caso #",str(i+1),": ",x," ",y)
            
    except:
        print("Caso #",str(i+1),": ","A solução não é possível!")
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




