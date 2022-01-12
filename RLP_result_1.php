<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style type="text/css">
			a{color: #c7d3de;text-decoration: none;}
			a:hover{color: #c7d3de;}
		</style>
	</head>
	<body >
		<div style="width: 1350px;margin: auto;background-color: white;">
			<div id="top">
				<div style="background-color: #1f4e79;margin: 0;height: auto;width: 1350px;">
					<table id="top" border="0" cellspacing="0" cellpadding="0" style="color: aliceblue;width: 1350px;">
						<tr style="color: #e5eaef;">
							<td style="font-size: 65px;text-align: left;width: 50%;color: white;"><b>&nbsp;DeepLRR</b></td>
							<td style="text-align: right;"></td>
						</tr>
						<tr><td style="height: 15px;"></td></tr>
					</table>
				</div>
				<div style="background-color: #1f4e79;margin: 0;height: 15px;width: 1350px;">
					<table border="0" cellspacing="" cellpadding="" style="width: 1000px;margin: auto;">
						<tr><td style="border-bottom: solid 4px #356b9b;"></td></tr>
					</table>
				</div>
				<div style="background-color: #1f4e79;margin: 0;height: 40px;width: 1350px;">
					<table border="0" cellspacing="0" cellpadding="0" style="width: 100%;color: aliceblue;text-align: center;">
						<tr style="font-size: x-large;height: 40px;">
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"><a href="index.html"><b>HOME</b></a></td>
							<td style="width: 12.5%;"><a href="DeepLRR.html"><b>DeepLRR</b></a></td>
							<td style="width: 12.5%;"><a href="NBS.html"><b>NBS-LRR</b></a></td>
							<td style="width: 12.5%;"><a href="RLK.html"><b>LRR-RLK</b></a></td>
							<td style="width: 12.5%;"><a href="RLP.html"><b>LRR-RLP</b></a></td>
							<td style="width: 12.5%;"><a href="CONTACT.html"><b>CONTACT</b></a></td>
							<td style="width: 12.5%;"></td>
						</tr>
					</table>
				</div>
				<div id="point" style="width: 1350px;height: 10px;">
					<table border="0" cellspacing="0" cellpadding="0" style="width: 1350px;text-align: center;">
						<tr>
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"><img src="img/point.png" width="10px" ></td>
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"></td>
						</tr>
					</table>
				</div>
			</div>
			
			<div id="main" style="width: 1350px;">
					<div id="分界线" style="width: 1000px;border-bottom: 2px solid #C7D3DE;height: 20px;margin: auto;"></div>
					<div style="width: 1000px;height: 640px;">
						<p style="margin:auto;"></p>
						<?php
							$num = rand(pow(10,10),pow(10,11));
							if(isset($_POST['STEP_1_Submit']))
							{
								$sequence=$_POST['sequence1'];
								if(!$sequence && $_FILES['Usrfile1']['size'] ==0 ){$sequence=">eg1
MLIFTIPQFFFAAWVMVVSLQMQGYISCIEKERKGLLELKAYVNKEYSYDWSNDTKSDCCRWERVECDRTSGRVIGLFLNQTFSDPILINLSLFHPFEELRTLNLYDFGCTGWFDDIHGYKSLGKLKKLEILDMGNNEVNNSVLPFLNAASSLRTLILHGNNMEGTFPMKELKDLSNLELLDLSGNLLNGPVPGLAVLHKLHALDLSDNTFSGSLGREGYKSFERLKNLEILDISENGVNNTVLPFINTASSLKTLILHGNNMEGTFPMKELINLRNLELLDLSKNQFVGPVPDLANFHNLQGLDMSDNKFSGSNKGLCQLKNLRELDLSQNKFTGQFPQCFDSLTQLQVLDISSNNFNGTVPSLIRNLDSVEYLALSDNEFKGFFSLELIANLSKLKVFKLSSRSNLLRLKKLSSLQPKFQLSVIELQNCNLENVPSFIQHQKDLHVINLSNNKLTGVFPYWLLEKYPNLRVLLLQNNSLTMLELPRLLNHTLQILDLSANNFDQRLPENIGKVLPNIRHLNLSNNGFQWILPSSFGEMKDIKFLDLSHNNFSGSLPMKFLIGCSSLHTLKLSYNKFFGQIFPKQTNFGSLVVLIANNNLFTGIADGLRNVQSLGVLDLSNNYLQGVIPSWFGGFFFAYLFLSNNLLEGTLPSTLFSKPTFKILDLSGNKFSGNLPSHFTGMDMSLLYLNDNEFSGTIPSTLIKDVLVLDLRNNKLSGTIPHFVKNEFILSLLLRGNTLTGHIPTDLCGLRSIRILDLANNRLKGSIPTCLNNVSFGRRLNYEVNGDKLPFEINDDEEFAVYSRLLVLPRQYSPDYTGVLMFNVEFASKSRYDSYTQESFNFMFGLDLSSNELSGDIPKELGDLQRIRALNLSHNSLSGLIPQSFSNLTDIESIDLSFNLLRGPIPQDLSKLDYMVVFNVSYNNLSGSIPSHGKFSTLDETNFIGNLLLCGSAINRSCDDNSTTEFLESDDQSGDEETTIDMEIFYWSLAATYGVTWITFIVFLCFDSPWRRVWFHFVDAFISLFKCV";}
								$title=$_POST['title1'];
								$modelname = $_POST['model'];
								setcookie("RLPstep", "1");
								if($_FILES['Usrfile1']['size'] > 0)
								{	
									if($_FILES['Usrfile1']['size'] > 10*1024*1024)
									{
										echo "over 10MB! <br>";	
									}
									elseif($sequence && $_FILES['Usrfile1'])
									{
										echo "only one! <br>";
									}else
									{
										$tmp_path=$_FILES['Usrfile1']['tmp_name'];
										$upload_path="/var/www/lifenglab/DeepLRR/Upfile/RLP_file/".$_FILES['Usrfile1']['name'];
										if(move_uploaded_file($tmp_path,$upload_path))
										{
											chmod($upload_path,0777);
                                                                                        $outname = $title."_$num".".out";
											unset($out);
                                                      		                   	exec("python /home/lifeng/DeepLRR/scripts/LRR_RLP_RLK.py {$_FILES['Usrfile1']['name']} {$outname} {$modelname} 2>&1 ",$out);
											//var_dump($out);
											setcookie("RLPfd","RLP_file");
											setcookie("RLPf","$outname");
											setcookie("title","$title");
                                                                          	  ?><?php
									  		header("refresh:0;url=RLP_file_result.php");
										  ?><?php

										}else
										{
								          	   echo "upfile failed";
										}
									}
								}else
								{
									$seq_file_path="/var/www/lifenglab/DeepLRR/Upfile/RLP_file/$title"."_$num".".fasta";
									$file=fopen($seq_file_path,"w+");
									fwrite($file,$sequence);
									fclose($file);
									chmod($seq_file_path,0777);
									
									$inputname = $title."_$num".".fasta";
									$outname = $title."_$num".".out";
									$out_path = "/var/www/lifenglab/DeepLRR/Upfile/RLP_file/$outname";
                                                                        exec("python /home/lifeng/DeepLRR/scripts/LRR_RLP_RLK.py {$inputname} {$outname} {$modelname} 2>&1  ",$out);
									//for($i=0;$i < count($out);$i++){echo "$out[$i]<br>";}
									setcookie("RLPs","$out_path");
									?><?php
										header("refresh:0;url=RLP_seq_result.php");
									?><?php

								}
							}elseif(isset($_POST['STEP_2_Submit']))
							{
								$sequence=$_POST['sequence2'];
								if(!$sequence && $_FILES['Usrfile2']['size'] ==0 ){$sequence=">eg2
MGTTTNLRSWLYLILLFIVVVGVNAQNRRPKNVQVAVKAKWQGTPLLLEAGELISKESKQLFWEFTDAWLGSDGDDSDCKSARDCLLKISKQASTLLAQPVASLFHFSLTLRSASPRLVLYRQLADESLSSFPHGDDPSATGCCWVDTGSSLFYDVADLQSWLASAPAVGDAVQGPELFDFDHVHFDSRAGSPVAVLYGAVGTDCFRKFHLSLAKAAKEGKVTYVVRPVLPLGCEGKTRPCGAIGARDNVSLAGYGVELALKNMEYKAMDDSAIKKGITLEDPRTEDLSQDVRGFIFSKILDRKPELRSEVMAFRDYLLSSTVSDTLDVWELKDLGHQTAQRIVHASDPLQSMQEINQNFPSVVSSLSRMKLNESIKDEILSNQRMVPPGKALLALNGALLNIEDIDLYMLMDLAHQELSLANHFSKLKIPDGAIRKLLLTTPLPEPDSYRVDFRSVHVTYLNNLEEDDMYKRWRSNINEILMPAFPGQLRYIRKNLFHAVYVIDPATACGLESIETLRSLYENQLPVRFGVILYSTQLIKTIENNGGQIPSSDAVTNAQVKEDLSTMVIRLFLYIKEHHGIQTAFQFLGNLNTLRTESADSSEADIEQEHVDGAFVETILPKVKTLPQDILLKLRQEHTLKEASEASSMFVFKLGLAKLKCSFLMNGLVFDSVEEETLLNAMNEELPKIQEQVYYGQIESHTKVLDKLLSESGLSRYNPQIISGGKNKPRFVSLASSTRKGESMLNDVNYLHSPETSEDVKYVTHLLAADVATKKGMKLLHEGVRYLIGGSKSARLGVLFSSSQNADPHSLLFIKFFEKTASSFSHKEKVLYFLDKLCLFYEREYLLKTSVESASSQMFIDKVLELADEYGLSSKAYRSCLVESVDEELLKRLTKVAQFLSWELGLESDANAIISNGRVIFPVDERTFLGQDLHLLESMEFNQRVKPVQEIIEGIEWQDVDPDLLTSKYFSDVFMFVSSAMATRDRSSESARFEVLNSEYSAVLLGNENATIHIDAVIDPLSPTGQKLASLLQVLQKHVQTSMRIVLNPMSSLVDIPLKNYYRYVLPNTDDYSSTGFDVDGPKAFFANMPLSKTLTMNLDVPEPWLVEPVIAIHDLDNILLENLGDTTTLQAVFEVESLVLTGHCAEKDHEAPRGLQLILGTKNRPHLVDTLVMANLGYWQMKVSPGVWYLQLAPGRSSELYALKGGNDGSQDQSSLKRITIDDLRGKVVHLEVVKRKGKEHEKLLVPSDGDDAVQQNKEGSWNSNFLKWASGFVGGRQQSMKGGPDKEHEKGGRQGKTINIFSIASGHLYERFLKIMILSVLKNTNRPVKFWFIKNYLSPQFKDVIPHMAQEYNFEYELITYKWPSWLHKQKEKQRIIWAYKILFLDVIFPLSLEKVIFVDADQIIRTDMGELYDMDIKGRPLAYTPFCDNNREMDGYKFWKQGFWKEHLRGRPYHISALYVVDLVKFRETAAGDNLRVFYETLSKDPNSLSNLDQDLPNYAQHTVPIFSLPQEWLWCESWCGNATKAKARTIDLCNNPMTKEPKLQGARRIVTEWPDLDLEARKFTAKILGEDVELNEPVAAPATDKPNPLPSNDISEDTEQDLESKAEL";}
								$title=$_POST['title2'];
								setcookie("RLPstep", "2");
								if($_FILES['Usrfile2']['size'] > 0)
								{
									if($_FILES['Usrfile2']['size'] > 10*1024*1024)
									{
										echo "over 10MB <br>";
										
									}
									elseif($sequence && $_FILES['Usrfile2'])
									{
										echo "only one <br>";
										
									}else
									{
										$tmp_path=$_FILES['Usrfile2']['tmp_name'];
										$upload_path="/var/www/lifenglab/DeepLRR/Upfile/atypia/".$_FILES['Usrfile2']['name'];
										if(move_uploaded_file($tmp_path,$upload_path))
										{
											chmod($upload_path,0777);
                                                                                        $outname = $title."_$num".".out";
											unset($out);
											$type = "LRR_RLP";
                                                                            		exec("python /home/lifeng/DeepLRR/scripts/atypia.py {$_FILES['Usrfile2']['name']} {$outname} {$type}",$out);
											setcookie("RLPfd","atypia");
											setcookie("RLPf","$outname");
											setcookie("title","$title");
                                                                            	    ?><?php
											header("refresh:0;url=RLP_file_result.php");
											?><?php
									
										}else
										{
								           echo "upfile failed";
										   
										}
									}
								}else
								{
									$seq_file_path="/var/www/lifenglab/DeepLRR/Upfile/atypia/$title"."_$num".".fasta";
									$file=fopen($seq_file_path,"w+");
									fwrite($file,$sequence);
									fclose($file);
									chmod($seq_file_path,0777);
									$inputname = $title."_$num".".fasta";
									$outname = $title."_$num".".out";
									$out_path = "/var/www/lifenglab/DeepLRR/Upfile/atypia/$outname";
									$type = "LRR_RLP";
									unset($out);
                                                                        exec("python /home/lifeng/DeepLRR/scripts/atypia.py {$inputname} {$outname} {$type} 2>&1 ",$out);
                                                                        setcookie("RLPs","$out_path");
									//var_dump($out);
								    ?><?php
                                                                        header("refresh:0;url=RLP_seq_result.php");
								    ?><?php

								}
							}else
							{

							}
						?>
						
					</div>
			</div>
			
			<div id="bottom" style="float: left;width: 1350PX;height: 50px;">
				<div id="分界线" style="width: 1000px;border-bottom: 2px solid #C7D3DE;height: 20px;margin: auto;"></div>
				<div id="" style="width: 1350px;background-color:#1f4e79 ; margin: auto;text-align: center;height: 50px;">
					<p style="color: #FFFFFF;line-height: 50px;font-size: small;">Key Laboratory of Horticultural Plant Biology, Huazhong Agricultural University of China, Hubei, Wuhan 430070,China.</p>
				</div>
			</div>
		</div>
	</body>
</html>
