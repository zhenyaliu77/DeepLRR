<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>DeepLRR-Result</title>
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
							<td style="width: 12.5%;"><img src="img/point.png" width="10px" ></td>
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"></td>
							<td style="width: 12.5%;"></td>
						</tr>
					</table>
				</div>
			</div>
			
			<div id="main" style="width: 1350px;">
					<div id="分界线" style="width: 1000px;border-bottom: 2px solid #C7D3DE;height: 20px;margin: auto;"></div>
					<div id="list" style="height:auto !important;height:600px;min-height:600px;">
					<code><table border="0" cellspacing="8" cellpadding="0" style="width: 1000px;margin: auto;font-size:130%;">
							<tr style="height: 20px;background-color: #8497b0;text-align: center;color: aliceblue;">
							<?php
								$title = $_COOKIE['DeepLRR'];
								$title_num = $_COOKIE['img'];
								$file = $_COOKIE['img']."_predict2.txt";
								$img = "./img/DeepLRR/$title_num.png";
								chmod($img,0777);
								
								$file_path = "/var/www/lifenglab/DeepLRR/DeepLRR-1.01/outcome/$file";
								$fp = fopen("$file_path",'r');
								if(file_exists("$file_path"))
								{	
									$fileCont = file_get_contents($file_path);
									$lines = substr_count($fileCont, "\n");
									if($lines > 1){
									$cont = fgets($fp);
									$cont = str_replace('\n','',$cont);
                                                                        $arr = explode('	',$cont);                                                                                                   
                                                        ?>
		<div id="sequence_png" style="width: 1000px;margin: auto;height: auto !important;height:350px;min-height:350px;text-align:center;">
						<img src="<?php echo $img;?>" style="width: 1000px;" >
		</div>
                                                        <tr style="height: 20px;background-color: #8497b0;text-align: center;">
                                                                <td><?php echo $arr[0];?></td>
								<td colspan="2" ><?php echo $arr[1];?></td>
                                                                <td><?php echo $arr[2];?></td>
                                                                <td><?php echo $arr[3];?></td>
                                                                <td><?php echo $arr[4];?></td>
                                                                <td><?php echo $arr[5];?></td>

                                                                <td><?php echo $arr[6];?></td>
                                                        </tr>
                                                        <?php

									while(!feof($fp))
									{
										$cont = fgets($fp);
										if(feof($fp)){break;}
										$cont = str_replace('\n','',$cont);
										$arr = explode('	',$cont);					
							?>
							<tr style="height: 20px;line-height:20px;background-color: #e7e6e6;text-align: center;">
								<td><?php echo $arr[0];?></td>
								<td colspan="2" style="text-align:left;" >
									&nbsp;
									<?php
										$char = str_split($arr[1]);
										$ctrl = 0;
										$num = 1;
										for($i=0;$i<sizeof($char);$i++){
										//	echo $char[$i];
											if($char[$i]>='a'&&$char[$i]<='z'){
												$ele = strtoupper($char[$i]);
												?><b style="color:red;"><?php echo $ele;?></b><?php }else{echo $char[$i];}
										}
										//echo "$ctrl ";
										//echo "$num ";
										/*
										if($ctrl == 1){
										$str_seq = strtoupper($arr[1]);
										$str1 = substr($str_seq,0,$num);
										$str2 = substr($str_seq,$num,$l);
										$str3 = substr($str_seq,$num+11);
									echo $str1;?><b style="color:red;"><?php echo $str2;?></b><?php echo $str3;  # 不能换行，处理换行后的html空格问题
										}else{
											echo $arr[1];
										}*/
									?>
									</td>
								<td><?php echo $arr[2];?></td>
								<td><?php echo $arr[3];?></td>
								<td><?php echo $arr[4];?></td>
								<td><?php echo $arr[5];?></td>
								
								<td><?php echo $arr[6];?></td>
							</tr>
							<?php
								}fclose($fp);
								unset($fp);
								unlink($file_path);
								}else{?>
			<p style="margin: auto;text-align:center;font-size:200%;">No Leucine-rich repeat<br><br>If refreshed, please resubmit</p>
									<?php
								}
							}else{
								?>
			<p style="margin: auto;text-align:center;font-size:200%;">No Leucine-rich repeat<br><br>If refreshed, please resubmit</p>
								<?php
							}

							?>
						</table></code>
					</div>
			</div>
			
			<div style="height:30px;"></div>
			<div id="bottom" style="float: left;width: 1350PX;height: 50px;">
				<div id="分界线" style="width: 1000px;border-bottom: 2px solid #C7D3DE;height: 20px;margin: auto;"></div>
				<div id="" style="width: 1350px;background-color:#1f4e79 ; margin: auto;text-align: center;height: 50px;">
					<p style="color: #FFFFFF;line-height: 50px;font-size: small;">Key Laboratory of Horticultural Plant Biology, Huazhong Agricultural University of China, Hubei, Wuhan 430070,China.</p>
				</div>
			</div>
		</div>
	</body>
</html>

