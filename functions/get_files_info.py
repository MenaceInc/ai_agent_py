import os

def get_files_info(working_directory, directory=None):
    try:
        working_directory = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(working_directory, directory))
        
        if not path.startswith(working_directory):
            return f'\tError: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(path):
            return f'\tError: "{directory}" is not a directory'
        
        # - README.md: file_size=1032 bytes, is_dir=False
        # - src: file_size=128 bytes, is_dir=True
        # - package.json: file_size=1234 bytes, is_dir=False

        contents = os.listdir(path)
        result = []
        for item in contents:
            filepath = os.path.join(path, item)
            size = os.path.getsize(filepath)
            is_dir = not os.path.isfile(filepath)
            result.append(f" - {item}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(result)
    except Exception as e:
        return f"\tError: {e}"
