import numpy as np
import math
from vecproj import VectorCalculations
inst=VectorCalculations()

def length_test():
    """Tests length_check function testcases"""
    #Lets start by testing the length function with various cases, any acceptable vector, vectors with negatives and positives empty vectors, vectors with decimals etc
    assert inst.length_check([1,5,2],[4,5,7])
    assert inst.length_check([-1,5,-2], [0,0,0]) 
    assert inst.length_check([-1,5,-2], [-1,-7,-10]) 
    assert inst.length_check([0,0,0],[0,0,0])
    assert inst.length_check([],[])
    assert inst.length_check([0.34,0.5],[4,3.5])
    assert not inst.length_check([1,4,6], "hmm") #Non vector but they have equal lengths, important border case
    assert not inst.length_check([1,4,6], True) #Non vector
    assert not inst.length_check([1,4,6], [1,4]) #Different lengths
    assert not inst.length_check("hmm", "br")

def vec_check_test():
    """Tests vec_check function with relevant testcases"""
    #Let us now test the vec check function, especially important cases are empty vectors, vectors with only positives, only negatives and finally vectors with negative and positive numbers, vectors with non numbers and non vectors
    assert inst.vec_check([1,3,5])
    assert inst.vec_check([-1,-4,-7,-5])
    assert inst.vec_check([])
    assert inst.vec_check([-1,3,5,0])
    assert inst.vec_check([0,0,0,0])
    assert not inst.vec_check([1,4,5,6, "bruh", True])
    assert not inst.vec_check(None)

def dot_prod_test():
    """Tests the dotprod function with relevant testcases"""
    #Let us test the dot prod function, well just use some standard cases followed by tests with numpy such as only positives, negatives and positive floats, zerovectors, followed by errors
    assert inst.dot_prod([1,2,3],[4,5,6])==1*4+2*5+3*6 
    assert inst.dot_prod([1,2,3],[3,2,3])==1*3+2*2+3*3
    assert inst.dot_prod([1.5,2.5,3.7], [4.5,5.5,6.5])==1.5*4.5+2.5*5.5+3.7*6.5
    assert inst.dot_prod([0,0,0],[0,0,0])==0
    assert inst.dot_prod([1,3,5],[3,5,6])==np.dot([1,3,5], [3,5,6])
    assert inst.dot_prod([-1,-3,-5], [-3,-5,-6])==np.dot([-1,-3,-5],[-3,-5,-6])
    assert inst.dot_prod([5.5,3,0,-7.5], [-3,5,-6,0])==np.dot([5.5,3,0,-7.5],[-3,5,-6,0])
    assert inst.dot_prod([],[])==0
    assert inst.dot_prod([1,3,5], [0,0,0])==np.dot([1,3,5], [0,0,0])
    try:
        assert inst.dot_prod([0,0,0],[0,0])==0
    except ValueError as e:
        assert str(e)=="Please enter two vectors with the same length"
    try:
        assert inst.dot_prod([0,0,None],[0,0,0])==0
    except ValueError as e:
        assert str(e)=="The first vector has an incorrect structure, please only enter vectors with integers and floats"
    try:
        assert inst.dot_prod([0,0,0],[0,0,True])==0
    except ValueError as e:
        assert str(e)=="The second vector has an incorrect structure, please only enter vectors with integers and floats"

def cross_prod_test():
    """Tests the crossprod function with relevant testcases"""
    #Let us test the cross product function,  well just use some standard cases followed by more extensive testing with numpy such as only positives, only negatives, negatives and postives (and floats), only floats, zerovectors, followed by errors, 
    #note the need to convert to a normal array
    assert inst.cross_prod([1,2,3], [4,5,6]) == [2*6-3*5,3*4-1*6,1*5-2*4]
    assert inst.cross_prod([1,0,-1], [-1,1,0]) == [0-(-1)*1,(-1)*(-1)-1*0,1*1-0*(-1)]
    assert inst.cross_prod([1,2,3],[1,2,3])==[0,0,0] #paralell vectros
    assert inst.cross_prod([1,3,5], [3,5,6])==list(np.cross([1,3,5], [3,5,6]))
    assert inst.cross_prod([-1,-3,-5], [-3,-5,-6])==list(np.cross([-1,-3,-5], [-3,-5,-6]))
    assert inst.cross_prod([5.5,3,-7.5], [-3,5,-6])==list(np.cross([5.5,3,-7.5], [-3,5,-6]))
    assert inst.cross_prod([5.5,7.5,5.6], [3.6,5.5,9.9])==list(np.cross([5.5,7.5,5.6], [3.6,5.5,9.9]))
    assert inst.cross_prod([0,0,0],[0,0,0])==[0,0,0]
    assert inst.cross_prod([1,3,5], [0,0,0])==list(np.cross([1,3,5], [0,0,0]))
    try:
        assert inst.cross_prod(["hej"],[0,0,0])
    except ValueError as e:
        assert str(e)=="Please enter two vectors with integers and floats"
    try:
        assert inst.cross_prod([0,0],[0,0,0])
    except ValueError as e:
        assert str(e)=="The first vektor has an incorrect length, please enter a vector with 3 numbers"
    try:
        assert inst.cross_prod([0,0,0],[0,0])
    except ValueError as e:
        assert str(e)=="The second vektor has an incorrect length, please enter a vector with 3 numbers"

def test_vec_add():
    """Tests the vecadd function with relevant testcases"""
    #Let us test the add function, well just use well just use some standard cases followed by more extensive testing with numpy such as only positives, only negatives, negatives and postives (and floats), only floats, zerovectors, followed by errors
    assert inst.vec_add([1, 2, 3], [4, 5, 6])==[1+4,2+5,3+6]
    assert inst.vec_add([1, 2, 3], [-1,-2,-3])==[1-1, 2-2, 3-3]
    assert inst.vec_add([1.5,2.5,3.7], [4.5,5.5,6.5])==[1.5+4.5,2.5+5.5,3.7+6.5] 
    assert inst.vec_add([],[])==[] 
    assert inst.vec_add([1,3,5], [3,5,6])==list(np.add([1,3,5], [3,5,6]))
    assert inst.vec_add([-1,-3,-5], [-3,-5,-6])==list(np.add([-1,-3,-5], [-3,-5,-6]))
    assert inst.vec_add([5.5,3,-7.5], [-3,5,-6])==list(np.add([5.5,3,-7.5], [-3,5,-6]))
    assert inst.vec_add([5.5,7.5,5.6], [3.6,5.5,9.9])==list(np.add([5.5,7.5,5.6], [3.6,5.5,9.9]))
    assert inst.vec_add([0,0,0],[0,0,0])==[0,0,0]
    assert inst.vec_add([-1,3,5], [0,0,0])==list(np.add([-1,3,5], [0,0,0]))
    try:
        assert inst.vec_add([0,0,0],[0,0])==0
    except ValueError as e:
        assert str(e)=="Please enter two vectors with the same length"
    try:
        assert inst.vec_add([0,0,None],[0,0,0])==0
    except ValueError as e:
        assert str(e)=="The first vector has an incorrect structure, please only enter vectors with integers and floats"
    try:
        assert inst.vec_add([0,0,0],[0,0,True])==0
    except ValueError as e:
        assert str(e)=="The second vector has an incorrect structure, please only enter vectors with integers and floats"
    

def vec_sub_test():
    """Tests the vecsub function with relevant testcases"""
    #Let us test the subtract function, well just use well just use some standard cases followed by more extensive testing with numpy such as only positives, only negatives, negatives and postives (and floats), only floats, zerovectors, followed by errors, 
    assert inst.vec_sub([1, 2, 3], [4, 5, 6])==[1-4,2-5,3-6]
    assert inst.vec_sub([1, 2, 3], [-1,-2,-3])==[1-(-1)*1, 2-(-1)*2, 3-(-1)*3]
    assert inst.vec_sub([1.5,2.5,3.7], [4.5,5.5,6.5])==[1.5-4.5,2.5-5.5,3.7-6.5] 
    assert inst.vec_sub([],[])==[] 
    assert inst.vec_sub([1,3,5], [3,5,6])==list(np.subtract([1,3,5], [3,5,6]))
    assert inst.vec_sub([-1,-3,-5], [-3,-5,-6])==list(np.subtract([-1,-3,-5], [-3,-5,-6]))
    assert inst.vec_sub([5.5,3,-7.5], [-3,5,-6])==list(np.subtract([5.5,3,-7.5], [-3,5,-6]))
    assert inst.vec_sub([5.5,7.5,5.6], [3.6,5.5,9.9])==list(np.subtract([5.5,7.5,5.6], [3.6,5.5,9.9]))
    assert inst.vec_sub([0,0,0],[0,0,0])==[0,0,0]
    assert inst.vec_sub([-1,3,5], [0,0,0])==list(np.subtract([-1,3,5], [0,0,0]))
    try:
        assert inst.vec_sub([0,0,0],[0,0])==0
    except ValueError as e:
        assert str(e)=="Please enter two vectors with the same length"
    try:
        assert inst.vec_sub([0,0,None],[0,0,0])==0
    except ValueError as e:
        assert str(e)=="The first vector has an incorrect structure, please only enter vectors with integers and floats"
    try:
        assert inst.vec_sub([0,0,0],[0,0,True])==0
    except ValueError as e:
        assert str(e)=="The second vector has an incorrect structure, please only enter vectors with integers and floats"

def norm_calc_test():
    """Tests the norm calc function with relevant testcases"""
    #Let us test the norm calc function, for this we will again do the same and test some standard cases followed by more exhaustive testing of various border cases such as only positives, only negatives, negatives and postives (and floats), only floats, zerovectors, followed by errors, 
    assert inst.norm_calc([1, 2, 4], "l1")==abs(1)+abs(2)+abs(4)
    assert inst.norm_calc([1, 2, 4], "l2")==math.sqrt(1**2+2**2+4**2)
    assert inst.norm_calc([1.5,2.5,3.7],"l1")==abs(1.5)+abs(2.5)+abs(3.7)
    assert inst.norm_calc([1.5,2.5,3.7],"l1")==abs(1.5)+abs(2.5)+abs(3.7)
    assert inst.norm_calc([],"l1") == 0 #What do we get when plugging nothing into the respective formulae? 0
    assert inst.norm_calc([],"l2") == 0
    assert inst.norm_calc([-1,-2,-3],"l1")==np.linalg.norm([-1,-2, -3],1)
    assert inst.norm_calc([-1,-2,-3],"l2") ==np.linalg.norm([-1,-2,-3])
    assert inst.norm_calc([1, 2, 3], "l1") == np.linalg.norm([1,2, 3],1)
    assert inst.norm_calc([1, 2, 5], "l2") == np.linalg.norm([1,2,5])
    assert inst.norm_calc([1.5, 2.5, 3.7],"l1") == np.linalg.norm([1.5,2.5,3.7],1)
    assert inst.norm_calc([0, 0, 0], "l1") == np.linalg.norm([0, 0, 0], 1)
    assert inst.norm_calc([0, 0, 0], "l2") == np.linalg.norm([0, 0, 0])
    try:
        assert inst.norm_calc([0,4,3,"hmm", True], "l1")
    except ValueError as e:
        assert str(e)=="Please enter a vector with only integers and floats"
    try:
        assert inst.norm_calc([0,4,3,0], True)
    except TypeError as e:
        assert str(e)=="Please enter what norm to calculate as a string, 'l1' or 'l2'"

def normalization_test():
    """Tests the normalization function with relevant testcases"""
    #Let us test the normal vector calculation, let us test for some standard cases, positives only, floats, and finally empty vectors, negative vectors and errors
    assert inst.normal_vec([1, 2, 4], "l1") == [1/7,2/7,4/7]  #note that abs(1+2+4)=7
    assert inst.normal_vec([1, 2, 4], "l2") == [1/math.sqrt(21), 2/math.sqrt(21), 4/math.sqrt(21)]  #note thats sqrt(1^2+2^2+4^2)
    assert inst.normal_vec([1.5, 2.5, 3.7],"L1")==[1.5/7.7,2.5/7.7,3.7/7.7]  #abs(1.5+2.5+3.7)
    assert inst.normal_vec([1.5, 2.5, 3.7],"L2")==[1.5/math.sqrt(22.19),2.5/math.sqrt(22.19),3.7/math.sqrt(22.19)]  #sqrt(1.5^2+2.5^2+3.7^2)
    assert inst.normal_vec([],"l1")==[]  
    assert inst.normal_vec([],"l2")==[]  
    assert inst.normal_vec([-1,-2,-4], "l1")==[-1/7,-2/7,-4/7] 
    assert inst.normal_vec([-1,-2,-4], "l2")==[-1/math.sqrt(21),-2/math.sqrt(21),-4/math.sqrt(21)] 
    try:
        assert inst.normal_vec([0,0,"Br"], "l1")
    except ValueError as e:
        assert str(e)=="Please enter a vector with only integers and floats"
    try:
        assert inst.normal_vec([0,4,3,0], "skrr")
    except TypeError as e:
        assert str(e)=="Please enter what norm to calculate, l1 or l2"
    try:
        assert inst.normal_vec([0,0,0],"l1")
    except ValueError as e:
        assert str(e)=="Division by zero not allowed, please enter a non zero vector"

def scal_prod_test():
    """Tests the scalprod function with relevant testcases"""
    #Let us test the scalarfunction, för k betraktar vi positiva, nollvärden negativa och floats, för vektorn betraktas tom vektor, nollvektor, positiv vektor och negativ vektor och slutligen errors
    assert inst.scal_prod(2,[1,2,10])==[2, 4, 20]
    assert inst.scal_prod(0, [1, 2, 10])==[0, 0, 0]
    assert inst.scal_prod(-1, [1, 2, 10]) == [-1, -2, -10]
    assert inst.scal_prod(2.5,[1, 2, 10]) == [2.5, 5.0, 25] 
    assert inst.scal_prod(2,[]) == []
    assert inst.scal_prod(3,[0, 0, 0])==[0,0,0]
    assert inst.scal_prod(2, [-1, -2, -10]) == [-2, -4, -20]
    try:
        assert inst.scal_prod("Tr",[3,4,5,6])
    except ValueError as e:
        assert str(e)=="Please enter a vector with only integers and floats and a constant value"
    try:
        assert inst.scal_prod(2,[3,True,5,6])
    except ValueError as e:
        assert str(e)=="Please enter a vector with only integers and floats and a constant value"

def proj_vec_test():
    """Tests the projection function with relevant testcases"""
    #Let us test the projection function, relevant test cases are positive vectors, projection onto the same vectors, vectors with positive and negative values, orthogonal vectors so well as a zero vector and floats followed by errors
    assert inst.proj_vec([1, 2, 4], [3,1,2]) == [13/21, 26/21, 52/21]  
    assert inst.proj_vec([1, 2, 2], [1, 2, 2]) == [1, 2, 2]
    assert inst.proj_vec([-1, 2, -3], [4, -5, -7]) == [-0.5, 1, -1.5]  
    assert inst.proj_vec([1, 0, 0], [0, 1, 0]) == [0, 0, 0]  #unitvectors are orthogonal, important test case!
    assert inst.proj_vec([-1, -2, -3], [-4, -5, -7]) == [-2.5, -5, -7.5]  
    assert inst.proj_vec([1, 0, 0], [0, 0, 0]) == [0, 0, 0]  
    assert inst.proj_vec([1.0, 2.0, 3.0], [4.0, 5.0, 7.0]) == [2.5, 5.0, 7.5] #please note that if the floats have decimal value we get inkongruent values with many decimals
    try:
        assert inst.proj_vec([0,0,0],[3,4,5])
    except ValueError as e:
        assert str(e)=="Division by zero not allowed, please enter a non zero vector"

def main():
    length_test()
    vec_check_test()
    dot_prod_test()
    cross_prod_test()
    test_vec_add()
    vec_sub_test()
    norm_calc_test()
    normalization_test()
    scal_prod_test()
    proj_vec_test()


if __name__ == "__main__":
    main()