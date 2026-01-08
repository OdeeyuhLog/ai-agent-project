# functions/get_files_info.py
import os

from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        working_abs_path = os.path.abspath(working_directory)
        target_dir = os.path.abspath(os.path.join(working_directory, directory))

        if not target_dir.startswith(working_abs_path):
            return f"Error: Cannot list {directory} as it is outside the directory"

        if not os.path.isdir(target_dir):
            return Exception(f"{directory} is not a directory")

        file_tree_str_list = [
            f"Result for '{'current' if directory == '.' else directory} directory'"
        ]
        for file in os.listdir(target_dir):
            filepath = os.path.join(target_dir, file)
            valid_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            file_tree_str_list.append(
                f"- {str(file)}: file_size={file_size} bytes, is_dir={valid_dir}"
            )

        return "\n".join(file_tree_str_list)

    except Exception as e:
        return f"Error: {str(e)}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="List files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            )
        },
    ),
)
