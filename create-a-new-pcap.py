#!/usr/bin/env python
#coding=utf8
import sys
import os
from scapy.layers import http
import scapy.all as scapy

for i in range(0,10):

    charset = b'GET /kami.jspx?ka=247 HTTP/1.1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1\r\nHost: 10.121.64.102:8083\r\nAccept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2\r\nConnection: keep-alive\r\n\r\n'
    charisset = b'GET /kami.jspx?kami=2%d6 HTTP/1.1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1\r\nHost: 10.121.64.102:8083\r\nAccept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2\r\nConnection: keep-alive\r\n\r\n'%(i)
    charsett = b'GET /kami.jspx?ka=757 HTTP/1.1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1\r\nHost: 10.121.64.102:8083\r\nAccept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2\r\nConnection: keep-alive\r\n\r\n'
    stringset = '/k%d.aspx?ka=5%d0'%(i,i)
    stringsett = '/k%d.aspx?ka=3%d8'%(i,i)
    stringsettt = '/k%d.aspx'%(i)

    list_a = []
    if __name__ == '__main__':
        count = 0           
        port = 0
        pcap_dir = 'Behinder_v2.0.1-2.pcap'
        packeges = scapy.rdpcap(pcap_dir)
        
        while(count!=1):

            for p in packeges:   
                #p.show()
                temp = p         
                if 'TCP' in temp:
                    print("1")
                    sport = temp['TCP'].sport
                    window = temp['TCP'].window
                    chksum = temp['TCP'].chksum
                    print(sport)
                    if 'Raw' in temp:
                        if(sport == 49211):
                            if (window == 64240):
                                print("2")
                                temp['Raw'].load = charisset
                                list_a.append(temp)
                            else:
                                list_a.append(temp)
                        else:
                            list_a.append(temp)
                    else:
                        list_a.append(temp)
                else:
                    list_a.append(temp)
            


                                  

            count = count + 1

        pcap_dirafter = 'Behinder_v2.0.1-2-1-%d.pcap'%(i)
        scapy.wrpcap(pcap_dirafter,list_a)


