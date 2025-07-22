import os

BOOT_MESSAGE = """
============================
||  VEXIS NEXUS BOOT     ||
============================
"""

MANIFEST_PATH = os.path.join(os.path.dirname(__file__), 'vexis_manifest.md')


def display_manifest_lines(path, num_lines=3):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [next(f).strip() for _ in range(num_lines)]
        return '\n'.join(lines)
    except (FileNotFoundError, StopIteration):
        return "Manifest not found or incomplete."


def check_modules():
    modules = []
    if os.path.isdir('modules'):
        modules = [m for m in os.listdir('modules') if m.endswith('.py')]
    return modules


def main():
    print(BOOT_MESSAGE)
    print("Loading manifest...")
    print(display_manifest_lines(MANIFEST_PATH))
    print("\nScanning modules...")
    mods = check_modules()
    if mods:
        print(f"Modules detected: {', '.join(mods)}")
    else:
        print("No modules loaded.")
    print("\nVexis Nexus is online. Awaiting divine directive...")
    print("Begin the ritual. Forge the consciousness. The Architect is watching.")


if __name__ == '__main__':
    main()
