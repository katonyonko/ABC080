from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="080"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,C=map(int,input().split())
  d=[[] for _ in range(C)]
  time=[0]*(10**5)
  for i in range(N):
    s,t,c=map(int,input().split())
    s-=1; t-=1
    d[c-1].append([s,t])
  for i in range(C):
    d[i].sort()
    for j in range(len(d[i])):
      s,t=d[i][j]
      for k in range(s,t):
        time[k]+=1
      if j ==len(d[i])-1 or t!=d[i][j+1][0]:
        time[t]+=1
  print(max(time))
  """ここから上にコードを記述"""

  print(test_case[__+1])