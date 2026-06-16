import shutil, os

skills_dir = r"C:\Users\rulur\hermes-config\skills"
copy_py = r"C:\Users\rulur\hermes-config\copy_skills.py"
manifest = r"C:\Users\rulur\hermes-config\SKILLS_MANIFEST.txt"

# Remove skills directory
if os.path.isdir(skills_dir):
    shutil.rmtree(skills_dir)
    print("Removed skills/")

# Remove helper files
for f in [copy_py, manifest]:
    if os.path.exists(f):
        os.remove(f)
        print(f"Removed {os.path.basename(f)}")

print("Done")
