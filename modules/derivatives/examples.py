import sympy as sp

EXAMPLES = [
    {
        "expression": "x**2",
        "derivative": "2*x",
        "description": "Basic power rule example."
    },
    {
        "expression": "sp.sin(x)",
        "derivative": "sp.cos(x)",
        "description": "Derivative of sine."
    }
]

def get_examples():
    return EXAMPLES
