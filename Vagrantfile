# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_version = "20191030.0.0"
  config.vm.box_check_update = false

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  config.vm.synced_folder "./data", "/vagrant_data", create: true, owner: "root", group: "root"

  config.vm.provision "file", source: "cachelab-handout.tar.gz", destination: "/home/vagrant/cachelab-handout.tar.gz"
  config.vm.provision "file", source: "hust.list", destination: "/home/vagrant/hust.list"
  config.vm.provision "shell", inline: <<-SHELL
    mv /home/vagrant/hust.list /etc/apt/sources.list.d/hust.list
    apt-get update
    apt-get install -y valgrind
  SHELL
end
