#!/bin/sh

folder=../uploads/
CR=`printf '\r'`

# CGI output must start with at least empty line (or headers)
echo "Content-type: text/html"
printf '\r\n'

while read -r line; do
    #get file name of uploaded file
    echo "$line" | grep "filename" > /dev/null && file="$(echo "$line"|cut -d\" -f4)"
    test x"$line" = x"" && break
    test x"$line" = x"$CR" && break
done

echo "$file uploaded."
cat >"${folder}${file}"

printf "<html>\n<body>\nFile upload has been accepted"
