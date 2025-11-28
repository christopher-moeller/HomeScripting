import ast
import os
import importlib.util

scripts_base_folder = "scripts"

def list_paths_for_scripts():
    script_filenames = [f for f in os.listdir(scripts_base_folder) if f.endswith(".py")]
    return [os.path.join(scripts_base_folder, s) for s in script_filenames]

def list_top_level_functions(script_path):
    with open(script_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=script_path)
    return [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]

def get_function_parameters(script_path, function_name):
    """
    Returns a list of parameters for a given function in a script,
    including type annotations if provided.
    Format: [(param_name, type_annotation_or_None), ...]
    """
    with open(script_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=script_path)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            params = []

            # Regular arguments
            for arg in node.args.args:
                annotation = ast.unparse(arg.annotation) if arg.annotation else None
                params.append((arg.arg, annotation))

            # *args
            if node.args.vararg:
                annotation = ast.unparse(node.args.vararg.annotation) if node.args.vararg.annotation else None
                params.append(("*" + node.args.vararg.arg, annotation))

            # **kwargs
            if node.args.kwarg:
                annotation = ast.unparse(node.args.kwarg.annotation) if node.args.kwarg.annotation else None
                params.append(("**" + node.args.kwarg.arg, annotation))

            return params

    raise ValueError(f"Function '{function_name}' not found in {script_path}")

def run_function(script_path, function_name, *args, **kwargs):
    """
    Dynamically imports a script and executes a function with the given arguments.
    Returns the function result.
    """
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Script not found: {script_path}")

    module_name = os.path.splitext(os.path.basename(script_path))[0]

    # Load the module dynamically
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get the function
    if not hasattr(module, function_name):
        raise ValueError(f"Function '{function_name}' not found in {script_path}")

    func = getattr(module, function_name)

    # Execute the function
    return func(*args, **kwargs)


example_script_path = list_paths_for_scripts()[0]
example_function = list_top_level_functions(example_script_path)[0]
print(run_function(example_script_path, example_function, 1, 2))