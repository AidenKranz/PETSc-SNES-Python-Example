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
        Create a function to monitor the SNES
        
        >>> def monitor(snes, it, rnorm):
        >>>     PETSc.Sys.Print(f"iter = {its}, SNES Function norm {fnorm:g}")

        Set the monitor with setMonitor()
        
        >>> ...
        >>> snes.setMonitor(monitor)
        >>> snes.setFromOptions()
        >>> ...
        """
