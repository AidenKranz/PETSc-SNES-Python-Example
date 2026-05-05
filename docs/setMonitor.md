# petsc4py.PETSc.SNES.setMonitor

[Petsc4py Documentation](https://petsc.org/release/petsc4py/reference/petsc4py.PETSc.SNES.html#petsc4py.PETSc.SNES.setMonitor) | 
[Source code at petsc4py/PETSc/SNES.pyx:1462](https://gitlab.com/petsc/petsc/-/blob/release/src/binding/petsc4py/src/petsc4py/PETSc/SNES.pyx?ref_type=heads#L1462)  
[C Source: SNESMonitorSet](https://petsc.org/release/manualpages/SNES/SNESMonitorSet/) | 
[Location](https://petsc.org/release/src/snes/interface/snes.c.html#SNESMonitorSet)

<br>

    def setMonitor(self, monitor, args, kargs) -> None:
        """
        Sets an additional function that is to be used at every iteration of the `SNES` nonlinear solver to display the iteration's progress.

        Logically collective.

        Parameters
        ----------
        monitor: SNESMonitorFunction | None
            The callback. This is a callable that must take at least 3 positional arguments:
                - snes: the `SNES` object
                - it: `int`, the current iteration
                - rnorm: `float`, norm of the residual
        args: tuple[Any, ...] | None, optional
            Additional positional arguments for the callback.
        kargs: dict[str, Any] | None, optional
            Additional keyword arguments for the callback.

        Returns
        -------
        None
        
        See Also
        --------
        getMonitor, petsc.SNESMonitorSet

        Examples
        --------
        Example monitoring the SNES while it solves x^2-2=0
        
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
        >>>     val = snes.getSolution().array_r[0]
        >>>     print(f"--- Iteration {it}: Residual Norm = {rnorm:.2e}, Current x = {val:.4f} ---")
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
        --- Iteration 0: Residual Norm = 1.00e+00, Current x = 1.0000 ---
        --- Iteration 1: Residual Norm = 2.50e-01, Current x = 1.5000 ---
        --- Iteration 2: Residual Norm = 6.94e-03, Current x = 1.4167 ---
        --- Iteration 3: Residual Norm = 6.01e-06, Current x = 1.4142 ---
        --- Iteration 4: Residual Norm = 4.56e-12, Current x = 1.4142 ---
        Final Solution: 1.4142135623747067
        """
