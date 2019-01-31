# Basic Form Action using BusyBox httpd - CGI scripts

> busybox httpd -vfp 8080 -h webserver-httpd-busybox/

Goto http://localhost:8080
Check files in uploads directory


Scripts: https://github.com/metalx1000/busybox-httpd-webserver-scripts
If encounter errors as: 'Syntax error: end of file unexpected (expecting "do")'
> Run: 
    hexdump -C filename.cgi 
    look for 0d 0a sequences. Then strip \r (0d) with the tr command:
    cat filename.cgi | tr -d '\r' >> newfilename.cgi