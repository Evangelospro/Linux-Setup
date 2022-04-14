!#/bin/bash
git clone https://github.com/Evangelospro/ZSHRC/
cd ZSHRC
./setup.sh
./install-packages.sh
cd ..
git clone https://github.com/material-shell/material-shell
cd material-shell
make install
