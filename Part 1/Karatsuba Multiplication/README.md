# Karatsuba Multiplication in Python

## Problem
Using the standard multiplication to multiply two numbers works well for realtively smaller numbers.  
But what about **really large** numbers? Instead of using the standard multiplication algo which takes O(n<sup>2</sup>) time
**we will use a divide and conquer approach.**  
This algorithm was developed by Anatoly Karatsuba, a russian mathematician, in 1960. 

**Note:** _This works for numbers with even # of digits, but it can be just as easily extended to numbers with odd # of digits._

## Pseudo Code
**Input:** two n-digit positive integers x and y.
**Output:** the product x · y.  
**Assumption:** n is a power of 2.
```
if n = 1 then // base case
  compute x · y in one step and return the result
else // recursive case
  a, b := first and second halves of x
  c, d := first and second halves of y
  compute p := a + b and q := c + d using grade-school addition
  recursively compute ac := a · c, bd := b · d, and
  pq := p · q
  compute adbc := pq-ac-bd using grade-school addition
  compute 10n · ac + 10n/2 · adbc + bd using grade-school addition and return the result
```

## Approach
Consider 2 numbers x and y to be multiplied.
Now, let a & b be first and last halves of x, and c & d for y.
Now, thier multiplication can be written as:  

![formula1](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20x%20%5Ccdot%20y%20%3D%20%2810%5E%7B%5Cfrac%7Bn%7D%7B2%7D%7D%20a%20&plus;%20b%29%20%5Ccdot%20%2810%5E%7B%5Cfrac%7Bn%7D%7B2%7D%7D%20c%20&plus;%20d%29)  
![formula2](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20x%20%5Ccdot%20y%20%3D%2010%5E%7Bn%7D%20%B7%20%28ac%29%20&plus;%2010%5E%7B%5Cfrac%7Bn%7D%7B2%7D%7D%20%B7%20%28a%20%B7%20d%20&plus;%20b%20%B7%20c%29%20&plus;%20b%20%B7%20d)

Now, the thing is, we will need 4 recursive calls to execute this equation, which means the recurrence relation will be:  

![recrela1](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20T%28n%29%20%5Cleq%204%20%5Ccdot%20T%28%5Cfrac%7Bn%7D%7B2%7D%29%20&plus;%20O%28n%29)

This still gives a running time of **O(n<sup>2</sup>)**
But the genius of Karatsuba realised that we can get away with just 3 recursive calls with some magical mathematical rearrangement.  

![formula3](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%28a&plus;b%29%28c&plus;d%29-ac-bd%20%3D%20ad%20&plus;%20bc)

Replacing this, the recurrence relation becomes:  

![recrela2](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20T%28n%29%20%5Cleq%203%20%5Ccdot%20T%28%5Cfrac%7Bn%7D%7B2%7D%29%20&plus;%20O%28n%29)

Thus, the overall running time reduces to 

![runningtime](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20O%28n%5E%7B%5Clog_%7B2%7D%203%7D%29%20%5Capprox%20O%28n%5E%7B1.585%7D%29)
