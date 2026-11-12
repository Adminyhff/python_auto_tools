import os


def hunt_for_passwords(target_dir):
    print(f"[*] Starting hunt in: {target_dir}")

    # os.walk automatically goes through every folder and subfolder
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            # we only care about text or log files
            if file.endswith(".txt") or file.endswith(".log"):
                file_path = os.path.join(root, file)
                # open the file and read it safely
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line in f:
                            if "password" in line.lower():
                                print(f"[+] Found potential credential in {file_path}:")
                                print(f"   ->{line.strip()}")

                except Exception as e:
                    # Ingnore files that we don't have permission to read
                    pass


if __name__ == "__main__":
    # Create a test directory and some dummy files first！
    # Run it on your currrent directory "." for testing
    hunt_for_passwords(".")
