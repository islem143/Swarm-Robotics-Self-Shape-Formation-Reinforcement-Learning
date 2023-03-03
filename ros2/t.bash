# #!/bin/bash
source install/setup.bash
while : 
do 
    x="pgrep dqn"
    e="pgrep env"
    y=$(eval "$x")
    z=$(eval "$e")
    if [ -z "$y" ]; then echo null; 
    else
       echo "not null"
    fi   
    sleep 1

done
