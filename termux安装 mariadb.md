04.08 17:49
$ pkg update

//termux安装 mariadb

$ pkg install mariadb
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libedit
The following NEW packages will be installed:
  libedit mariadb
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 17.5 MB of archives.
After this operation, 181 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 libedit aarch64 20191231-3.1-0 [71.6 kB]
Get:2 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 mariadb aarch64 2:10.4.12-4 [17.4 MB]
Fetched 17.5 MB in 51s (340 kB/s)
Selecting previously unselected package libedit.
(Reading database ... 3162 files and directories currently installed.)
Preparing to unpack .../libedit_20191231-3.1-0_aarch64.deb ...
Unpacking libedit (20191231-3.1-0) ...
Selecting previously unselected package mariadb.
Preparing to unpack .../mariadb_2%3a10.4.12-4_aarch64.deb ...
Unpacking mariadb (2:10.4.12-4) ...
Setting up libedit (20191231-3.1-0) ...
Setting up mariadb (2:10.4.12-4) ...
Initializing mysql data directory...
Installing MariaDB/MySQL system tables in '/data/data/com.termux/files/usr/var/lib/mysql' ...
OK

To start mysqld at boot time you have to copy
support-files/mysql.server to the right place for your system


Two all-privilege accounts were created.
One is root@localhost, it has no password, but you need to
be system 'root' user to connect. Use, for example, sudo mysql
The second is u0_a169@localhost, it has no password either, but
you need to be the system 'u0_a169' user to connect.
After connecting you can set the password, if you would need to be
able to connect as any of these users with a password and without sudo

See the MariaDB Knowledgebase at http://mariadb.com/kb or the
MySQL manual for more instructions.

You can start the MariaDB daemon with:
cd '/data/data/com.termux/files/usr' ; /data/data/com.termux/files/usr/bin/mysqld_safe --datadir='/data/data/com.termux/files/usr/var/lib/mysql'

You can test the MariaDB daemon with mysql-test-run.pl
cd '/data/data/com.termux/files/usr/mysql-test' ; perl mysql-test-run.pl

Please report any problems at http://mariadb.org/jira

The latest information about MariaDB is available at http://mariadb.org/.
You can find additional information about the MySQL part at:
http://dev.mysql.com
Consider joining MariaDB's strong and vibrant community:
https://mariadb.org/get-involved/

$
