import subprocess

def build_frontend():
    subprocess.run(["npm", "run", "build"], cwd="../frontend")