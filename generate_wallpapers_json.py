import os
import json

# Configuration
OUTPUT_FILE = "wallpapers.json"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

def is_valid_folder(folder_name: str) -> bool:
    """Ignore hidden/system folders."""
    return (
        os.path.isdir(folder_name)
        and not folder_name.startswith(".")
    )

def get_image_files(folder_path: str) -> list[str]:
    """Return sorted list of image filenames inside a folder."""
    images = []
    for file in os.listdir(folder_path):
        _, ext = os.path.splitext(file.lower())
        if ext in IMAGE_EXTENSIONS:
            images.append(file)
    return sorted(images)

def generate_wallpaper_json() -> None:
    data = {}

    for item in sorted(os.listdir(".")):
        if is_valid_folder(item):
            images = get_image_files(item)
            if images:  # include folder only if it has images
                data[item] = images

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"cGenerated {OUTPUT_FILE} with {len(data)} categories.")

if __name__ == "__main__":
    generate_wallpaper_json()
