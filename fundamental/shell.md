文本处理

- sed -i '/{MATCHTEXT}/a\{APPENDTEXT}' FILENAME
- find DIRPATH -type f -name FILENAME
- grep -rn "string to be searched" DIR
- tail -f path | grep -v -E 'IGNORE_TEXT|lTEXT2|TEXT3'
- split -l LINENUMBER FILENAME
- seq START_NUM INTERVAL END_NUM

网络

- tcpdump -i eth1 'dst host 9.81.23.59 and dst port 7001'
- tcpdump -i eth1 'src 9.81.28.92 and dst 10.228.10.28'

进程

- 查进程号 netstat -nap | grep PORT_NUM
- 进程启动位置 lsof -p PROCESS_NUM
- 查句柄  ls -lrt /proc/pid/fd
- pidof PROCESS_NUM
- 查子进程 cat /proc/A_pid/limits
- 进程打开句柄数 lsof -n|awk '{print \$2}'|sort|uniq -c|sort -nr
- 查看网络句柄数 lsof |grep IPv4|wc -l lsof |grep TCP|wc -l
- 查 cpu 内存 top: virt分配内存，res使用内存，shm共享内存
- strace -p PROCESS_NAME
