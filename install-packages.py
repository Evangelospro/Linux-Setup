#!/usr/bin/python3
import os
packages = open('packages.txt', 'r')
for package_name in packages.readlines():
    response = input(f"Do you want to install {package_name} (y/n)")
    if response == 'y':
        print(f"Installing {package_name}...")
        os.system('yay -Sy ' + package_name)
    else:
        print(f"Skipping {package_name}...")
