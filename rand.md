# 随机数产生



## /dev/random 真随机数

要想获取真的随机数，需要从无规则的物理现象获取。内核维护了一个熵池，用来收集不可预设的数据，例如设备输入频率，中断产生次数等。 熵池就是一个变化的数字，默认最大值为4096 bit。 读取/dev/random则可以获取真正的随机数。

然而熵池是有限的。熵池会被读取消耗。读取的数据如果超过熵池大小，会造成阻塞。

可以通过下面命令来观察熵池被消耗的情况：
- 读取熵池 cat /dev/random
- 查看熵池大小: cat  /proc/sys/kernel/random/entropy_avail


# /dev/urandom， srand 伪随机数
srand 和 /dev/urandom 产生的是一个固定数字序列，可以被预测。 srand加seed的作用只是从固定数字序列的某个位置开始读取，返回的也是一个固定数字序列。 

urandom使用例子：
- head -c 50 /dev/urandom | tr -dc 'a-z' | fold -w 3 | head -n 1





