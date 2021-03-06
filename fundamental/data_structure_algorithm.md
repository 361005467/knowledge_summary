# 数据结构

- 二叉搜索树：左子树节点比右子树小。普通二叉树有可能退化成单链表
  - avl 树：任意节点的左右两个子树的高度差的绝对值不超过 1
  - 红黑树：最长路径的长度 小于等于 最短路径的两倍
  - avl 树更平衡，搜索更快，插入删除比红黑树慢。worst-case 都是 log n。均摊时间复杂度不一样。 红黑树 insert delete 均摊 o(1)

# 算法

排序

- 快速排序
  - 调整：取 pivot，让所有小的放在 pivot 左边。
  - 方法： 先从右边扫，互换，再从这边扫；直到 i==j
- 归并排序

  - 递归直到 l=r，然后对两个排好序的数组进行归并排序

- 插入排序

  - 将无序元素插入有序数组中，然后移动元素

- 选择排序
  - 从无序数组中找最小元素，然后和无序的第一个交换
- 冒泡排序
  - 两两比较转换，把大数往最右边移动
- 堆排序
  - 建堆（o(n)））,顶部跟尾部互换，调整堆（单次 log（n））

合并排序链表

- 新建链表 两两比较，跟归并排序一样
- 递归，取两 list 的第一个元素比较，取小的一个，然后将剩下两个 list 递归

链表是否有环

- 快慢指针前进，如果有圈会相遇，没有就直到空指针结束

第 k 大数

- 最小堆法：维护一个 k 个数的最小堆，，将剩下的元素和堆顶比较替换。 o(n)+ （n-k）.lg(n)
- 归并：各自分开找第 k 大，然后合起来再找第 k 大

lru

- 哈希+双向链表
- 双向是为了删除 O(1)，哈希为了查找 o(1)
- lru-k：需要维护每个 key 的访问次数

统计大文件词频

- 逐行读，将单词写到小文件。将相同的单词哈希写到同一个文件
