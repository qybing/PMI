# a = 'https://restapi.amap.com/v3/place/text?citylimit=True&children=1&offset=25&extensions=all&page=27&city=110106&types=190403&key=b6ba73b213120eed85db66678a1f9981&key=8dbe9cda7de78e5e2f44cf1f9d385b15&key=8dbe9cda7de78e5e2f44cf1f9d385b15&key=b6ba73b213120eed85db66678a1f9981&key=ece61dac007323c2e972475ca77fa1dd&key=ee26a4ed76fa33fec419a556ccada055&key=8129c0f0cf3f25e1e0420804de9cb76d&key=20742e3615bee0c169383e7245a44589&key=ee26a4ed76fa33fec419a556ccada055&key=cba62d487805d2525402999bcd860c4e&key=5e4d54108b2b58990eba6eb73d57c1f3&key=94b18d5a91c3d9365662a3a51a0d6840&key=8dbe9cda7de78e5e2f44cf1f9d385b15&key=a6ab4d30847a531677a2448487a63866&key=a6ab4d30847a531677a2448487a63866&key=3d4b48ad3bb18c7535ecaffcbcc2e726&key=3525c904abfd01ebc1c453442e5d66f4&key=b6ba73b213120eed85db66678a1f9981&key=94b18d5a91c3d9365662a3a51a0d6840&key=3a3c8817d1ef04f5580ace5c6161f444&key=eacdbbef916eefaae53fa1a440ba562e&key=5e4d54108b2b58990eba6eb73d57c1f3&key=b6ba73b213120eed85db66678a1f9981&key=5e4d54108b2b58990eba6eb73d57c1f3&key=3a3c8817d1ef04f5580ace5c6161f444&key=d3f123123cab4948ad0e7f7df3401fdc'
# b = a.find('&key')
# print(a)
# print(a[0:b])
c = 'https://restapi.amap.com/v3/place/text?citylimit=True&children=1&offset=25&extensions=all&page=27&city=110106&types=190403'
d = c.find('&key')
if d>0:
    print(c[0:d])