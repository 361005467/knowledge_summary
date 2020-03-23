- run 启动进程  
- next 执行下一行代码
- step 执行下一行代码。如果是函数则会进入
- break LINENUMBER 在 LINENUMBER 设置断点
- break FILENAME:LINENUMBER 在 FILENAME 文件里的 第LINENUMBER行设置断点
- continue 执行下一个断点
- until LINENUMBER 执行 LINENUMBER 行
- print VARIABLE 打印变量值
- bt 打印函数调用栈
- watch MEM


多线程调试
- info threads 展示所有线程
- set scheduler-locking on 设置只运行当前线程
- thread NUMBER 切换到 NUMBER 线程

多进程调试
- set follow-fork-mode parent/children 调试父进程/子进程
- set detach-on-fork on/off 允许/不允许 子进程创建运行
- show detach-on-fork 展示 detach-on-fork 是否开启
- info inferiors 展示所有进程
- inferior NUMBER 切换到 NUMBER 进程
