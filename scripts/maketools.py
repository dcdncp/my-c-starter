from os import path

context = None
rules = []

class Rule():
    def __init__(self, output, *input):
        global rules
        self.input = input
        self.output = output
        self.commands = [] 
    
    def __enter__(self):
        global context
        context = self
        return self
    
    def __exit__(self, type, value, traceback):
        global context
        rules.append(self)
        context = None

def build(output, *input):
    return Rule(output, *input)

def run(*args):
    global context
    if context is not None:
        context.commands.append(args)

def make(path="Makefile"):
    with open(path, "w") as f:
        for rule in reversed(rules):
            in_ = " ".join(rule.input)
            f.write(f"{rule.output}: {in_}\n")
            for command in rule.commands:
                cmd = " ".join(command)
                f.write(f"\t{cmd}\n")

def extract_headers_files(src_files, include_dirs=[]):
    headers = []
    for src in src_files:
        with open(src, "r") as f:
            for rawLine in f:
                line = rawLine.strip()
                if line.startswith("#include"):
                    header = line.split(" ")[1].strip().replace("\"", "").replace("<", "").replace(">", "")
                    if header not in headers:
                        headers.append(header)
    header_paths = [path.normpath(path.join(path.dirname(src), header)).replace("\\", "/") for header in headers]
    paths = []
    for header, header_path in zip(headers, header_paths):
        if path.exists(header_path):
           paths.append(header_path) 
        else:
            for include_dir in include_dirs:
                maybe_header = path.join(include_dir, header)
                if path.exists(maybe_header):
                    paths.append(path.normpath(maybe_header).replace("\\", "/"))
                    break
    return paths