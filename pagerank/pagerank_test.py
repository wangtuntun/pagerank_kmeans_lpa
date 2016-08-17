
import sys
from pageRank import pageRank

links = [[]]

def read_file(filename):
    f = open(filename, 'r')
    for line in f:
        (frm, to) = map(int, line.split(" "))#python int max 2147483647
        # (frm, to) = map(long, line.split(" "))#python int max 2147483647
        extend = max(frm - len(links), to - len(links)) + 1
        for i in range(extend):
            links.append([])
        links[frm].append(to)
    f.close()

#read_file(sys.argv[1])
#read_file('all-tests.txt')
read_file('friend.txt')
pr =  pageRank(links, alpha=0.85, convergence=0.00001, checkSteps=10)
sum = 0
for i in range(len(pr)):
    print i, "=", pr[i]
    sum = sum + pr[i]
print "s = " + str(sum)


