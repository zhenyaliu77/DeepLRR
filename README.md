#网站重搭

#安装Apache2
#sudo apt-get install apache2

#查看状态
#service apache2 status

#安装php
#sudo apt-get install php

#安装其他模块
#sudo apt-get install libapache2-mod-php
#sudo apt-get install php7.2-mysql

#修改文件上传大小限制
#/etc/php/版本号/apache2/php.ini
#upload_max_filesize = 10M
#重启
#service apache2 restart

#将DeepLRR放入/var/www/html/
#cd /var/www/html/DeepLRR
#将用户www-data添加到lifeng组
#usermod -aG lifeng www-data
#chmod 774 *
#将DeepLRR所有者和组设置为lifeng
#chown www-data *
#chgrp www-data *
#定时清理DeepLRR/img/DeepLRR下的文件和Upfile/* 上传的文件，以及脚本文件夹中的outcome目录内的文件

#NBS、RLP、RLK的脚本目录DeepLRR放在/home/lifeng下
#即 /home/lifeng/DeepLRR

#粗暴解决权限问题
#chmod 777 *

#解决环境问题
#修改/etc/apache2下的envvars
#在里面export PATH=（lifeng的PATH变量）
#export PERL5LIB=…
#export PERL_LOCAL_LIB_ROOT=…
#保存退出后重启apache2
#/etc/init.d/apache2 restart


#如果DeepLRR目录不在/var/www/html or /var/www/lifenglab
#在vi中使用以下命令修改,在控制台模式输入以下（先打:）
%s/var\/www\/html/var\/www\/lifenglab/g



