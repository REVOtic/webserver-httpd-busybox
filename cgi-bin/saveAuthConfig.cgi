#!/bin/sh
alias urldecode='sed "s@+@ @g;s@%@\\\\x@g" | xargs -0 printf "%b"'
echo -e "Content-type: text/plain\n"
decoded_str=`echo $QUERY_STRING | urldecode`
echo $decoded_str
touch /run/shm/auth.conf
echo $decoded_str > /run/shm/auth.conf
