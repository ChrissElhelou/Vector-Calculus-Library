import math
import numpy as np

class VectorCalculations:
    #https://www.tutorialsteacher.com/python/staticmethod-decorator vi återanvänder kod

    @staticmethod
    def length_check(vek1,vek2):
        """Function that checks that the length of the vectors are equivalent"""
        if isinstance(vek1, (list)) and isinstance(vek2, (list)) and len(vek1)==len(vek2) :
            return True
        else:
            return False
        
    @staticmethod
    def vec_check(vek):
        """Function that checks that we have a vector with acceptable numbers"""
        if isinstance(vek, list) and all(isinstance(x, (int,float)) and not isinstance(x, bool) for x in vek):
            return True
        else:
            return False
        
    def dot_prod(self, vek1, vek2):
        """Function that takes in two vectors and calculates the dot product"""
        prod=0
        if not self.length_check(vek1,vek2):
            raise ValueError("Please enter two vectors with the same length")
        if not self.vec_check(vek1):
            raise ValueError("The first vector has an incorrect structure, please only enter vectors with integers and floats")
        if not self.vec_check(vek2):
            raise ValueError("The second vector has an incorrect structure, please only enter vectors with integers and floats")
        for i in range(len(vek1)):
            prod=prod+vek1[i]*vek2[i]
        return prod

    def cross_prod(self, vek1, vek2):
        """Function that takes in two vectors and returns the cross product"""
        if not self.vec_check(vek1) or not self.vec_check(vek2):
            raise ValueError("Please enter two vectors with integers and floats")
        if len(vek1)!= 3:
            raise ValueError("The first vektor has an incorrect length, please enter a vector with 3 numbers")
        if len(vek2)!= 3:
            raise ValueError("The second vektor has an incorrect length, please enter a vector with 3 numbers")
        prod=[vek1[1]*vek2[2]-vek1[2]*vek2[1], vek1[2]*vek2[0]-vek1[0]*vek2[2], vek1[0]*vek2[1]-vek1[1]*vek2[0]]
        return prod

    def vec_add(self, vek1, vek2):
        """Function that takes in two vectors and returns the sum of the two vectors"""
        sum=[]
        if not self.length_check(vek1,vek2):
            raise ValueError("Please enter two vectors with the same length")
        if not self.vec_check(vek1):
            raise ValueError("The first vector has an incorrect structure, please only enter vectors with integers and floats")
        if not self.vec_check(vek2):
            raise ValueError("The second vector has an incorrect structure, please only enter vectors with integers and floats")
        for i in range(len(vek1)):
            sum.append(vek1[i]+vek2[i])
        return sum

    def vec_sub(self, vek1, vek2):
        """Function that takes in two vectors and returns the difference of the two vectors"""
        diff=[]
        if not self.length_check(vek1,vek2):
            raise ValueError("Please enter two vectors with the same length")
        if not self.vec_check(vek1):
            raise ValueError("The first vector has an incorrect structure, please only enter vectors with integers and floats")
        if not self.vec_check(vek2):
            raise ValueError("The second vector has an incorrect structure, please only enter vectors with integers and floats")
        for i in range(len(vek1)):
            diff.append(vek1[i]-vek2[i])
        return diff

    def norm_calc(self,vek, entry):
        """Function that calculates the l1 or l2 norm of a vector"""
        if not self.vec_check(vek):
            raise ValueError("Please enter a vector with only integers and floats")
        if not isinstance(entry, (str)) or entry.lower() not in {"l1", "l2"}:
            raise TypeError("Please enter what norm to calculate as a string, 'l1' or 'l2'")
        norm=0
        if entry.lower()=="l1":
            for elem in vek:
                norm=norm+abs(elem)
        elif entry.lower()=="l2":
            for elem in vek:
                norm=norm+elem**2
            norm=math.sqrt(norm)
        return norm

    def normal_vec(self,vek, entry):
        """Function that calculates that l1 or l2 normalizes a vector"""
        if not self.vec_check(vek):
            raise ValueError("Please enter a vector with only integers and floats")
        if not isinstance(entry,(str)) or entry.lower() not in {"l1", "l2"}:
            raise TypeError("Please enter what norm to calculate, l1 or l2")
        norm=self.norm_calc(vek, entry)
        if norm==0 and len(vek)!=0:
            raise ValueError("Division by zero not allowed, please enter a non zero vector")
        norm_vec=[]
        for elem in vek:
            norm_vec.append(elem/norm)
        return norm_vec

    def scal_prod(self,c, vek):
        """Function that calculates the scalar product of a vector given a vector and a scalar"""
        if not self.vec_check(vek) or isinstance(c,(bool)) or not isinstance(c,(int,float)):
            raise ValueError("Please enter a vector with only integers and floats and a constant value")
        prod=[]
        for elem in vek:
            prod.append(c*elem)
        return prod

    def proj_vec(self,vek1, vek2):
        """Function that performs projection of vek1 onto vek2"""
        prod_vektors=self.dot_prod(vek1,vek2)
        vek1_norm=self.dot_prod(vek1, vek1)
        if vek1_norm !=0:
            k=prod_vektors/vek1_norm
            res_vek=self.scal_prod(k,vek1)
        else:
            raise ValueError("Division by zero not allowed, please enter a non zero vector")
        return res_vek