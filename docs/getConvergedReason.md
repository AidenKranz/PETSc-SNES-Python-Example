# petsc4py.PETSc.SNES.getConvergedReason

[Petsc4py Documentation](https://petsc.org/release/petsc4py/reference/petsc4py.PETSc.SNES.html#petsc4py.PETSc.SNES.getConvergedReason) | 
[Source code at petsc4py/PETSc/SNES.pyx:1755](https://gitlab.com/petsc/petsc/-/tree/release/src/binding/petsc4py/src/petsc4py/PETSc/SNES.pyx#L1755)  
[C Source: SNESGetConvergedReason](https://petsc.org/release/manualpages/SNES/SNESGetConvergedReason/) | 
[Location](https://petsc.org/release/src/snes/interface/snes.c.html#SNESGetConvergedReason)

<br>

    def getConvergedReason(self) -> ConvergedReason:
        """
        Gets the reason the `SNES` iteration was stopped, which may be due to convergence, divergence, or stagnation

        Not collective.

        Returns
        -------
        reason : ConvergedReason
          negative value indicates diverged, positive indicates converged, zero indicates the `SNES` is still iterating.
        
        
        See Also
        --------
        setConvergedReason, petsc.SNESGetConvergedReason, ConvergedReason

        Examples
        --------
        Monitor the SNES and use getConvergedReason() to check its status while solving x^2-2=0:
        
        >>> import sys
        >>> from petsc4py import PETSc
        >>> 
        >>> def monitor(snes, it, rnorm):
        >>>     """
        >>>     Custom monitor function.
        >>>     snes: The SNES object
        >>>     its:  Current iteration number
        >>>     rnorm: Current L2 norm of the residual
        >>>     """
        >>>     # Print Update
        >>>     reason = snes.getConvergedReason()
        >>>     print(f"Convergence status: {reason}")
        >>> 
        >>> def form_function(snes, x, f):
        >>>     """
        >>>     Defines the function F(x) = x^2 - 2
        >>>     """
        >>>     x_val = x.array_r[0]
        >>>     f_val = x_val**2 - 2.0
        >>>     f.setArray([f_val])
        >>> 
        >>> # Initialize PETSc vectors
        >>> x = PETSc.Vec().createSeq(1)  # Solution vector
        >>> f = PETSc.Vec().createSeq(1)  # Residual vector
        >>> 
        >>> # Set initial guess
        >>> x.setArray([1.0]) 
        >>> 
        >>> # Create the SNES solver
        >>> snes = PETSc.SNES().create()
        >>> snes.setFunction(form_function, f)
        >>> 
        >>> # Set the custom monitor
        >>> snes.setMonitor(monitor)
        >>> 
        >>> # Solve
        >>> snes.setFromOptions() # Allows overriding via command line (e.g., -snes_monitor)
        >>> snes.solve(None, x)
        >>> 
        >>> print(f"Final Solution: {x.getArray()[0]}")
        Convergence status: 0
        Convergence status: 0
        Convergence status: 0
        Convergence status: 0
        Convergence status: 3
        Final Solution: 1.4142135623747067
        """
