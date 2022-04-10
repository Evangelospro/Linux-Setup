#!/usr/bin/python3
packages = open('packages.txt', 'r')
for package in packages.readlines():
    package_name = package.split('/')[0]
    response = input(f"Do you want to install {package_name} (y/n)")
    if response == 'y':
        print(f"Installing {package_name}...")
        os.system('pacman -Sy ' + package)
    else:
        print(f"Skipping {package_name}...")