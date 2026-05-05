# Summary

This tutorial demonstrates how to use petscy4py to solve the differential equation $u'' + u^{2} = f$, sequentially. 

`tutorial_module.py` uses the Newton method on the interval $[0,1]$ with grid spacing $h = \frac{1}{n-1}$ and $n=5$ by first 
expressing the problem as a root-finding problem $F(u)=0$ where $F(u) = u'' + u^{2} - f$. In this example, $f$ is defined in 
`ApplicationContext.F` as $f(x)=6x + x^6$. With border conditions of $u(0)=0$ and $u(1)=1$, the true solution to this problem is $u(x)=x^3$.

In `tutorial_presentation.ipynb` you will find a visualization of the solver's progress. After 3 iterations,
the Newton method produces $\hat{u}$ with a norm of error of $1.49751e-10$

## AI Translation

Google Gemini was used to translate this example from the C tutorial found at https://petsc.org/release/src/snes/tutorials/ex2.c.html. After 
fixing a few minor hallucinations, the output was compared with the original script to confirm accuracy.

## petsc4py documentation

In `docs/` There are Markdown files containing three new docstrings (including links to the
relevant PETSc GitLab lines) for petsc4py used in this project that might be lacking in documentation compared to others.
