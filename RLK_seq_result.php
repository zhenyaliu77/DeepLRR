<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>LRR-RLP Result</title>
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
					<div id="list" style="heigh:auto !important;hieght:600px;min-height:600px;">
						<table border="0" cellspacing="8" cellpadding="0" style="width: 910px;margin: auto;">
							<br>
						<?php
							$file_path = $_COOKIE['RLKs'];
							$fp = fopen("$file_path",'r');
							$step = $_COOKIE['RLKstep'];
							if(file_exists("$file_path"))
							{
								$fileCont = file_get_contents($file_path);
                                                                $lines = substr_count($fileCont, "\n");
                                                                if($lines > 1)
							    {	
								$ctrl = 0;
								$cont = fgets($fp);
							?>
							<tr style="height: 20px;background-color: #8497b0;text-align: center;color: aliceblue;">
                                                                <td>Protein ID</td>
                                                                <td>Length</td>
                                                                <td>Start</td>
                                                                <td>End</td>
                                                                <td >Domain</td>
                                                                
                                                                <td>Source</td>
                                                        </tr>

                                                        <?php

								while(!feof($fp))
								{
									$cont = fgets($fp);
									if(feof($fp)){break;}
									$cont = str_replace('\n','',$cont);
									$arr = explode('	',$cont);
								?>
									<tr style="height: 20px;background-color: #e7e6e6;text-align: center;">
										<td><?php echo $arr[0];?></td>
                                                                		<td><?php echo $arr[1];?></td>
                                                                		<td><?php echo $arr[2];?></td>
                                                                		<td><?php echo $arr[3];?></td>
                                                                		<td><?php echo $arr[4];?></td>
                                                                
                                                                		<td><?php echo $arr[5];?></td>
									</tr>
								<?php

								}
							
							fclose($fp);
							unset($fp);
							unlink($file_path);
							}else{$ctrl = 1;}
						}else{$ctrl = 1;}
					if($ctrl){
						if($step == "1"){
						?>
	<p style="margin: auto;text-align:center;font-size:200%;">No LRR-RLK<br><br>If refreshed, please resubmit</p>
						<?php
						}else if($step == "2"){
						?>
	<p style="margin: auto;text-align:center;font-size:200%;">No Atypical domains<br><br>If refreshed, please resubmit</p>
						<?php						
						}
					}
							?>
						</table>
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
