from glob import glob
from os import makedirs, path
from maketools import make, build, run, extract_headers_files
import config as cfg

def compile_object(output, input):
    run(*cfg.CC, *cfg.CFLAGS, "-c", input, "-o", output)

def link_objects(output, *inputs):
    run(*cfg.CC, *cfg.LDFLAGS, "-o", output, *inputs)    

print("Building Makefile\n")

# Target
print("Target:         ", cfg.TARGET)
print()

# Print info about compilation
print("Compiler:       ", " ".join(cfg.CC))
print("Compiler flags: ", " ".join(cfg.CFLAGS))
print("Linker flags:   ", " ".join(cfg.LDFLAGS))
print()

if not path.exists(cfg.TARGET_DIR):
    print(f"Creating target directory: {cfg.TARGET_DIR}")
    makedirs(cfg.TARGET_DIR)
    print()

if not path.exists(cfg.OBJECTS_DIR):
    print(f"Creating objects directory: {cfg.OBJECTS_DIR}")
    makedirs(cfg.OBJECTS_DIR)
    print()

# Get all source files
src_files = []

for f in cfg.SRC_DIRS:
    src_files += [p.replace(path.sep, "/") for p in glob(path.join(f, "**/*.c"), recursive=True)]


if len(src_files) > 0:
    print("Source files:")
    for f in src_files:
        print(f"  - {f}")
    print()
else:
    print("No source files found")
    exit(0)

obj_files = []
for f in src_files:
    base_dir = f.split("/")[0]
    obj = path.join(cfg.OBJECTS_DIR, f.replace(".c", ".o", 1).replace(base_dir+"/", "").replace("/", ".")).replace("\\", "/")
    obj_files.append(obj)
    
print("Object files:")
for f in obj_files:
    print(f"  - {f}")
print()

for src, obj in zip(src_files, obj_files):
    headers = extract_headers_files(src_files, cfg.INCLUDE_DIRS)
    with build(obj, src, *headers):
        compile_object(obj, src)

target = path.normpath(path.join(cfg.TARGET_DIR, cfg.TARGET)).replace("\\", "/")

print("Linking target:")
print(f"  - {target}")
print()

with build(target, *obj_files):
    link_objects(target, *obj_files)

print("Makefile built successfully")

make()
