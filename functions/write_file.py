import os


def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(working_directory, file_path))

        if not target_file.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the working directory'

        if os.path.isdir(target_file):
            f'Error: Cannot write to "{file_path}" as it is a directory '
        
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote tp "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {str(e)}"
