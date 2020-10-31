import numpy as np
import scipy.stats
  
def criticalRange( mu, sigma, n ) : 
  # Your code to calculate the critical region should go here
  
  return lower
  
def hypothesisTest( data, n, mu, sigma ) : 
  l = criticalRange( mu, sigma, n )
  # You need to use the l value that is returned from the critical range
  # function above within an if statement.  This if statement should decide whether 
  # there is sufficient evidence to reject the null hypothesis.  The code should
  # then return either the statement about the null hypothesis being rejected or
  # the statement about there being insufficient evidence to reject the null 
  # hypothesis form the flowchart.
  

# You need to set these three variables using the information in the question  
mu0 = 
sigma = 
observation =
nmeasurements = 
print( hypothesisTest( observation, mu0, sigma ) )
