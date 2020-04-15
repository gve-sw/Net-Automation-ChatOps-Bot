#!/bin/bash
ip_addr=$1
dest_route=$2
fil_name=$RANDOM
echo " Getting Route Entry from $ip_addr"
#cp /myhubot/bash/handlers/.route-filter.py
#/myhubot/bash/handlers/$fil_name.py
sleep 5
#chmod +x /myhubot/bash/handlers/$fil_name.py
#sed -i 's/ipaddr/'$ip_addr'/g' /myhubot/bash/handlers/$fil_name.py
#sed -i 's/dest/'$dest_route'/g' /myhubot/bash/handlers/$fil_name.py
#python /myhubot/bash/handlers/$fil_name.py
python route-filter.py
sleep 2
#rm /myhubot/bash/handlers/$fil_name.py
exit 0