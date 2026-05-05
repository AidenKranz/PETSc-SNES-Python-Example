[Original Documentation](https://petsc.org/release/petsc4py/reference/petsc4py.PETSc.Mat.html#petsc4py.PETSc.Mat.setFromOptions)

# petsc4py.PETSc.Mat.setFromOptions

[Petsc4py Documentation](https://petsc.org/release/petsc4py/reference/petsc4py.PETSc.Mat.html#petsc4py.PETSc.Mat.setFromOptions) | 
[Source code at petsc4py/PETSc/Mat.pyx:1974](https://gitlab.com/petsc/petsc/-/tree/release/src/binding/petsc4py/src/petsc4py/PETSc/Mat.pyx#L1974)  
[C Source: MatSetFromOptions](https://petsc.org/release/manualpages/Mat/MatSetFromOptions/) | 
[Location](https://petsc.org/release/src/mat/utils/gcreate.c.html#MatSetFromOptions)

<br>

    def setFromOptions(self) -> None:
        """
        Set up the internal data structures for using the matrix with the relevant command line arguments or options database.

        Collective.

        See Also
        --------
        petsc.MatSetUp

        Notes
        -----

        Valid arguments include:
            -mat_type seqaij
                MATSEQAIJ type, uses MatCreateSeqAIJ(), designed for single-processor sparse matrices based on the Compressed Sparse Row format. Requires that non zero entrie be allocated before using.
            -mat_type mpiaij
                MATMPIAIJ type, uses MatCreateAIJ(), used for parallel sparse matrices.
            -mat_type seqdense
                MATSEQDENSE type, uses MatCreateSeqDense(), used for sequential dense matrices.
            -mat_type mpidense
                MATMPIDENSE, uses MatCreateDense(), used for distributed dense matrices.
            -mat_type seqbaij
                MATSEQBAIJ, uses MatCreateSeqBAIJ(), used for sequential block sparse matrices, based on block sparse compressed row format. Can also have the argument:
                    -mat_baij_mult_version version - indicate the version of the matrix-vector product to use (0 often indicates using BLAS)
            -mat_type mpibaij
                MATMPIBAIJ, uses MatCreateBAIJ(), a matrix type to be used for distributed block sparse matrices. Can also have the arguments:
                    -mat_block_size bs - set the blocksize used to store the matrix
                    -mat_baij_mult_version version - indicate the version of the matrix-vector product to use (0 often indicates using BLAS)
                    -mat_use_hash_table fact - set hash table factor
            -mat_vec_type
                Specifies the VecType used by MatCreateVecs(), see MatSetVecType()
        
        Examples
        --------
        Create a matrix using the default argument `-mat_type seqaij`
        
        >>> from petsc4py import PETSc
        >>> A = PETSc.Mat().create()
        >>> A.setSizes([2, 2])
        >>> for x,y in [(x, y) for x in [0,1] for y in [0,1]]:
        >>>     A.setValue(x,y,x+y)
        >>> A.setFromOptions() 
        >>> A.setUp()
        >>> A.assemble()
        >>> v = PETSc.Viewer()
        >>> v(A)
        Mat Object: 1 MPI process
          type: seqaij
        row 0: (0, 0.)  (1, 1.) 
        row 1: (0, 1.)  (1, 2.) 
        """
