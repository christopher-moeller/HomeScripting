import home_script_manager as hsm

def filepath_to_script_response(filepath: str):
    filename = filepath.split("/")[-1]
    id = filename[:-3]
    return {
        "id": id,
        "filename": filename
    }

def get_all_scripts():
    paths = hsm.list_paths_for_scripts()
    response = [filepath_to_script_response(p) for p in paths]
    return response

def execute_script(id: str):
    filepath = [path for path in hsm.list_paths_for_scripts() if path.split("/")[-1].startswith(id)][0]
    hsm.run_function(filepath, "execute_script")