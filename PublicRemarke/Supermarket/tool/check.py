import re

# a = '<span id="avgPriceTitle" class="item">消费: 1<span class="fn-67HV">.</span><span class="fn-67HV"></span> 元</span>'
# b = re.sub('\.',r'<span class="fppppppppppp"></span>',a)
# print(b)
# print(a)
a = '021-6689189518918372830'
print(a[0:12])
print(a[12:])
print(len(a))