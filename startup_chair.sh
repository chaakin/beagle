### Start auto-login stuff here
echo none > /sys/class/leds/beaglebone\:green\:usr2/trigger
echo none > /sys/class/leds/beaglebone\:green\:usr0/trigger

# Flash LED0 5 times real quick to let me know POST is done
for i in 1 2 3 4 5
do
	echo 255 > /sys/class/leds/beaglebone\:green\:usr0/brightness
	sleep .02
	echo 0 > /sys/class/leds/beaglebone\:green\:usr0/brightness
	sleep .02
done

### Now run main python script
sleep 2s
rm -f /root/beagle/stop_blink.txt

cd /root/beagle/ && python blink.py &
cd /root/beagle/ && python switch_plus_electric.py
