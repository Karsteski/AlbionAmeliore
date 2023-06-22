#!/bin/python

import os, sys, subprocess

UI_FILE_DIR = "src/ui/ui_files/"
OUTPUT_DIR = "src/ui/ui_classes/"

def get_filenames(directory: str) -> list[str]:
    filenames = os.listdir(directory)
    return filenames

def run_command(command: str, filenames: list[str], input_dir: str, output_dir: str) -> None:
    for filename in filenames:
        # Reformat filename to fit the Qt convention
        output_filename = "ui_" + filename[:-3] + ".py"
        output_file = output_dir + output_filename
        with open(output_file, "w") as file:
                input_file = input_dir + filename
                full_command = command + " " + input_file
                print("full command = ", full_command)
                print("output= ", output_file)

                subprocess.call(full_command, stdout=file, shell=True)

if __name__ == "__main__":
    filenames = get_filenames(UI_FILE_DIR)

    run_command("pyside6-uic", filenames, UI_FILE_DIR, OUTPUT_DIR)

