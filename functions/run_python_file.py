import subprocess
import os


def run_python_file(working_directory, file_path, args=None):
       try:
           abs_working_dir = os.path.abspath(working_directory)
           target_file = os.path.abspath(os.path.join(abs_working_dir, file_path))

           if not target_file.startswith(abs_working_dir):
               return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

           if not os.path.isfile(target_file):
               return f'Error: "{file_path}" does not exist or is not a regular file'

           if not file_path.endswith('.py'):
               return f'"{file_path}" is not a Python file'

           command = ["python", target_file]

           command_run = subprocess.run(command, capture_output=True, text=True, timeout=30)

           output = command_run.stdout

           if command_run.check_returncode:
               output += f"\n Process exited with code {str(command_run.returncode)}"

           if command_run.stdout is None or command_run.stderr is None:
               output += "\n No output produced"

           if command_run.stdout:
               output += f"\n STDOUT: {command_run.stdout} "

           if command_run.stderr:
               output += f"\n STDERR: {command_run.stderr}"

           return output
        
       except Exception as e:
           return f"Error: executing Python file: {e}"

