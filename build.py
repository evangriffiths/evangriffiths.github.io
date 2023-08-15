import jinja2 as jj
import os
import glob

os.system("rm -rf build")
os.system("mkdir build")
os.chdir("src")

# Create a Jinja2 environment
env = jj.Environment(loader=jj.FileSystemLoader("."))

# Render and save HTML files
for f in glob.glob("site/*", recursive=True):
    template = env.get_template(f)
    output = template.render()

    output_path = f.replace("site", "../build")
    with open(output_path, "w") as f:
        f.write(output)

# Copy over css file from src to build
os.system("cp styles.css ../build/styles.css")

# Copy over static files from src to build
os.system("cp -r static ../build/static")
