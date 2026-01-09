import os

from google.genai import types


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
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {str(e)}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Creates a file and writes the provided content inside it, if the same file name already exists, it overwrites it instead with the new content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="File directory where the supposed file should be found, default should be the current directory",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Name of the file to create or overwrite if existing already.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="This is the string content to write inside the pointed file",
            ),
        },
    ),
)
