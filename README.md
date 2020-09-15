# How to setup Odoo version 12 Community

## Resource and download script

#### 1.Install manual
[link tutorial by linuxize](https://linuxize.com/post/how-to-deploy-odoo-12-on-ubuntu-18-04/#before-you-begin).

[link tutorial by getopenerp.com](https://www.getopenerp.com/install-odoo-12-on-ubuntu-18-04/). 
 
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
 
```sudo useradd -m -d /opt/odoo12 -U -r -s /bin/bash odoo12```

_You can use any name for your Odoo user as long you create a PostgreSQL user with the same name._


### Install and Configure PostgreSQL

Install the PostgreSQL package from the Ubuntu’s default repositories:

```
sudo apt install postgresql
```
Once the installation is completed, create a PostgreSQL user with the same name as the previously created system user, in our case that is ``odoo12``:

``` sudo su - postgres -c "createuser -s odoo12"```


### Install Wkhtmltopdf
The `wkhtmltox` package provides a set of open-source command line tools which can render HTML into PDF and various image formats. In order to print PDF reports, you will need the `wkhtmltopdf` tool. The recommended version for Odoo is `0.12.x` which is not available in the official Ubuntu 18.04 repositories.

```
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb
```
Once the download is completed install the package by typing:
```
sudo apt install ./wkhtmltox_0.12.5-1.bionic_amd64.deb
```

## Install and Configure Odoo12

We will install Odoo from the GitHub repository inside an isolated _Python virtual environment._
Before starting with the installation process, change to user _“odoo12”_:
``sudo su - odoo12``

Start by cloning the Odoo 12 source code from the Odoo GitHub repository:

```
git clone https://www.github.com/odoo/odoo --depth 1 --branch 12.0 /opt/odoo12/odoo
```
Once the source code is downloaded, create a new Python virtual environment for the Odoo 12 installation:

```
cd /opt/odoo12
python3 -m venv odoo-venv
```
Next, activate the environment with the following command:

```
source odoo-venv/bin/activate
```

Install all required Python modules with pip3:

```(venv)```  ```pip3 install wheel```

 ``(venv)`` ```pip3 install -r odoo/requirements.txt```

If you encounter any compilation errors during the installation, make sure that you installed all of the required dependencies listed in the _Before you begin_ _ section.

Deactivate the environment using the following command:

```(venv)``` `` deactivate``

Create a new directory for the custom addons:

```
mkdir /opt/odoo12/odoo-custom-addons
```
Switch back to your sudo user:
``` 
exit
```

Next, create a configuration file, by copying the included sample configuration file:

```
sudo cp /opt/odoo12/odoo/debian/odoo.conf /etc/odoo12.conf
```
Open the file and edit it as follows:

```nginx

[options]
; This is the password that allows database operations:
admin_passwd = my_admin_passwd
db_host = False
db_port = False
db_user = odoo12
db_password = False
addons_path = /opt/odoo12/odoo/addons,/opt/odoo12/odoo-custom-addons
```


### Modif your file.conf



## Additional Install

#### Install Nginx
[link tutorial by digitalocean](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04).

#### Install Webmin
[link tutorial by digitalocean](https://www.digitalocean.com/community/tutorials/how-to-install-webmin-on-ubuntu-18-04).
