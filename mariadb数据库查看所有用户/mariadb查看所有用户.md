04.11 10:52
mariadb查看所有用户
查看所有用户



select user, plugin from mysql.user;



https://www.cnblogs.com/apollo1616/articles/10294490.html#autoid-0-3-0


跳过授权

mysqld --skip-grant-tables --user=mysql &


update mysql.user set authentication_string=password('a123')  where user='root' and host='localhost';     


菜鸟教程

MySQL 重置 root 密码


https://www.runoob.com/note/27730




mariadb官方教程


https://mariadb.com/kb/zh-cn/mariadb/





