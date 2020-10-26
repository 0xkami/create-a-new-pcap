# create-a-new-pcap
最近写了一个改包的脚本
Python中有一个scapy库，是个好东西
Scapy 中文文档：https://www.cntofu.com/book/33/4.md
## 0x1 读取包中的数据
  函数：show(),scapy.rdpcap(路径)
  使用：
  pcap_dir = 'xx.pcap'#文件名也可
  packeges = scapy.rdpcap(pcap_dir)
    for p in packeges:   
      p.show()
  可以清楚看到每层的数据
## 0x2 修改对应位置的数据
  通过读取包中每层的数据，我们可以看到每层里有哪些对应的名称和数据
  比如我们想改一个DNS包里Host处的域名，就只要找到要改的地方的层名(DNS Question Record)和“变量名”(qname)，改为自己设置的值即可，然后把数据插到列表里，最后使用scapy.wrpcap(包名,数据)输出数据包即可
  注意：要修改一个包时，需要先看清楚包的结构，有些DNS包并不能解析出对应的层名或”变量名“，而是另外的结构
  for p in packeges: 
    temp = p
    if temp.haslayer("DNS Question Record"):#对应的层
      temp["DNS Question Record"].qname = charset1 #qname是对应域名数据的命名，可以看作变量名
      list_a.append(temp)
    else:
      list_a.append(temp)
