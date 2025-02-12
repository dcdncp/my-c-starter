TARGET = "app.exe"

INCLUDE_DIRS = ["include"]
SRC_DIRS = ["src"]

TARGET_DIR = "build/target"
OBJECTS_DIR = "build/objects"

CC = "clang", "-std=c11"
CFLAGS = "-Wall", *[f"-I{d}" for d in INCLUDE_DIRS]
LDFLAGS = ()

