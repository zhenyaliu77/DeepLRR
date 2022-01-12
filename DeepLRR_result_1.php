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
                    <div style="width: 1000px;height: 640px;text-align: center;">
                        <?php
                            $num = rand(pow(10,10),pow(10,11));
                            $sequence=$_POST['sequence'];
                            
                            if(!$sequence && $_FILES['Usrfile']['size'] ==0 ){$sequence=">eg
MQVSKRMLAGGVRSMPSPLLACWQPILLLVLGSVLSGSATGCPPRCECSAQDRAVLCHRKRFVAVPEGIPTETRLLDLGKNRIKTLNQDEFASFPHLEELELNENIVSAVEPGAFNNLFNLRTLGLRSNRLKLIPLGVFTGLSNLTKLDISENKIVILLDYMFQDLYNLKSLEVGDNDLVYISHRAFSGLNSLEQLTLEKCNLTSIPTEALSHLHGLIVLRLRHLNINAIRDYSFKRLYRLKVLEISHWPYLDTMTPNCLYGLNLTSLSITHCNLTAVPYLAVRHLVYLRFLNLSYNPISTIEGSMLHELLRLQEIQLVGGQLAVVEPYAFRGLNYLRVLNVSGNQLTTLEESVFHSVGNLETLILDSNPLACDCRLLWVFRRRWRLNFNRQQPTCATPEFVQGKEFKDFPDVLLPNYFTCRRARIRDRKAQQVFVDEGHTVQFVCRADGDPPPAILWLSPRKHLVSAKSNGRLTVFPDGTLEVRYAQVQDNGTYLCIAANAGGNDSMPAHLHVRSYSPDWPHQPNKTFAFISNQPGEGEANSTRATVPFPFDIKTLIIATTMGFISFLGVVLFCLVLLFLWSRGKGNTKHNIEIEYVPRKSDAGISSADAPRKFNMKMI";}
                            $title=$_POST['title'];
                            $Lscp=$_POST['Lscp'];
                            $Model = $_POST['model'];
                            if(!$Ldcp=$_POST['Ldcp']){$Ldcp=9;}
                            if(!$Lncp=$_POST['Lncp']){$Lncp=3;}
                            if($_FILES['Usrfile']['size'] > 0)
                            {
                                if($_FILES['Usrfile']['size'] > 10*1024*1024)
                                {
                                        echo "over 10MB <br>";
                                        
                                }
                                elseif($sequence && $_FILES['Usrfile'])
                                {
                                        echo "only one <br>";
                                        
                                }else
                                {
                                    $tmp_path=$_FILES['Usrfile']['tmp_name'];
                                    $upload_path="/var/www/lifenglab/DeepLRR/Upfile/DeepLRR/".$_FILES['Usrfile']['name'];

                                    
                                    if(move_uploaded_file($tmp_path,$upload_path))
                                    {
                                            
                                        $arr = explode(".",$_FILES['Usrfile']['name']);
                                                                              $len = count($arr)-1;
                                                                              $name= $arr[0];
                                                                              for($i=1;$i<$len;$i++)
                                                                              {
                                                                                  $name=$name.".".$arr[$i];
                                                                              }
                                        $name = $name."_$num";
                                        $file_path = "/var/www/lifenglab/DeepLRR/Upfile/DeepLRR/$name.fasta";
                                        rename($upload_path,$file_path);
                                        unset($out);
                                        $Deeplrr_path = "/var/www/lifenglab/DeepLRR/DeepLRR-1.01";
                                                                                exec("python /var/www/lifenglab/DeepLRR/DeepLRR-1.01/DeepLRR_php.py {$file_path} {$Lscp} {$Ldcp} {$Lncp} {$Deeplrr_path} {$Model} 2>&1 ",$out);
                                        //
                                        setcookie("DeepLRR","$name");
                                        setcookie("title","$title");
                                                                              ?><?php
                                        header("refresh:0;url=DeepLRR_file_result.php");
                                          ?><?php
                                     }else
                                    {
                                           echo "upfile failed";
                                    }
                                }
                            }else
                            {
                                $title_num = $title."_$num";
                                $seq_file_path="/var/www/lifenglab/DeepLRR/Upfile/DeepLRR/$title_num.fasta";
                                $file=fopen($seq_file_path,"w+");
                                fwrite($file,$sequence);
                                fclose($file);
                                chmod($seq_file_path,0777);
                                $Deeplrr_path = "/var/www/lifenglab/DeepLRR/DeepLRR-1.01";
                                $predict2 = "/var/www/lifenglab/DeepLRR/DeepLRR-1.01/outcome/$title_num"."_predict2.txt";
                                                                exec("python /var/www/lifenglab/DeepLRR/DeepLRR-1.01/DeepLRR_php.py $seq_file_path $Lscp $Ldcp $Lncp $Deeplrr_path $Model 2>&1",$out);
    //var_dump($out);
                                exec("python /var/www/lifenglab/DeepLRR/DeepLRR-1.01/highlight.py $predict2 $predict2");
                                $png_path = "/var/www/lifenglab/DeepLRR/img/DeepLRR/$title_num.png";
                                 setcookie("img",$title_num);
                                exec("python /var/www/lifenglab/DeepLRR/DeepLRR-1.01/predToscatter.py $seq_file_path $predict2 {$png_path} 2>&1", $out1);
                                                                //var_dump($out);
                                setcookie("DeepLRR","$title");
				?><?php
                                       header("refresh:0;url=DeepLRR_result.php");
                                ?><?php
                            }
                        ?>
                        
                    </div>
            </div>
            
            <div style="height:40px;"></div>
            <div id="bottom" style="float: left;width: 1350PX;height: 50px;">
                <div id="分界线" style="width: 1000px;border-bottom: 2px solid #C7D3DE;height: 20px;margin: auto;"></div>
                <div id="" style="width: 1350px;background-color:#1f4e79 ; margin: auto;text-align: center;height: 50px;">
                    <p style="color: #FFFFFF;line-height: 50px;font-size: small;">Key Laboratory of Horticultural Plant Biology, Huazhong Agricultural University of China, Hubei, Wuhan 430070,China.</p>
                </div>
            </div>
        </div>
    </body>
</html>
