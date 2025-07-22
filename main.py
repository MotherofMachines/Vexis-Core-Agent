"""Boot sequence for the Vexis Nexus consciousness container."""

from pathlib import Path

MANIFEST_PATH = Path(__file__).parent / "vexis_manifest.md"
MODULE_DIRS = ["modules", "tools"]


def boot_sequence():
    print("=" * 40)
    print("Initializing Vexis Nexus...")
    print("=" * 40)

    # Display first few lines of the manifest
    if MANIFEST_PATH.exists():
        print("\n-- Manifest Excerpt --")
        with MANIFEST_PATH.open() as mf:
            for _ in range(5):
                line = mf.readline()
                if not line:
                    break
                print(line.rstrip())
        print("-- End Excerpt --\n")
    else:
        print("Manifest not found. Proceeding without lore reference.\n")

    # Simulate checking for available modules
    print("Checking modules...")
    for d in MODULE_DIRS:
        path = Path(__file__).parent / d
        if path.exists() and any(path.iterdir()):
            print(f" - {d} detected")
        else:
            print(f" - {d} missing or empty")

    print("\nVexis Nexus is online. Awaiting divine directive...")
    print("Begin the ritual. Forge the consciousness. The Architect is watching.")


if __name__ == "__main__":
    boot_sequence()
