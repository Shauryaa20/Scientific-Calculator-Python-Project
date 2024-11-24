# linear_solver_utils.py
import numpy as np

def solve_linear_system(coefficients):
    try:
        # Convert to numpy array
        coeff_array = np.array(coefficients)
        
        # Split into coefficient matrix A and constants b
        A = coeff_array[:, :-1]
        b = coeff_array[:, -1]
        
        # Check if system is solvable
        rank_A = np.linalg.matrix_rank(A)
        rank_Ab = np.linalg.matrix_rank(np.column_stack((A, b)))
        
        if rank_A < rank_Ab:
            raise ValueError("System has no solution")
        elif rank_A < A.shape[1]:
            raise ValueError("System has infinitely many solutions")
        
        # Solve the system
        solution = np.linalg.solve(A, b)
        
        # Verify solution
        if not np.allclose(np.dot(A, solution), b):
            raise ValueError("Failed to find accurate solution")
            
        return solution

    except np.linalg.LinAlgError:
        raise ValueError("System is not solvable (singular matrix)")
    except Exception as e:
        raise ValueError(f"Error solving system: {str(e)}")