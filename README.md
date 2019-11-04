# 系统结构实验课

## Lab0-基础知识

### 实验准备

1. 抓取资料库
    - 安装 [Windows版本git](https://gitforwindows.org/) 后执行 `git clone https://github.com/cs-course/computer-architecture-experiment`
      - git 详细知识可以通过 [git-tutorial](https://github.com/cs-course/git-tutorial) 学习
    - 或者 [下载](https://github.com/cs-course/computer-architecture-experiment/archive/master.zip) 后解压缩

2. 建立实验用 Linux 64-bit 虚拟机环境
    - 安装 **VirtualBox 虚拟机** ([下载](https://www.virtualbox.org/wiki/Downloads))
    - 安装 **Vagrant 虚拟机管理工具** ([下载](https://www.vagrantup.com/downloads.html))
      - Vagrant 详细知识可以通过 [vagrant-tutorial](https://github.com/cs-course/vagrant-tutorial) 学习
    - 导入基础镜像
      - 下载镜像至资料库目录，下载地址：[微云](https://share.weiyun.com/5zo2M2m)，[官方](http://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64-vagrant.box)
      - 进入 Windows 命令行窗口
        - 使用 "Windows系统 --> 命令提示符"
        - 或者按下 "Win+R" 运行 cmd 命令
      - 进入资料库目录，执行 `vagrant box add bionic-server-cloudimg-amd64-vagrant.json`
    - 初始化虚拟机系统
      - 在资料库目录中执行`vagrant up`
      - 执行`vagrant status`检查是否正常运行
      - 使用完成后，执行 `vagrant halt` 关闭虚拟机，下次仍通过 `vagrant up` 重启虚拟机
      - **注意**：若不再需要，或需重建，可用 `vagrant destroy -f` 清除

### 实验内容

检查系统配置

1. 处理器信息

```bash
vagrant@ubuntu-bionic:~$ lscpu
Architecture:        x86_64 # 这些内容各机不完全一样
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              2      # CPU核数 (虚拟机只使用部分主机处理器核)
On-line CPU(s) list: 0,1
...
L1d cache:           32K    # L1数据缓存
L1i cache:           32K    # L1指令缓存
L2 cache:            256K   # L2缓存
L3 cache:            6144K  # L3缓存
NUMA node0 CPU(s):   0,1
...
```

2. 主存储器信息

```bash
vagrant@ubuntu-bionic:~$ free -h
              total        used        free      shared  buff/cache   available
Mem:           985M         76M        726M        588K        181M        771M
Swap:            0B          0B          0B
```

**注意**：在 [Vagrantfile](./Vagrantfile) 里面已经设置虚拟机内存为 1GB。

3. 外部存储器信息

```bash
vagrant@ubuntu-bionic:~$ lsblk
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
sda      8:0    0  10G  0 disk
└─sda1   8:1    0  10G  0 part /
sdb      8:16   0  10M  0 disk
vagrant@ubuntu-bionic:~$ df -h -x tmpfs
Filesystem      Size  Used Avail Use% Mounted on
udev            481M     0  481M   0% /dev
/dev/sda1       9.7G  1.7G  8.1G  17% /
vagrant         237G  175G   62G  74% /vagrant
vagrant_data    237G  175G   62G  74% /vagrant_data
vagrant@ubuntu-bionic:~$
```

## Lab1-指令系统及指令集并行

### 实验准备

1. 安装JDK [下载](https://www.oracle.com/technetwork/java/javase/overview/index.html)
2. 下载熟悉 [MIPS64](https://www.edumips.org/)

### 实验内容

……

### 参考

- [WinMIPS64](http://indigo.ie/~mscott/)

## Lab2-流水线技术

### 实验准备

与上一次实验相同

### 实验内容

……

### 参考

与上一次实验相同

## Lab3-存储系统

### 实验准备

1. 开启 Windows 命令行窗口，进入资料库目录，执行 `vagrant up` 开启实验用虚拟机 (*在 Lab0 中建立*)
2. 解压缩 cachelab-handout.tar.gz 文件进资料库中 data 目录
   - **注意**：此目录与主机共享，以便将作业保存在主机中
   - 使用 `vagrant ssh` 进入虚拟机，执行命令行 `cd /vagrant_data && tar xzvf ~/cachelab-handout.tar.gz`
   - 或在主机中使用工具软件将 cachelab-handout.tar.gz 解压缩进data目录
3. 执行 `vagrant ssh default` 进入虚拟机控制台，执行 `cd /vagrant_data` 进入此目录，用 `ls` 命令确认 cachelab 实验文件已就位

### 实验内容

…缓存仿真器实现…

…矩阵转置…

### 参考

  - [Computer Systems: A Programmer's Perspective, 3/E (CS:APP3e)](http://www.csapp.cs.cmu.edu/)，[实验作业](http://csapp.cs.cmu.edu/3e/labs.html)

## Lab4-输入输出系统

### 实验准备

1. 开启 Windows 命令行窗口，进入资料库目录，执行 `vagrant up` 开启实验用虚拟机 (*在 Lab0 中建立*)

2. 执行 `vagrant ssh` 进入虚拟机
3. 执行 `cat /proc/mdstat` 确认 mdadm 与 Linux 内核配置正常

```bash
vagrant@ubuntu-bionic:~$ cat /proc/mdstat
Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10]
unused devices: <none>
vagrant@ubuntu-bionic:~$
```

### 实验内容

…创建几个loop设备…

…使用mdadm配置软阵列…

### 参考

  - [在Linux里面建立虚拟块设备 (loop设备)](https://www.thegeekdiary.com/how-to-create-virtual-block-device-loop-device-filesystem-in-linux)
  - [在Ubuntu 16.04里使用mdadm建立RAID](https://www.digitalocean.com/community/tutorials/how-to-create-raid-arrays-with-mdadm-on-ubuntu-16-04)
  - [软阵列(Software RAID) HOWTO::RAID配置](https://raid.wiki.kernel.org/index.php/RAID_setup)

## Lab5-互连网络

### 实验准备

……

### 实验内容

……

