import json

d = {"redjbot": "NDcxNzM4NDEyMTAyMTg5MDU3.Gzh0l4.AEn0USYMuiezVET3NQc6LBpYSZgEFbEpes1DMs", "redbot": 'OTgzODM4NjI1OTU3NTYwMzIw.G0xXT1.tcbl_2QVur_6FWSc3rvyAQ_XJ4Tu5WjZ_sXLSo', 'redbat': 'Nzk4MjY3MTM3MDIxNDQ0MTQ2.Gqe__j.biqAA2ZIONLeTMDXCjeo31Cjeo31q1fJnPUVUGLOnWyk'}
json.dump(d, open('tokens.txt', 'w'))

whip = json.load(open('tokens.txt'))
print (whip)
print (whip['redjbot'])
