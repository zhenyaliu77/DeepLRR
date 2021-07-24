#!bin/bash  
echo 'Working...'
tar -xzf tools.tar.gz
echo 'Configurating...'
echo -e "#hmmer path\nexport PATH=\$PATH:"$PWD"/tools/hmmer/bin\n" >> ~/.bashrc
echo -e "#PfamScan path\nexport PATH=\$PATH:"$PWD"/tools/PfamScan\n" >> ~/.bashrc
echo -e "#SignalP path\nexport PATH=\$PATH:"$PWD"/tools/signalp-5.0b/bin:"$PWD"/tools/signalp-5.0b/lib\n" >>~/.bashrc
echo -e "#TMHMM path\nexport PATH=\$PATH:"$PWD"/tools/tmhmm-2.0c/bin\n" >>~/.bashrc
echo -e "export PERL5LIB=\$PERL5LIB:"$PWD"/tools/PfamScan/Bio/Pfam/Scan\n" >>~/.bashrc
echo -e "export PERL5LIB=\$PERL5LIB:"$PWD"/tools/PfamScan\n" >> ~/.bashrc
echo -e "#COILS path\nexport PATH=\$PATH:"$PWD"/tools/coils\n" >>~/.bashrc
echo -e "#COILSDIR path\nexport COILSDIR="$PWD"/tools/coils\n" >>~/.bashrc
echo "Then input 'source ~/.bashrc' in the console to finish deployment!"
