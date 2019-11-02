# 系统结构实验课

## Lab0-基础知识

### 实验准备

1. 抓取资料库
    - 安装 [Windows版本git](https://gitforwindows.org/) 后执行 `git clone https://github.com/cs-course/computer-architecture-experiment`
    - 或者 [下载](https://github.com/cs-course/computer-architecture-experiment/archive/master.zip) 后解压缩

2. 建立实验用 Linux 64-bit 虚拟机环境
    - 安装 **VirtualBox 虚拟机** ([下载](https://www.virtualbox.org/wiki/Downloads))
    - 安装 **Vagrant 虚拟机管理工具** ([下载](https://www.vagrantup.com/))
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
      - 若不再需要，或需重建，可用 `vagrant destroy -f` 清除

### 实验内容

检查系统配置

lscpu ……

free ……

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

基于实验用虚拟机

解压缩CacheLab实验资料

### 实验内容

CacheLab

### 参考

  - [Computer Systems: A Programmer's Perspective, 3/E (CS:APP3e)](http://www.csapp.cs.cmu.edu/)，[实验作业](http://csapp.cs.cmu.edu/3e/labs.html)

## Lab4-输入输出系统

### 实验准备

基于实验用虚拟机

确认mdadm与Linux内核配置

### 实验内容

使用mdadm配置软阵列

### 参考

  - [在Linux里面建立虚拟块设备 (loop设备)](https://www.thegeekdiary.com/how-to-create-virtual-block-device-loop-device-filesystem-in-linux)
  - [在Ubuntu 16.04里使用mdadm建立RAID](https://www.digitalocean.com/community/tutorials/how-to-create-raid-arrays-with-mdadm-on-ubuntu-16-04)
  - [软阵列(Software RAID) HOWTO::RAID配置](https://raid.wiki.kernel.org/index.php/RAID_setup)

## Lab5-互连网络

### 实验准备

……

### 实验内容

……

