import sympy as sp

x, y = sp.symbols("x y")

def parse_expression(expr_str: str):
    return sp.sympify(expr_str, locals={"x": x, "y": y, "sp": sp})

def evaluate_expression(expr_str: str, value_map: dict):
    expr = parse_expression(expr_str)
    return float(expr.evalf(subs=value_map))

def derivative(expr_str: str, var: str = "x"):
    sym_var = x if var == "x" else y
    expr = parse_expression(expr_str)
    return sp.diff(expr, sym_var)
