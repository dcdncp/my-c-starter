# C Project Template

This is a simple template for C projects. It includes a basic structure for organizing your source code, headers, and build files.

## Project Structure

```
├── build/
│   ├── objects/
│   └── target/
├── include/
│   └── add.h
├── scripts/
│   ├── config.py
│   ├── maketools.py
│   └── prepare.py
├── src/
│   ├── adder/
│   │   └── add.c
│   ├── compile_flags.txt
│   └── main.c
├── .gitignore
├── README.md
```

## Build Instructions

1. Ensure you have Python installed.
2. Run the `prepare.py` script to generate the Makefile:
   ```sh
   python scripts/prepare.py
   ```
3. Use `make` to build the project:
   ```sh
   make
   ```

## Files

- include: Directory for header files.
- src: Directory for source files.
- scripts: Directory for build scripts.
- build: Directory for build output.

## Example

The template includes a simple example with an `add` function:

- add.h: Header file for the `add` function.
- add.c: Implementation of the `add` function.
- main.c: Example usage of the `add` function.

## License

This project is licensed under the MIT License.
