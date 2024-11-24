# linear_solver_utils.py
import numpy as np

def solve_linear_system(coefficients):
    """
    Solve a system of linear equations using numpy.
    
    Args:
        coefficients: List of lists containing equation coefficients and constants
                     For example: [[a1, b1, c1], [a2, b2, c2]] for a system of 2 equations
                     where c1 and c2 are the constants (right-hand side of equations)
    
    Returns:
        numpy array with solution values for variables
    """
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

def check_solution_stability(A, b, solution):
    """
    Check the stability of the solution using condition number.
    
    Args:
        A: Coefficient matrix
        b: Constants vector
        solution: Computed solution
    
    Returns:
        dict containing condition number and stability assessment
    """
    cond_num = np.linalg.cond(A)
    
    stability = {
        'condition_number': cond_num,
        'is_stable': cond_num < 1e10,
        'assessment': 'stable' if cond_num < 1e10 else 'potentially unstable'
    }
    
    return stability

def get_solution_accuracy(A, b, solution):
    """
    Calculate the accuracy of the solution.
    
    Args:
        A: Coefficient matrix
        b: Constants vector
        solution: Computed solution
    
    Returns:
        float: relative error norm
    """
    residual = np.dot(A, solution) - b
    relative_error = np.linalg.norm(residual) / np.linalg.norm(b)
    return relative_error

def generate_points_for_plotting(coefficients, x_range=(-10, 10), num_points=100):
    """
    Generate points for plotting the equations.
    
    Args:
        coefficients: List of equation coefficients
        x_range: Tuple of (min_x, max_x)
        num_points: Number of points to generate
    
    Returns:
        dict containing x and y values for each equation
    """
    x = np.linspace(x_range[0], x_range[1], num_points)
    equations_points = []
    
    for coeff in coefficients:
        a, b, c = coeff
        if b != 0:
            y = (-a*x + c) / b
        else:
            # Handle vertical lines
            x_val = c/a if a != 0 else np.nan
            y = np.full_like(x, np.nan)
            x = np.full_like(x, x_val)
        
        equations_points.append({
            'x': x,
            'y': y
        })
    
    return equations_points