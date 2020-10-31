import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_criticalRange(self) :
        l = scipy.stats.norm.ppf(0.05,loc=97,scale=4/np.sqrt(100) )
        lll= criticalRange( mu0, sigma, 100 )
        self.assertTrue( np.abs(l-lll)<1e-4, "you have calculated the bound for the critical range incorrectly")
        
    def test_hypothesisTest(self) : 
        hhh = hypothesisTest( observation, nmeasurements, mu0, sigma ) 
        self.assertTrue( hhh=="the null hypothesis is rejected in favour of the alternative", "your hypothesisTest function returns the wrong string" )
        self.assertTrue( inspect.getsource(hypothesisTest).find("if")>0, "your hypothesisTest function does not contain an if statement )
        self.assertTrue( inspect.getsource(hypothesisTest).find("there is insufficient evidence to reject the null hypothesis")>0, "The hypothesis test function does not contain the string "there is insufficient evidence to reject the null hypothesis."  This string should be present and output when the sample mean falls outside the critical region." ) 

    def test_variables(self) : 
        self.assertTrue( mu0==97, "the variale mu0 has been set incorrectly" )
        self.assertTrue( sigma==4, "the variable sigma has been set incorrectly" )
        self.assertTrue( observation==85 , "the variable observations has been set incorrectly" )
        self.assertTrue( nmeasurements==100, "the variable nmesurements has been set incorrectly" )
