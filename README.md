--2022.01.25 this is for Seeed reComputer Jetson Version product      
this is used for Jetson final product testing     
auto_csi 	-> CAM0 & CAM1   
auto_debug	-> Micro USB port   
auto_iperf	-> eth0 speed   
auto_usb	-> Just found usb devices   
auto_usb_speed	-> USB write & read speed   
auto_camera	-> take vidio by 2pcs csi   
auto_gpio	-> test pi header   
auto_gpio_key	-> test PCIe E Key gpio   
factory_test	-> run all the function test   
v4l2_test	-> camara test tool   
boot_from_usb	-> modify /boot/extlinux/extlinux.conf for booting from usb   
t		-> factory operator using   

python3:   
aliyun upload   
eeprom write   

log file save at oss2 bucket: recomputerjetsonlituo   

#40Pin Header GPIO No   
75,78 74,77 216,51 50,168 14,20 194,19, 16,13 17,15 18,232 76,79 149,49 200,48 38,12   
#40Pin Header GPIO testing Header   
3-40, 5-38, 7-36, 11-32, 13-26, 15-24, 19-22, 21-18, 23-16, 29-10, 35-12, 31-8, 33-37   

#Enable eeprom steps      
mkdir /lib/modules/4.9.253-tegra/extra      
cp drivers/misc/eeprom/at24.ko /lib/modules/4.9.253-tegra/extra   
cp drivers/misc/mods/mods.ko /lib/modules/4.9.253-tegra/extra   
cp drivers/nvmem/nvmem_core.ko /lib/modules/4.9.253-tegra/extra   
depmod -a   
cp drivers/jetson-sdmmc-overlay.dtbo /boot      
cd /boot   
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n "reComputer sdmmc"      


