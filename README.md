# How to setup Odoo version 12 Community

## Resource and download script

#### 1.Install manual
[link tutorial by linuxize](https://linuxize.com/post/how-to-deploy-odoo-12-on-ubuntu-18-04/#before-you-begin).

#### 2.Install by Script development
[Yenthe Script](https://github.com/Yenthe666/InstallScript/tree/12.0).


## Requirements
 - python 3.7 for odoo12
 - PostgreSQL
 - Wkhtmltopdf


### Before you begin
Login to you Ubuntu machine as a sudo user and update the system to the latest packages:
```
sudo apt update && sudo apt upgrade
```
Install Git , Pip , Node.js and the tools required to build Odoo dependencies:

```
sudo apt install git python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools node-less
```

### Create Odoo user

 - Create a new system user for Odoo named ``odoo12`` with home directory ``/opt/odoo12`` using the following command:
 
``sudo useradd -m -d /opt/odoo12 -U -r -s /bin/bash odoo12``

_You can use any name for your Odoo user as long you create a PostgreSQL user with the same name._


### Install and Configure PostgreSQL

Install the PostgreSQL package from the Ubuntu’s default repositories:

```
sudo apt install postgresql
```
Once the installation is completed, create a PostgreSQL user with the same name as the previously created system user, in our case that is ``odoo12``:

``sudo su - postgres -c "createuser -s odoo12"``




## Performance

The example takes ~45s to complete.

**Note:** the same setup in *Go* can be found [here](https://github.com/michaelwayman/go-ann) and it **takes ~85s**. The numpy library has been so optimized when dealing with complex mathematics that it is hard to do better, even in a compiled language, even when coding for particular use cases.
