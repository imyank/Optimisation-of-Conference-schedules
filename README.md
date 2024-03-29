# Optimisation-of-Conference-schedules

Background of task:

The goal is to take a complex new problem and formulate and solve it as a search. Formulation as search is an integral skill of AI that will come in handy whenever you are faced with a new problem. Heuristic search will allow you to find optimal solutions. Local search may not find the optimal solution, but is usually able to find good solutions for really large problems

Please read problem statement before going ahead.

Inputs Taken in following formats:

1. papers_per_session
2. parallel_sessions
3. time
4. C
5. n=papers_per_session*parallel_sessions*time

--The constant C is tradeoff between the importance of semantic coherence of one session versus reducing conflict across parallel sessions

Algorithm: First choice Hill climbing


Steps used:


1. Created a temporary shuffle function which will iterate through the papers_per_session, parallel_sessions and time. 
   This function will produce a sequence which will be utilised to calculate goodness score.
2. Difference and Similarity matrix(1- Difference matrix) are calculated.
3. Overall_goodness_score function calculates the total goodness value from the formula given and by traversing the 
   three nested loops of papers_per_session, parallel_sessions and time.
4. In Modified hill climbing, iterations taken are around 1250. A temp_var variable is taken which acts as a flag. 
   The schedule from the shuffle function is taken and a temporary goodness value is calculated.
5.  While iterating through three nested loops, random successors are generated by swapping the papers_per_session, 
    parallel_sessions and time, which is governed by random function(probability>0.5 & probability<=0.5)
6.  After swapping, the max goodness score is calculated 
7.  The schedule at which max score comes is stored in the variable global_sch
8.  Incremented one value in schedule for the desired output.
9.  Finally printing the result

for implementation refer to code.
