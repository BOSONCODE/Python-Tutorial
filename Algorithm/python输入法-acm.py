# encoding: utf-8  
  
''''' 
Created on Nov 6th, 2014 
 
@author: Speedcell 
'''  
  
'''''Python��������Ұ���ַ���������Ҫ�Լ�ת���� 
stripȥ���������˵Ŀհ׷�������str 
slipt���ַ������հ׷��𿪣�����[str] 
map��list�����ֵӳ�䵽ָ�����ͣ�����[type] 
 
EOF��ץ�쳣 
 
print����Ӷ��žͲ��ỻ�У�����֮����Ȼ3.x�����д��� 
 
��Ŀϸ��û��̫ϸ�������еĵط����ԣ���Ҫ������Щϸ���� 
 
��������ϤǤ�'''  
  
# �ж����������ݣ���û�о���ĸ������ж����飬ֻ�������Ӧÿ�����룬Ӧ�����������  
  
while True:  
    try:  
        a, b = map(int, raw_input().strip().split())  
        print a + b,  
    except EOFError:  
        break  
      
# ����һ���������������ǽ������ж��������ݣ�Ȼ��������ÿ�����ݵľ���ֵ��  
  
tcase = int(raw_input().strip())  
for case in range(tcase):  
    a, b = map(int, raw_input().strip().split())  
    print a + b,  
      
# �ж����������ݣ�û�о���ĸ������ж�����,������Ŀȴ����������ʲô����  
  
while True:  
    a, b = map(int, raw_input().strip().split())  
    if a == 0 and b == 0:  
        break  
    print a + b,  
      
# �����ж��飬��ȴ��Ŀ������ÿ����������ʲô������������ֲ�֮ͬ�����ڣ�ÿ�����붼����Ӧ��ϸ����  
      
tcase = int(raw_input().strip())  
for case in range(tcase):  
    a, b = map(int, raw_input().strip().split())  
    if a == 0 and b == 0:  
        break  
    print a + b,  
      
# ��ε�����ʵ������һ�����������������ж����У�������ÿһ�С�����ÿһ�е����룬�л���Ϊ��һ������������������һ����������һ������һ���ж������롣  
  
tcase = int(raw_input().strip())  
for case in range(tcase):  
    data = map(int, raw_input().strip().split())  
    n, array = data[0], data[1:]  
      
    sum = 0  
    for i in range(n):  
        sum += array[i]  
    print sum,  
      
# �ж����������ݣ�����ÿ���������ݵĵ�һ��������������ݽ�����Ҫ����������  
  
while True:  
    try:  
        data = map(int, raw_input().strip().split())  
        n, array = data[0], data[1:]  
              
        sum = 0  
        for i in range(n):  
            sum += array[i]  
        print sum,  
    except EOFError:  
        raise  
      
# ���������ֻ�Ǽ򵥵���ÿ�������߶��һ�����ж��ѣ�  
  
while True:  
    try:  
        a, b = map(int, raw_input().strip().split())  
        print a + b  
    except EOFError:  
        break  
      
# �������͵����ע��ľ��ǻ��У�������Ŀ˵����������У�ÿ������֮����ʲôʲô�����������ڶ�Ӧ�����ͬʱҪ�ж�һ���Ƿ������һ�������������ǣ��� ����Ŀ��˵�Ķ��������һ���ǻ��л�ո񣩣�����ǣ���ֱ�ӽ�����  
  
while True:  
    data = raw_input().strip()  
    if data.isspace():  
        break  
    else:  
        data = map(int, data)  
        n, array = data[0], data[1:]  
                  
        sum = 0  
        for i in range(n):  
            sum += array[i]  
        print sum, 