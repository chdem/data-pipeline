import os
import shutil

def rename(path, new_path):
    if os.path.exists(path):
        os.rename(path, new_path)

def remove(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)

PROJECT_DIR = os.getcwd()
include_minio = "{{cookiecutter.include_minio}}"
include_postgres = "{{cookiecutter.include_postgres}}"

if include_minio != "yes":
    remove(os.path.join(PROJECT_DIR, "src/minio"))

if include_postgres != "yes":
    remove(os.path.join(PROJECT_DIR, "src/postgres"))

#remove les machins inutiles une fois le projet généré
remove(os.path.join(PROJECT_DIR, "docker")) # TODO à mettre juste à la racine du cookiecutter ??

#on renomme le GENERATE_README en README.md
rename(os.path.join(PROJECT_DIR, ".env.exemple"), os.path.join(PROJECT_DIR, ".env"))