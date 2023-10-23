from zip_read_yaml import read_yaml_zip
from pathlib import Path

current_dir = Path(__file__).absolute().parent
zip_dir = current_dir.joinpath('zip_folders')
read_yaml_zip(zip_dir, "test.yaml", "new_test.yaml")