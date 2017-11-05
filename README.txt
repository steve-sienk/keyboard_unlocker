1. Put `keyboard_unlocker.sh` and `run_unlocker.sh` into /root/
2. Add to chron jobs: `sudo chrontab -e`

To connect to the CHIP over USB:
- On mac/unix:
 - ls /dev/cu.*
 - screen /dev/cu.usbmodem14111 9600
 