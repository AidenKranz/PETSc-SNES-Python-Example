[Original Documentation](https://petsc.org/release/petsc4py/reference/petsc4py.PETSc.SNES.html#petsc4py.PETSc.SNES.setMonitor)

def setMonitor(self,
                   monitor: SNESMonitorFunction  | None,
                   args: tuple[Any, ...] | None = None,
                   kargs: dict[str, Any] | None = None) -> None:
        """Set the callback used to monitor solver convergence.

        Logically collective.

        Parameters
        ----------
        monitor
            The callback.
        args
            Positional arguments for the callback.
        kargs
            Keyword arguments for the callback.

        See Also
        --------
        getMonitor, petsc.SNESMonitorSet

        """
