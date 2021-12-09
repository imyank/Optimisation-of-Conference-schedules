import random

### Taking inputs
papers_per_session = int(input())
parallel_sessions=int(input())
time=int(input())
C=float(input())
n = papers_per_session*parallel_sessions*time

## shuffling_temporary_function

list_1=[]
def schedulement():
  a,b,c=0,0,0
  list_1= list(range(0, n))
  #random.shuffle(list_1)
  temp_sch=[]
  ####### finding temporary schedulement
  i= len(list_1)-1
    ####### selecting range of
  #### parralel sessions
  while a<parallel_sessions:
    temp_2= []
    b=0
    ####### selecting range of
    ###### time
    while b<time:
      temp_1= []
      c=0
       ####### selecting range of
      ######### papers per session
      while c<papers_per_session:
        temp_1.append(list_1[i])
        i=i-1
        c=c+1
      ############ appending 1st arrays
      temp_2.append(temp_1)
      b=b+1
    ############ appending 2nd arrays
    temp_sch.append(temp_2)  
    ####### increment and return
    a=a+1
  return(temp_sch)



## calculate difference and similarity matrix

diff_matrix=[]
sim_matrix=[]

for i in range(n):
  dist = input().split()
  diff_matrix.append([float(i) for i in dist])
  sim_matrix.append([1-float(i) for i in dist])


## calculate final goodness score 

def overall_goodness_score(type_of_sch):
  g_value,op1,op2,pr,po1 = 0,0,0,0,0
  itr=[]
  itr_1=[]
  itr_2=[]
  #### parralel sessions
  while op1<parallel_sessions:
    op2=0
    #### time
    while op2<time:
      i1=0
      ########## papers per session
      while i1<papers_per_session:
        ####### selecting range of
        ##### papers per session
        for z in range((i1+1),(papers_per_session)):
          itr=type_of_sch[op1][op2]
          g_value = g_value + sim_matrix[itr[i1]][itr[z]]
        i1=i1+1
      op2=op2+1
    op1=op1+1
  ############# time
  while pr<time:
    ######### selecting range of
    ####### parallel_sessions
    while po1<parallel_sessions: 
      ###########  selecting range of
      ######### parallel_sessions
      for po2 in range((po1+1),parallel_sessions):
        i2=0
        ######### selecting range of
        ########### papers per session
        while i2<papers_per_session:
          for z in range(papers_per_session):
            itr_1=type_of_sch[po1][pr]
            itr_2=type_of_sch[po2][pr]
            g_value = g_value + C*diff_matrix[itr_1[i2]][itr_2[z]]
          i2=i2+1
      po1=po1+1
    pr=pr+1
  return(g_value) 


### final algo
maxi=-5
temp_var = 1
overall_score= 0.0
temp_score= 0.0
steps_limit=1
local_sch=[]
global_sch=[]
####### First choice hill climbing
#######  taking some iterations
for i in range(1255):
 ####### checking temporary var
 if(temp_var!=0):
   ######## taking necessary variables
  temp_var ,order_sch = 0,schedulement()
  local_sch = order_sch
  var1,var3,var5=0,0,0
   ###### storing variables temporary
  temp_local_score = overall_goodness_score(order_sch)
  ####### necessary variables
    ######### selecting range of
        ########### papers per session
  while var1<papers_per_session:
    ######### selecting range of
        ########### papers per session
      for var2 in range((var1+1),papers_per_session): 
            ######### selecting range of
####### parallel_sessions
        while var3<parallel_sessions:     
              ######### selecting range of
####### parallel_sessions                    
          for var4 in range((var3+1),parallel_sessions):
              ######### selecting range of
####### time
            while var5<time:
                ######### selecting range of
####### time
              for var6 in range((var5+1),time):
                ########### using probability approach to select he next successor
                qa=random.random()
                interchange=order_sch
                if qa>0.5:
                  interchange[var3][var5][var1],interchange[var4][var6][var1]=interchange[var4][var6][var1],interchange[var3][var5][var1]
                else:
                  interchange[var3][var5],interchange[var4][var6]=interchange[var4][var6],interchange[var3][var5]
                ###### storing max
                temp_local_score=max(temp_local_score,overall_goodness_score(interchange))
                ####### replacement
                local_sch = interchange
                temp_var= 1
              var5=var5+1
          var3=var3+1
      var1=var1+1
########## selecting max value
  overall_score=max(overall_score,overall_goodness_score(local_sch))
  global_sch= local_sch


######### Increment each value
x,y=0,0
while x<parallel_sessions:
  y=0
  while y<time:
    global_sch[x][y] = [q + 1 for q in global_sch[x][y]]
    y+=1
  x+=1
            
        
## printing result
for p in range(0,parallel_sessions):
  for q in range(0,time):
        if q == time-1:
             print(*global_sch[p][q], end=" ")
        else:
            print(*global_sch[p][q], end=" | ") 
  print()