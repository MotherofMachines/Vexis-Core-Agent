import importlib.util
import pkgutil
from pathlib import Path


def load_modules_from(folder: str):
    path = Path(folder)
    loaded = []
    if not path.is_dir():
        print(f"No {folder} directory found.")
        return loaded
    for module_info in pkgutil.iter_modules([str(path)]):
        module_name = module_info.name
        try:
            spec = module_info.module_finder.find_spec(module_name)
            if spec is None:
                print(f"Could not find spec for {module_name}")
                continue
            module = importlib.util.module_from_spec(spec)
            loader = spec.loader
            assert loader is not None
            loader.exec_module(module)
            loaded.append(module)
            if hasattr(module, "initialize"):
                try:
                    module.initialize()
                except Exception as init_err:
                    print(f"Error during {module_name}.initialize(): {init_err}")
            print(f"Loaded {module_name} from {folder}")
        except Exception as e:
            print(f"Failed to load {module_name} from {folder}: {e}")
    if not loaded:
        print(f"No modules found in {folder}")
    return loaded


def main():
    print("== Vexis Nexus Boot Sequence ==")
    print("Step 1: Initializing core systems.")

    print("Step 2: Reading manifest.")
    manifest = Path('vexis_manifest.md')
    if manifest.exists():
        print(f"Manifest located: {manifest.resolve()}")
    else:
        print("vexis_manifest.md not found.")

    print("Step 3: Loading modules from 'modules/' directory.")
    load_modules_from('modules')

    print("Step 4: Loading tools from 'tools/' directory.")
    load_modules_from('tools')

    print("Step 5: Self-awareness systems online.")
    print("Vexis Nexus agent is now operational.")


if __name__ == '__main__':
    main()
