# Vector-Calculus-Library
VectorCalculations is a library that provides calculation for frequently used linear algebra vector operations developed in early 2024.

## Features
**Vector length Function:** Checks that the length of two vectors `v1` and `v2` are equal.

**Vector Check Function:** Checks that a given vector `vek` only contains numbers

**Dot Product Calculator:** Calculates the dot product of two vectors `v1` and `v2` 

**Cross Product Calculator:** Calculates the cross product of two vectors `v1` and `v2` 

**Vektor Addition Calculator:** Add together two vectors `v1` and `v2`.

**Vektor Subtraction Calculator:** Subtracts two vectors `v1` and `v2`.

**Norm Calculator:** Calculates the norm a vector `vek`  given the choice between l1- and l2 norm as an (str) `entry`.

**Normalize Function:** Normalizes a vector `vek` given the choice between l1- and l2 normalization as an (str) `entry`.

**Scalar Product Calculator:** Calculates the scalar product gives a vector `vek` and a scalar `k`.

**Projection Calculator:** Calculates the projection of a vector `v1` onto `v2`.



## Documentation

```python
@staticmethod
def  length_check(vek1,vek2):
"""Function that checks that the length of the vectors are equivalent"""

@staticmethod
def  vec_check(vek):
"""Function that checks that we have a vector with acceptable numbers"""

def  dot_prod(self, vek1, vek2):
"""Function that takes in two vectors and calculates the dot product"""

def  cross_prod(self, vek1, vek2):
"""Function that takes in two vectors and returns the cross product"""

def  vec_add(self, vek1, vek2):
"""Function that takes in two vectors and returns the sum of the two vectors"""

def  vec_sub(self, vek1, vek2):
"""Function that takes in two vectors and returns the difference of the two vectors"""

def  norm_calc(self,vek, entry):
"""Function that calculates the l1 or l2 norm of a vector"""

def  normal_vec(self,vek, entry):
"""Function that calculates that l1 or l2 normalizes a vector"""

def  scal_prod(self,c, vek):
"""Function that calculates the scalar product of a vector given a vector and a scalar"""

def  proj_vec(self,vek1, vek2):
"""Function that performs projection of vek1 onto vek2""" 
````

### Roadmap

* The API of this library is frozen.
* Version numbers adhere to [semantic versioning](http://semver.org/).
