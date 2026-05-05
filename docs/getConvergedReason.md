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
        (See tutorial_module.py) Create a function to monitor the SNES and use getConvergedReason() to check its status:
        
        >>> def monitor(snes, it, rnorm):
        >>>     reason = snes.getConvergedReason()
        >>>     PETSc.Sys.Print("Still iterating" if reason == snes.ConvergedReason.ITERATING else "Iteration complete")

        Set the monitor, and solve.
        
        >>> ...
        >>> snes.setMonitor(monitor)
        >>> snes.setFromOptions()
        >>> ...
        >>> snes.solve(None, x)
        >>> its = snes.getIterationNumber()
        >>> PETSc.Sys.Print(f"number of SNES iterations = {its}\n")
        Still iterating
        Still iterating
        Still iterating
        Iteration complete
        number of SNES iterations = 3
        """
