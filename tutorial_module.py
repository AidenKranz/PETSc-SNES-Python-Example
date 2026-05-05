import sys
import petsc4py
petsc4py.init(sys.argv)
from petsc4py import PETSc

class ApplicationContext:
    def __init__(self, n):
        self.n = n
        self.h = 1.0 / (n - 1)
        
        # Create vectors F (RHS) and U (Exact Solution)
        self.F = PETSc.Vec().createSeq(n)
        self.U = PETSc.Vec().createSeq(n)
        
        # Initialize right-hand side of PDE and exact solution
        xp = 0.0
        for i in range(n):
            v = 6.0 * xp + (xp + 1e-12)**6.0  # +1.e-12 prevents 0^6 domain errors
            self.F.setValue(i, v)
            
            v = xp**3
            self.U.setValue(i, v)
            xp += self.h

        self.F.assemble()
        self.U.assemble()

    def formInitialGuess(self, x):
        """Computes initial guess."""
        x.set(0.5)

    def formFunction(self, snes, x, f):
        """Evaluates nonlinear function, F(x)."""
        n = self.n
        d = (n - 1) ** 2.0
        
        # Obtain read/write arrays from PETSc vectors
        xx = x.array_r
        ff = f.array
        gg = self.F.array_r

        ff[0] = xx[0]
        for i in range(1, n - 1):
            ff[i] = d * (xx[i - 1] - 2.0 * xx[i] + xx[i + 1]) + xx[i]**2 - gg[i]
        ff[n - 1] = xx[n - 1] - 1.0
        

    def formJacobian(self, snes, x, J, P):
        """Evaluates Jacobian matrix."""
        n = self.n
        d = (n - 1) ** 2.0
        
        xx = x.array_r
        
        P.zeroEntries()
        
        # Boundary points
        P.setValue(0, 0, 1.0)
        P.setValue(n - 1, n - 1, 1.0)
        
        # Interior grid points
        for i in range(1, n - 1):
            cols = [i - 1, i, i + 1]
            vals = [d, -2.0 * d + 2.0 * xx[i], d]
            P.setValues([i], cols, vals)
            
        P.assemble()
        if J != P:
            J.assemble()
        # Returning SAME_NONZERO_PATTERN is required by PETSc
        return PETSc.Mat.Structure.SAME_NONZERO_PATTERN

# Global list to hold iteration history
iteration_history = []

def monitor(snes, its, fnorm):
    """User-defined monitoring routine."""
    reason = snes.getConvergedReason()
    PETSc.Sys.Print(f"iter = {its}, SNES Function norm {fnorm:g}")
    PETSc.Sys.Print("Still iterating" if reason == snes.ConvergedReason.ITERATING else "Iteration complete")
    # Get the current solution vector from the SNES context
    x_current = snes.getSolution()

    # Request read-only access to the array
    arr = x_current.array_r 
    
    # Make a copy for our history list
    iteration_history.append(arr.copy()) 


def main():
    OptDB = PETSc.Options()
    n = OptDB.getInt('n', 5)
    
    comm = PETSc.COMM_WORLD
    if comm.getSize() != 1:
        PETSc.Sys.Print("This is a uniprocessor example only!")
        sys.exit(1)
        
    appctx = ApplicationContext(n)
    
    # -------------------------------------------------------------------------
    # Create vector data structures; set function evaluation routine
    # -------------------------------------------------------------------------
    x = PETSc.Vec().createSeq(n)
    r = x.duplicate()
    
    x.setName("Approximate Solution")
    appctx.U.setName("Exact Solution")
    
    # -------------------------------------------------------------------------
    # Create nonlinear solver context
    # -------------------------------------------------------------------------
    snes = PETSc.SNES().create(comm)
    snes.setFunction(appctx.formFunction, r)
    
    # -------------------------------------------------------------------------
    # Create matrix data structure; set Jacobian evaluation routine
    # -------------------------------------------------------------------------
    J = PETSc.Mat().createAIJ(size=[n, n], nnz=3, comm=comm)
    J.setFromOptions()
    J.setUp()
    
    snes.setJacobian(appctx.formJacobian, J, J)
    
    # -------------------------------------------------------------------------
    # Customize nonlinear solver; set runtime options
    # -------------------------------------------------------------------------
    # Set an optional user-defined monitoring routine
    snes.setMonitor(monitor)
    iteration_history.clear()
    snes.setFromOptions()
    
    # Print parameters used for convergence testing (optional)
    abstol, rtol, stol, maxit = snes.getTolerances()
    PETSc.Sys.Print(f"atol={abstol:g}, rtol={rtol:g}, stol={stol:g}, maxit={maxit}")
    
    # -------------------------------------------------------------------------
    # Evaluate initial guess; then solve nonlinear system
    # -------------------------------------------------------------------------
    appctx.formInitialGuess(x)
    
    snes.solve(None, x)
    its = snes.getIterationNumber()
    PETSc.Sys.Print(f"number of SNES iterations = {its}\n")
    
    # -------------------------------------------------------------------------
    # Check solution and clean up
    # -------------------------------------------------------------------------
    # Calculate difference between approximate x and exact U
    x.axpy(-1.0, appctx.U) 
    norm = x.norm(PETSc.NormType.NORM_2)
    PETSc.Sys.Print(f"Norm of error {norm:g}, Iterations {its}")

    # -------------------------------------------------------------------------
    # Visualizing the Solver's Progress
    # -------------------------------------------------------------------------
    import numpy as np
    import matplotlib.pyplot as plt
    
    domain = np.linspace(0, 1.0, n)
    plt.figure(figsize=(8, 5))
    
    # Plot each iteration's guess
    for i, guess in enumerate(iteration_history):
        plt.plot(domain, guess, marker='.', label=f'Iteration {i}')
        
    # Plot the exact solution for reference
    plt.plot(domain, appctx.U.getArray(), 'k--', linewidth=2, label='Exact Solution')
    
    plt.title("Newton Method Convergence History")
    plt.xlabel('Domain (x)')
    plt.ylabel('u(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
if __name__ == '__main__':
    main()