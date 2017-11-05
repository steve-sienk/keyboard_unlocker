#!/bin/sh
variable=$(ps -ef | grep keyboard_unlocker | wc -l | awk '{print $1}')
echo $variable
if [ $variable \< 2 ]
    then
        python /root/keyboard_unlocker/keyboard_unlocker.py
fi

echo unlocker done

