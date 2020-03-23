文本处理

- sed -i '/{MATCHTEXT}/a\{APPENDTEXT}' FILENAME
- find DIRPATH -type f -name FILENAME
- grep -rn "string to be searched" DIR
- tail -f path | grep -v -E 'IGNORE_TEXT|lTEXT2|TEXT3'

网络

- tcpdump -i eth1 'dst host 9.81.23.59 and dst port 7001'
- tcpdump -i eth1 'src 9.81.28.92 and dst 10.228.10.28'

进程

- 查进程号 netstat -nap | grep PORT_NUM
- 进程启动位置 lsof -p PROCESS_NUM
- 查句柄  ls -lrt /proc/pid/fd
- pidof PROCESS_NUM
- 查子进程 cat /proc/A_pid/limits
