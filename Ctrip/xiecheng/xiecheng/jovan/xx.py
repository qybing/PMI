import json
import re

a= '{"hotelid":"452197","amount":"988"},{"hotelid":"467314","amount":"998"},{"hotelid":"456474","amount":"1050"},{"hotelid":"374791","amount":"1068"},{"hotelid":"374801","amount":"718"},{"hotelid":"21785802","amount":"1449"},{"hotelid":"1641390","amount":"1388"},{"hotelid":"439311","amount":"1298"},{"hotelid":"7514902","amount":"588"},{"hotelid":"12052851","amount":"428"},{"hotelid":"535615","amount":"816"},{"hotelid":"939388","amount":"1888"},{"hotelid":"473871","amount":"932"},{"hotelid":"2231618","amount":"1011"},{"hotelid":"436066","amount":"506"},{"hotelid":"457112","amount":"758"},{"hotelid":"1602274","amount":"399"},{"hotelid":"6410223","amount":"1888"},{"hotelid":"445313","amount":"686"},{"hotelid":"608345","amount":"858"},{"hotelid":"13598382","amount":"617"},{"hotelid":"1836273","amount":"873"},{"hotelid":"14131570","amount":"714"},{"hotelid":"845507","amount":"808"},{"hotelid":"482534","amount":"888"}'
print(a)
b = a[1:-1].split('},{')
for i in b:
    c = re.findall('"hotelid":"(\d+)","amount":"(\d+)"',i)
    print(c[0][0],c[0][1])