import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        working_directory = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(working_directory, file_path))
        
        if not path.startswith(working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(path):
            return f'Error: File "{file_path}" not found.'
        
        if not path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        temp = subprocess.run(["python3", f"{path}"], timeout=30, text=True, capture_output=True,
                                cwd=working_directory)
        if len(temp.stdout) == 0 and len(temp.stderr) == 0 and temp.returncode == 0:
            return "No output produced."
        
        result = ""
        if len(temp.stdout) > 0:
            result += f"STDOUT:{temp.stdout}\n"
        if len(temp.stderr) > 0:
            result += f"STDERR:{temp.stderr}\n"
        if temp.returncode != 0:
            result += f"Process exited with code {temp.returncode}\n"

        return result

    except Exception as e:
        return f"Error: executing Python file: {e}"