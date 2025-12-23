import os
import subprocess

DATASETS = {
    "asl_alphabet": "grassknoted/asl-alphabet",
    # Add more datasets here:
    # "bsl_alphabet": "username/bsl-alphabet",
}

os.makedirs("data", exist_ok=True)

for folder_name, kaggle_id in DATASETS.items():
    target_dir = os.path.join("data", folder_name)

    if os.path.exists(target_dir):
        print(f"{folder_name} already exists, skipping download.")
        continue 

    os.makedirs(target_dir, exist_ok=True)

    print(f"Downloading {folder_name}...")

    subprocess.run(
        [
            "kaggle", "datasets", "download",
            "-d", kaggle_id,
            "-p", target_dir,
            "--unzip"
        ],
        check=True
    )

print("All datasets are ready.")