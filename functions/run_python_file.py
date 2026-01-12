import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(abs_working_dir, file_path))

        if not target_file.startswith(abs_working_dir):
            return f'error: cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'"{file_path}" is not a python file'

        command = ["python", target_file]

        command_run = subprocess.run(
            command, capture_output=True, text=True, timeout=30
        )

        output = command_run.stdout

        if command_run.check_returncode:
            output += f"\n process exited with code {str(command_run.returncode)}"

        if command_run.stdout is None or command_run.stderr is None:
            output += "\n no output produced"

        if command_run.stdout:
            output += f"\n stdout: {command_run.stdout} "

        if command_run.stderr:
            output += f"\n stderr: {command_run.stderr}"

        return output

    except Exception as e:
        return f"error: executing python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a single specific python file which absolute path would be given by the user",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="File directory where the supposed python file should be found, default should be the current directory",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Nmae of the python file to run, must end in '.py'",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Arguments provided but are optional and not required",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="String content inside the argument if they are provided",
                ),
            ),
        },
    ),
)
