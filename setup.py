from setuptools import setup


def read_requirements(file_path):
    dependencies = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.split("#")[0].strip()
                if line:
                    dependencies.append(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return dependencies


requirements_list = read_requirements("requirements.txt")
setup(
    name="Minecraft Server CLI",
    version="0.1.0",
    py_modules=["main"],
    install_requires=requirements_list,
    entry_points={
        "console_scripts": [
            "mcli = main:mcli",
        ],
    },
)
