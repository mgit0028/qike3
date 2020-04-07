04.08 17:50
Welcome to Termux!

Wiki:            https://wiki.termux.com
Community forum: https://termux.com/community
Gitter chat:     https://gitter.im/termux/termux
IRC channel:     #termux on freenode

Working with packages:

 * Search packages:   pkg search <query>
 * Install a package: pkg install <package>
 * Upgrade packages:  pkg upgrade

Subscribing to additional repositories:

 * Root:     pkg install root-repo
 * Unstable: pkg install unstable-repo
 * X11:      pkg install x11-repo

Report issues at https://termux.com/issues

//更新

$ pkg update
Ign:1 https://dl.bintray.com/grimler/game-packages-24 games InRelease
Ign:2 https://dl.bintray.com/grimler/science-packages-24 science InRelease
Get:3 https://dl.bintray.com/grimler/game-packages-24 games Release [5344 B]
Get:5 https://dl.bintray.com/grimler/science-packages-24 science Release [5348 B]
Get:6 https://dl.bintray.com/grimler/game-packages-24 games Release.gpg [475 B]
Ign:4 https://dl.bintray.com/termux/termux-packages-24 stable InRelease
Get:7 https://dl.bintray.com/grimler/science-packages-24 science Release.gpg [475 B]
Get:8 https://dl.bintray.com/termux/termux-packages-24 stable Release [6061 B]
Get:9 https://dl.bintray.com/grimler/game-packages-24 games/stable aarch64 Packages [3332 B]
Get:10 https://dl.bintray.com/termux/termux-packages-24 stable Release.gpg [821 B]
Get:11 https://dl.bintray.com/grimler/science-packages-24 science/stable aarch64 Packages [3973 B]
Get:12 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 Packages [114 kB]
Fetched 140 kB in 5s (23.8 kB/s)
Reading package lists... Done
Building dependency tree... Done
8 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Calculating upgrade... Done
The following NEW packages will be installed:
  dialog
The following packages will be upgraded:
  command-not-found game-repo gpgv gzip
  openssl science-repo termux-tools util-linux
8 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 2068 kB of archives.
After this operation, 217 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 gzip aarch64 1.10-3 [79.1 kB]
Get:2 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 dialog aarch64 1.3-20200327-0 [92.0 kB]
Get:3 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 util-linux aarch64 2.35.1-1 [567 kB]
Get:4 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 termux-tools all 0.78 [6024 B]
Get:5 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 gpgv aarch64 2.2.20-2 [140 kB]
Get:6 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 openssl aarch64 1.1.1f [1128 kB]
Get:7 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 command-not-found aarch64 1.49 [53.6 kB]
Get:8 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 game-repo all 1.2 [1104 B]
Get:9 https://dl.bintray.com/termux/termux-packages-24 stable/main aarch64 science-repo all 1.1 [1104 B]
Fetched 2068 kB in 2min 16s (15.2 kB/s)
(Reading database ... 3152 files and directories currently installed.)
Preparing to unpack .../gzip_1.10-3_aarch64.deb ...
Unpacking gzip (1.10-3) over (1.10-2) ...
Setting up gzip (1.10-3) ...
Selecting previously unselected package dialog.
(Reading database ... 3152 files and directories currently installed.)
Preparing to unpack .../dialog_1.3-20200327-0_aarch64.deb ...
Unpacking dialog (1.3-20200327-0) ...
Setting up dialog (1.3-20200327-0) ...
(Reading database ... 3157 files and directories currently installed.)
Preparing to unpack .../util-linux_2.35.1-1_aarch64.deb ...
Unpacking util-linux (2.35.1-1) over (2.35.1) ...
Setting up util-linux (2.35.1-1) ...
(Reading database ... 3157 files and directories currently installed.)
Preparing to unpack .../termux-tools_0.78_all.deb ...
Unpacking termux-tools (0.78) over (0.74) ...
Setting up termux-tools (0.78) ...
(Reading database ... 3158 files and directories currently installed.)
Preparing to unpack .../gpgv_2.2.20-2_aarch64.deb ...
Unpacking gpgv (2.2.20-2) over (2.2.19) ...
Setting up gpgv (2.2.20-2) ...
(Reading database ... 3158 files and directories currently installed.)
Preparing to unpack .../openssl_1.1.1f_aarch64.deb ...
Unpacking openssl (1.1.1f) over (1.1.1e) ...
Setting up openssl (1.1.1f) ...
(Reading database ... 3158 files and directories currently installed.)
Preparing to unpack .../command-not-found_1.49_aarch64.deb ...
Unpacking command-not-found (1.49) over (1.48) ...
Preparing to unpack .../archives/game-repo_1.2_all.deb ...
Unpacking game-repo (1.2) over (1.1) ...
Preparing to unpack .../science-repo_1.1_all.deb ...
Unpacking science-repo (1.1) over (1.0) ...
Setting up game-repo (1.2) ...
Downloading updated package list ...
Ign:2 https://dl.bintray.com/grimler/game-packages-24 games InRelease
Ign:3 https://dl.bintray.com/grimler/science-packages-24 science InRelease
Ign:1 https://dl.bintray.com/termux/termux-packages-24 stable InRelease
Get:5 https://dl.bintray.com/grimler/game-packages-24 games Release [5344 B]
Hit:5 https://dl.bintray.com/grimler/game-packages-24 games Release
Get:7 https://dl.bintray.com/grimler/science-packages-24 science Release [5348 B]
Hit:7 https://dl.bintray.com/grimler/science-packages-24 science Release
Get:4 https://dl.bintray.com/termux/termux-packages-24 stable Release [6061 B]
Hit:4 https://dl.bintray.com/termux/termux-packages-24 stable Release
Reading package lists... Done
Building dependency tree
Reading state information... Done
All packages are up to date.
Setting up science-repo (1.1) ...
Downloading updated package list ...
Ign:1 https://dl.bintray.com/grimler/game-packages-24 games InRelease
Ign:3 https://dl.bintray.com/grimler/science-packages-24 science InRelease
Get:4 https://dl.bintray.com/grimler/game-packages-24 games Release [5344 B]
Hit:4 https://dl.bintray.com/grimler/game-packages-24 games Release
Ign:2 https://dl.bintray.com/termux/termux-packages-24 stable InRelease
Get:7 https://dl.bintray.com/grimler/science-packages-24 science Release [5348 B]
Hit:7 https://dl.bintray.com/grimler/science-packages-24 science Release
Get:6 https://dl.bintray.com/termux/termux-packages-24 stable Release [6061 B]
Hit:6 https://dl.bintray.com/termux/termux-packages-24 stable Release
Reading package lists... Done
Building dependency tree
Reading state information... Done
All packages are up to date.
Setting up command-not-found (1.49) ...
$
