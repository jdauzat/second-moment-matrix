# ISAT 690 Special Topics | Assignment 1

Second moment matrix M is defined as: 

$$M = \sum_{x,y}w(x,y)\begin{bmatrix}
I_x^2&I_xI_y\\
I_xI_y&I_y^2\\
\end{bmatrix}$$

Where, w (x,y) is a 3x3 window function and its value is 1 for all x and y, $I_x$ is the gradient of I with
respect to x and $I_y$ is the gradient of I with respect to y.

## Input Image I

$$\begin{bmatrix}
10&10&10&10&10&10&10&10&10&10\\
10&10&10&10&10&10&10&10&10&10\\
10&10&10&10&10&10&10&10&10&10\\
10&10&50&60&60&60&60&60&10&10\\
10&10&50&60&60&60&60&60&10&10\\
10&10&50&50&10&10&10&10&10&10\\
10&10&50&50&10&10&10&10&10&10\\
10&10&50&50&10&10&10&10&10&10\\
10&10&50&50&10&10&10&10&10&10\\
10&10&50&50&10&10&10&10&10&10\\
\end{bmatrix}$$

1) Find the gradient of the input image with respect to x and y. Gradients of image I with respect to x
and y are given as;

$$\frac{\partial I}{\partial x}[x,y] = {I_x \approx I[x+ 1, y] - I[x, y]}$$

$$\frac{\partial I}{\partial y}[x,y] = {I_y \approx I[x, y+1] - I[x, y]}$$

2) Find matrix M for the pixels marked by red. Window function w(x,y) is a 3x3 window with all values
equal to 1.
