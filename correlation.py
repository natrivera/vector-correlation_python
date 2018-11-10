import numpy as np

def corr(arr1 , arr2):
    
    #define two arrays with ratings from signature
    Ri = arr1
    Rj = arr2

    #extract all the non zero terms from the arrays
    Ri_non_zero = [i for i in Ri if i !=  0 ]
    Rj_non_zero = [ i for i in Rj if i != 0 ]

    #get the mean of the non zero arrays
    Ri_mean_non_zero = sum(Ri_non_zero) / len(Ri_non_zero)
    Rj_mean_non_zero = sum(Rj_non_zero) / len(Rj_non_zero)

    #create arrays where both users have ratings
    Ri_sim = np.array([ i if j != 0 else 0 for i,j in zip(Ri,Rj) ])
    Rj_sim = np.array([ j if i != 0 else 0 for i,j in zip(Ri,Rj) ])

    #extract all the non zero terms from the arrays
    Ri_sim = Ri_sim[Ri_sim != 0]
    Rj_sim = Rj_sim[Rj_sim != 0]

    #calculate the variance of each element
    Ri_sim_var = Ri_sim - Ri_mean_non_zero
    Rj_sim_var = Rj_sim - Rj_mean_non_zero

    #square the variance of each element
    Ri_sim_sq_var = Ri_sim_var **2
    Rj_sim_sq_var = Rj_sim_var **2

    #calculat the sum product of the squared variances
    sum_prod_var = sum(Ri_sim_var * Rj_sim_var)

    #calculate the sum squared variance for each user
    Ri_sim_sum_sq_var = sum(Ri_sim_sq_var)
    Rj_sim_sum_sq_var = sum(Rj_sim_sq_var)

    #calculate the sqrt of the sum squared variance for each user
    Ri_sim_sqrt_sum_sq_var = Ri_sim_sum_sq_var**(1/2)
    Rj_sim_sqrt_sum_sq_var = Rj_sim_sum_sq_var**(1/2)

    #calculate the product of sqrt of the sum squared variance for both users
    prod_sum_sqrt_sq_var = Ri_sim_sqrt_sum_sq_var * Rj_sim_sqrt_sum_sq_var

    #calculate the corrrelation 
    corr = sum_prod_var / prod_sum_sqrt_sq_var

    #output the correlation
    print("Correlation: " , corr)

Ri = [ 4, 1, 0, 0, 3, 3, 4, 5, 0]
Rj = [ 3, 0, 1, 4, 0, 4, 5, 0, 0]
corr(Ri , Rj)