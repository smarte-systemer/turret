# Interpolation
 

Implements two different interpolation techniques:
- Linear
- Polynomial 

```{note}
Both are dependent on equally spaced x-values to work optimal. 
```
## Linear
This interpolation works by finding the smallest interval for $ y_a $ and $ y_b $ so that $ y $ is $ y\in[y_a, y_b] $

The linear interpolation is then calculated as:

\begin{gather*}
y=y_a + (y_b - y_a)\dot{\frac{x-x_a}{x_b-x_a}}
\end{gather*}


## Polynomial
Polynimal interpolation uses Lagrange polynomial calculation. This method works by calculating basis polynomial for each value set. These basis polynomials are summed togheter to produce an estimated y-value.

$$ P(x)=\sum_{i=1}^{n}{y_j\prod_{\begin{smallmatrix} j=0 & \\ j\neq i\end{smallmatrix}}^{n}\frac{x-x_i}{x_j-x_i}} $$

[Source](https://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html)


```{eval-rst}
.. automodule:: turret.interpolation
   :members:
   :undoc-members:
   :show-inheritance:
``` 