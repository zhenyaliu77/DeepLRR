DeepLRR version 1.01 by Zhenya Liu (zhenyaliu77@gmail.com)

Usage:
run "python DeepLRR.py *.fasta Lscp Ldcp Lncp"
*.fasta      query input files are FASTA .fasta(default)
Lscp <int>   Leucine-rich repeat score control parameter are in [1,11] 4(recommend)
Ldcp <int>   Leucine-rich repeat distance control parameter are in [1,¡Þ] 9(recommend)
Lncp <int>   Leucine-rich repeat number control parameter are in [2,¡Þ] 3(recommend)
-h           print this usage message


tips:
1>	output files in ./DeepLRR-1.01/outcome
2>	./DeepLRR-1.01/demo/Q96FE5.fasta could be used to test DeepLRR
3>	If your Python not install torch module,copy torch directory(./DeepLRR-1.01/torch) into ./Python3/Lib/site-packages
4>	run "python predToscatter.py ./DeepLRR-1.01/demo/Q96FE5.fasta ./DeepLRR-1.01/outcome/Q96FE5_predict2.txt"
	you will get a scatter plot about the Q96FE5_predict2.txt