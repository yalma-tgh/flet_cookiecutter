import os
import subprocess
import sys

# Get the current working directory (where the project has been generated)
project_dir = os.path.abspath(os.path.curdir)

# Define the virtual environment folder name
venv_dir = os.path.join(project_dir, 'venv')

def create_virtualenv():
    """Create and activate a virtual environment, and install dependencies."""
    try:
        # Create a virtual environment
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])

        # Determine the platform-specific path to the activate script
        if os.name == 'nt':
            activate_script = os.path.join(venv_dir, 'Scripts', 'activate')
        else:
            activate_script = os.path.join(venv_dir, 'bin', 'activate')

        # Install requirements in the virtual environment
        print("Installing dependencies...")
        subprocess.check_call([os.path.join(venv_dir, 'bin', 'pip'), "install", "-r", "requirements.txt"])

        print("\nVirtual environment setup complete!")
        print(f"To activate it, run:\n\n  source {activate_script}\n")

    except subprocess.CalledProcessError as error:
        print(f"Error during setup: {error}")
        sys.exit(1)

if __name__ == "__main__":
    create_virtualenv()
