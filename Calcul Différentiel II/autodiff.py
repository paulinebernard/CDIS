"""

   >>> from math import pi

Scalar Functions
--------------------------------------------------------------------------------

    >>> def f(x):
    ...     return pi
    >>> g = deriv(f)
    >>> g(0.0)
    0.0
    >>> g(1.0)
    0.0

    >>> def f(x):
    ...     return 2 * x + 1.0
    >>> g = deriv(f)
    >>> g(0.0)
    2.0
    >>> g(1.0)
    2.0
    >>> g(2.0)
    2.0

    >>> def f(x):
    ...     return x * x + 2 * x + 1
    >>> g = deriv(f)
    >>> g(0.0)
    2.0
    >>> g(1.0)
    4.0
    >>> g(2.0)
    6.0

    >>> def f(x):
    ...     return x ** 2 + 2 * x + 1
    >>> g = deriv(f)
    
    Here g(0.0) won't work 
    
    >>> g(1.0)
    4.0
    >>> g(2.0)
    6.0

    >>> def f(x):
    ...    return cos(x) * cos(x) + sin(x) * sin(x)
    >>> g = deriv(f)
    >>> g(0.0)
    0.0
    >>> g(pi/4)
    0.0
    >>> g(pi/2)
    0.0

    >>> def f(x):
    ...     return sin(x) * cos(x)
    >>> g = deriv(f)
    >>> def h(x):
    ...     return cos(x) * cos(x) - sin(x) * sin(x)
    >>> g(0.0) == h(0.0)
    True
    >>> g(pi/4) == h(pi/4)
    True
    >>> g(pi/2) == h(pi/2)
    True

Multivariable Functions
--------------------------------------------------------------------------------

    >>> def f(x, y):
    ...     return 1.0
    >>> grad(f)(0.0, 0.0)
    [0.0, 0.0]
    >>> grad(f)(1.0, 2.0)
    [0.0, 0.0]

    >>> def f(x, y):
    ...     return x + 2 * y + 1
    >>> grad(f)(0.0, 0.0)
    [1.0, 2.0]
    >>> grad(f)(1.0, 2.0)
    [1.0, 2.0]

    >>> def f(x, y):
    ...     return x * x + y * y
    >>> grad(f)(0.0, 0.0)
    [0.0, 0.0]
    >>> grad(f)(1.0, 2.0)
    [2.0, 4.0]

Branching
--------------------------------------------------------------------------------

    >>> def f(x):
    ...     if x < 0.0:
    ...         return -x
    ...     else:
    ...         return x
    >>> g = deriv(f)
    >>> g(-1.0)
    -1.0
    >>> g(1.0)
    1.0

    >>> def f(x):
    ...     if x <= 0.0:
    ...         return 0.0
    ...     else:
    ...         return x * x
    >>> g = deriv(f)
    >>> g(-1.0)
    0.0
    >>> g(1.0)
    2.0

    >>> def f(x): 
    ...     return (x > 0) * x * x
    >>> g = deriv(f)
    >>> g(-1.0) == 0.0 # actually, -0.0
    True
    >>> g(1.0)
    2.0

"""

# TODO: 
#   - constant wrapping
#   - test management (branching)

# Python 3.7 Standard Library
import doctest
import inspect
import math 
import operator

# ------------------------------------------------------------------------------
class Node:
    def __init__(self, value, function=None, *args):
         self.value = value
         self.function = function
         self.args = args
    def __str__(self):
        if self.function is None:
            return str(self.value)
        else:
            function_name = self.function.__qualname__
            args_str = ", ".join(str(arg) for arg in self.args)
            return f"{function_name}({args_str})"
    def ___repr__(node):
        reprs = [repr(self.value)]
        if self.function is not None:
            reprs.append(self.function.__qualname__)
        if self.args:
            reprs.extend([repr(arg) for arg in self.args])
        args_repr = ", ".join(reprs)
        return f"Node({args_repr})"

def autodiff(function):
    def autodiff_function(*args):
        if any([isinstance(arg, Node) for arg in args]):
            node_args = []
            values = []
            for arg in args:
                if isinstance(arg, Node):
                    node_args.append(arg)
                    values.append(arg.value)
                else:
                    node_args.append(Node(arg)) 
                    values.append(arg)
            output_value = function(*values)
            output_node = Node(output_value, autodiff_function, *node_args)
            return output_node
        else:
            return function(*args)        
    autodiff_function.__qualname__ = function.__qualname__
    return autodiff_function

# Function and Operators
# ------------------------------------------------------------------------------
functions  = ["exp", "log", "sqrt", "sin", "cos", "tan"]
operators  = ["add", "sub", "mul", "truediv", "pow"]
operators += ["neg", "pos"]
operators += ["lt", "le", "ge", "gt"] # not ne or eq ; fucks up the current
# topological sort. Of cours we could work with ids in the topological sort,
# or have a global flag to disable node outputs but it's overkill;
# x == y does generate "thin sets" in general where the differential
# cannot be computed.

globs = globals()
for function_name in functions:
    function = getattr(math, function_name)
    function = autodiff(function)
    globs[function_name] = function
for operator_name in operators:
    op = getattr(operator, operator_name)
    binary_op = (len(inspect.signature(op).parameters) == 2)
    op = autodiff(op)
    globs[operator_name] = op
    setattr(Node, f"__{operator_name}__", op)
    if binary_op:
        setattr(Node, f"__r{operator_name}__", op)
def _bool(x):
    if isinstance(x, Node):
        return bool(x.value)
    else:
        return bool(x)
Node.__bool__ = _bool


# Elementary Differentials 
# ------------------------------------------------------------------------------

differential = {}

# Derivative to Differential
def d_from_derivative(f_prime): # TODO: extend to partials ?
    def d_f(x):
        return lambda dx: f_prime(x) * dx
    return d_f

differential[exp] = d_from_derivative(exp)
differential[log] = d_from_derivative(lambda x: - 1.0 / x)
def d_pow(x, y):
    return lambda dx, dy: pow(x, y) * (y / x * dx + log(x) * dy)
differential[pow] = d_pow
differential[sqrt] = d_from_derivative(lambda x: 0.5 / sqrt(x))
differential[sin] = d_from_derivative(cos)
differential[cos] = d_from_derivative(lambda x: - sin(x))
differential[tan] = d_from_derivative(lambda x: 1.0 / (cos(x) * cos(x)))

differential[add] = lambda x, y: add
differential[sub] = lambda x, y: sub
def d_mul(x, y):
    return lambda dx, dy: dx * y + x * dy
differential[mul] = d_mul
def d_truediv(x, y):
    return lambda dx, dy: dx / y - x / y / y * dy 
differential[truediv] = d_truediv
differential[neg] = lambda x: neg
differential[pos] = lambda x: pos

def zero(dx, dy):
    return 0.0
differential[lt] = lambda x, y: zero
differential[le] = lambda x, y: zero
differential[ge] = lambda x, y: zero
differential[gt] = lambda x, y: zero

# Topological Sort
# ------------------------------------------------------------------------------
def sort_nodes(end_node):
    todo = [end_node]
    nodes = []
    while todo:
        node = todo.pop()
        nodes.append(node)
        for parent in node.args:
            if parent not in nodes + todo:
                todo.append(parent) 
    done = []
    while nodes:
        for node in nodes[:]:
            if all([parent in done for parent in node.args]):
                done.append(node)
                nodes.remove(node)
    return done

# Automatic Differentation
# ------------------------------------------------------------------------------
def d(f):
    def df(*args): # args=(x1, x2, ...)
        start_nodes = [Node(arg) for arg in args]
        end_node = f(*start_nodes)
        if not isinstance(end_node, Node): # constant output
            end_node = Node(end_node)
        sorted_nodes = sort_nodes(end_node).copy()
        def df_x(*d_args): # d_args = (d_x1, d_x2, ...)
            for node in sorted_nodes:
                if node in start_nodes:
                    i = start_nodes.index(node)
                    node.d_value = d_args[i]
                elif node.function is None: # constant node
                    node.d_value = 0.0
                else:
                    _d_f = differential[node.function]
                    _args = node.args
                    _args_values = [_node.value for _node in _args]
                    _d_args = [_node.d_value for _node in _args]
                    node.d_value = _d_f(*_args_values)(*_d_args)
            return end_node.d_value
        return df_x
    df.__qualname__ = "d_" + f.__qualname__
    return df

# Differential Operators
# ------------------------------------------------------------------------------
def deriv(f):
    df = d(f)
    def deriv_f(x):
        return df(x)(1.0)
    return deriv_f

def grad(f):
    df = d(f)
    def grad_f(*args):
        n = len(args)
        grad_f_x = n * [0.0]
        df_x = df(*args)
        for i in range(0, n):
            e_i = n * [0.0]; e_i[i] = 1.0
            grad_f_x[i] = df_x(*e_i)
        return grad_f_x  
    return grad_f

# Unit Tests
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    doctest.testmod()