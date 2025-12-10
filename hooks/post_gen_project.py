import os
import shutil

def remove(path):
    if os.path.exists(path):
        shutil.rmtree(path)

PROJECT_DIR = os.getcwd()
include_minio = "{{cookiecutter.include_minio}}"
include_postgres = "{{cookiecutter.include_postgres}}"

if include_minio != "yes":
    remove(os.path.join(PROJECT_DIR, "minio"))

if include_postgres != "yes":
    remove(os.path.join(PROJECT_DIR, "postgres"))