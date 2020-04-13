# 系统结构实验课

## 基础知识

### 实验准备

抓取资料库

  - 安装 git ([Windows版本](https://gitforwindows.org/)) 后执行 `git clone https://github.com/cs-course/computer-architecture-experiment`
    - git 详细知识可以通过 [git-tutorial](https://github.com/cs-course/git-tutorial) 学习
  - 或者 [下载](https://github.com/cs-course/computer-architecture-experiment/archive/master.zip) 后解压缩

在Windows上还需要建立实验用**Linux 64-bit**虚拟机环境

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

## 存储系统

### 实验准备

如果是Linux环境，解压缩 cachelab-handout.tar.gz 即可。

如果是Windows环境则需要使用前面建立的虚拟机：

1. 开启 Windows 命令行窗口，进入资料库目录，执行 `vagrant up` 开启实验用虚拟机；
2. 执行 `vagrant ssh` 进入虚拟机，可以看到 `/vagrant_data` 目录，内容对应于主机 `data` 目录，可以先在主机里将 cachelab-handout.tar.gz 放进去；
3. 在虚拟机内，进入 `/vagrant_data` 目录解压缩 cachelab-handout.tar.gz 文件，可执行如下命令
   - `cd /vagrant_data && tar xzvf cachelab-handout.tar.gz`

### 实验内容

1. 缓存仿真器实现
2. 矩阵转置（可选）

### 参考

  - [Computer Systems: A Programmer's Perspective, 3/E (CS:APP3e)](http://www.csapp.cs.cmu.edu/)，[实验作业](http://csapp.cs.cmu.edu/3e/labs.html)
  - [CMU 15-213 CSAPP 深入理解计算机系统 课程视频 (Part12)](https://www.bilibili.com/video/BV1iW411d7hd?p=12)
  - [手工演算工具](./cachelab-extended)

## 输入输出系统

### 实验准备

建议使用虚拟机进行实验

1. 执行 `vagrant up` 开启实验用虚拟机；
2. 执行 `vagrant ssh` 进入虚拟机；
3. 执行 `cat /proc/mdstat` 确认 mdadm 与 Linux 内核配置正常：

```bash
vagrant@ubuntu-bionic:~$ cat /proc/mdstat
Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10]
unused devices: <none>
vagrant@ubuntu-bionic:~$
```

### 实验内容

1. 创建几个loop设备
2. 使用mdadm配置软阵列

### 参考

  - [在Linux里面建立虚拟块设备 (loop设备)](https://www.thegeekdiary.com/how-to-create-virtual-block-device-loop-device-filesystem-in-linux)
  - [在Ubuntu 16.04里使用mdadm建立RAID](https://www.digitalocean.com/community/tutorials/how-to-create-raid-arrays-with-mdadm-on-ubuntu-16-04)
  - [软阵列(Software RAID) HOWTO::RAID配置](https://raid.wiki.kernel.org/index.php/RAID_setup)

