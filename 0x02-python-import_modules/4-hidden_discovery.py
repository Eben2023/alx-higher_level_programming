#!/usr/bin/env python3
import importlib.util
def get_names(module_name):
    spec = importlib.util.spec_from_file_location(module_name, module_name + ".pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return [name for name in dir(module) if not name.startswith("__")]
if __name__ == "__main__":
    names = get_names("hidden_4")
    names.sort()
    for name in names:
        print(name)
