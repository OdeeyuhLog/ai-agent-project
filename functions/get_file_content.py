from os import path

from google.genai import types

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        abs_file_path = path.abspath(working_directory)
        target_file = path.normpath(path.join(abs_file_path, file_path))

        if not target_file.startswith(abs_file_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'

        if not path.isfile(target_file):
            return f'Error: File not found is not a regular file: "{file_path}'

        file = open(target_file)
        file_contents = file.read(MAX_CHARS)

        if file.read(1001):
            file_contents += (
                f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            )

        return file_contents

    except Exception as e:
        return f"Error: {str(e)}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Output all the contents inside a given file combined with the given absolute path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Name of the file that will be outputted by the function",
            ),
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
