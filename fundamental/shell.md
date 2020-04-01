文本处理

- sed -i '/{MATCHTEXT}/a\{APPENDTEXT}' FILENAME
- find DIRPATH -type f -name FILENAME
- grep -rn "string to be searched" DIR
- tail -f path | grep -v -E 'IGNORE_TEXT|lTEXT2|TEXT3'
- split -l LINENUMBER FILENAME
- seq START_NUM INTERVAL END_NUM
- cat FILENAME | awk -F '|' '{print $6}' | head -1 | sed s'/.$//' | sed 's/^..//'
- cat FILENAME | awk 'BEGIN { FS=":";print "TXT";sum=0};{sum +=\$1};END {print sum}'




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
- 查 cpu 内存 top: virt 分配内存，res 使用内存，shm 共享内存
- strace -p PROCESS_NAME

git
- git checkout --track origin/feat-kpage
- git branch -r
- git diff ecc1f4d65d30aae1d298d15cdc957e4c764f491a HEAD
- git reset --hard HEAD~1