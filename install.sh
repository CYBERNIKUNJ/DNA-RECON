#!/bin/bash

red="\e[0;31m"
green="\e[0;32m"
off="\e[0m"

function banner() {
clear
echo "          				  ";
echo "  ______   _        _______                 ";
echo " (  __  \ ( (    /|(  ___  )         ______  ";
echo " | (  \  )|  \  ( || (   ) |         | ___ \ ";
echo " | |   ) ||   \ | || (___) |  _____  | |_/ /___  ___ ___  _ __   ";
echo " | |   | || (\ \) ||  ___  | (_____) |    // _ \/ __/ _ \|  _ \  "; 
echo " | |   ) || | \   || (   ) |         | |\ \  __/ (_| (_) | | | |  ";
echo " | (__/  )| )  \  || )   ( |         \_| \_\___|\___\___/|_| |_|  ";
echo " (______/ |/    )_)|/     \|       ";
echo "                                    			       ";
}
                                                   
function termux() {
  echo -e "$red [$green+$red]$off Installing Python ...";
pkg install -y python*
echo -e "$red [$green+$red]$off Installing Requirements ...";
pip3 install -r requirements.txt

  echo -e "$red [$green+$red]$off Checking directories ..."

if [ -e "/data/data/com.termux/files/usr/share/DNA-recon" ]; then
  echo -e "$red [$green+$red]$off A previous installation was found Do you want to replace it? [Y/n]: "
read replace
if [ "$replace" == "y" ] || [ "$replace" == "Y" ] || [ -z "$replace" ]; then
 rm -r "/data/data/com.termux/files/usr/share/DNA-recon"
 rm "/data/data/com.termux/files/usr/bin/DNA-recon"
else
  echo -e "$red [$green✘$red]$off If You Want To Install You Must Remove Previous Installations";
  echo -e "$red [$green✘$red]$off Installation Failed";
 exit
fi
fi

  echo -e "$red [$green+$red]$off Installing ...";
mkdir "/data/data/com.termux/files/usr/share/DNA-recon"
 cp "DNA-recon.py" "/data/data/com.termux/files/usr/share/DNA-recon"
 cp "install.sh" "/data/data/com.termux/files/usr/share/DNA-recon"
 cp -R "utility/" "/data/data/com.termux/files/usr/share/DNA-recon/utility"
 cp -R "pytransform/" "/data/data/com.termux/files/usr/share/DNA-recon/pytransform"
 cp -R "modules/"  "/data/data/com.termux/files/usr/share/DNA-recon/modules"
  echo -e "$red [$green+$red]$off Creating Symbolic Link ...";
  echo "#!/data/data/com.termux/files/usr/bin/bash 
python3 /data/data/com.termux/files/usr/share/DNA-recon/DNA-recon.py" '${1+"$@"}' > "DNA-recon";
 cp "DNA-recon" "/data/data/com.termux/files/usr/bin"
 chmod +x "/data/data/com.termux/files/usr/bin/DNA-recon"
 rm "DNA-recon";
 if [ -d "/data/data/com.termux/files/usr/share/DNA-recon" ] ;
then
echo -e "$red [$green+$red]$off Tool successfully installed and will start in 5s!";
echo -e "$red [$green+$red]$off You can execute tool by typing DNA-recon"
sleep 5;
DNA-recon
else
echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
fi
}

function linux() {
echo -e "$red [$green+$red]$off Installing Python ...";
sudo apt-get install -y python*
echo -e "$red [$green+$red]$off Installing Requirements ...";
pip3 install -r requirements.txt
  echo -e "$red [$green+$red]$off Checking directories..."
if [ -d "/usr/share/DNA-recon" ]; then
    echo -e "$red [$green+$red]$off A Directory DNA-recon Was Found! Do You Want To Replace It? [Y/n]:" ;
    read replace
    if [ "$replace" = "y" ]; then
      sudo rm -r "/usr/share/DNA-recon"
      sudo rm "/usr/share/icons/DNA-recon.png"
      sudo rm "/usr/share/applications/DNA-recon.desktop"
      sudo rm "/usr/local/bin/DNA-recon"

else
echo -e "$red [$green✘$red]$off If You Want To Install You Must Remove Previous Installations";
echo -e "$red [$green✘$red]$off Installation Failed";
        exit
    fi
fi 

echo -e "$red [$green+$red]$off Installing ...";
echo -e "$red [$green+$red]$off Creating Symbolic Link ...";
echo -e "#!/bin/bash
python3 /usr/share/DNA-recon/DNA-recon.py" '${1+"$@"}' > "DNA-recon";
    chmod +x "DNA-recon";
    sudo mkdir "/usr/share/DNA-recon"
    sudo cp "install.sh" "/usr/share/DNA-recon"
    sudo cp "DNA-recon.py" "/usr/share/DNA-recon"
    sudo cp -R "utility/" "/usr/share/DNA-recon/utility"
    sudo cp -R "pytransform/" "/usr/share/DNA-recon/pytransform"
    sudo cp -R "modules/"  "/usr/share/DNA-recon/modules"	
    sudo cp "utility/DNA-LOGO.png" "/usr/share/icons"
    sudo cp "utility/DNA-recon.desktop" "/usr/share/applications"
    sudo cp "DNA-recon" "/usr/local/bin/"
    rm "DNA-recon";

if [ -d "/usr/share/DNA-recon" ] ;
then
echo -e "$red [$green+$red]$off Tool Successfully Installed And Will Start In 5s!";
echo -e "$red [$green+$red]$off You can execute tool by typing DNA-recon"
sleep 5;
DNA-recon
else
echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
fi 
}

if [ -d "/data/data/com.termux/files/usr/" ]; then
banner
echo -e "$red [$green+$red]$off DNA-recon Will Be Installed In Your System";
termux
elif [ -d "/usr/bin/" ];then
banner
echo -e "$red [$green+$red]$off DNA-recon Will Be Installed In Your System";
linux
else
echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
fi
