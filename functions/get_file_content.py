import os

def get_file_content(working_directory, file_path):
    try:
        working_directory = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(working_directory, file_path))
        
        if not path.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        MAX_CHARS = 10001

        file_content_string = ""
        with open(path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string = file_content_string[:-1]
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string

    except Exception as e:
        return f"Error: {e}"
