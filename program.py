import random as rd

def flip_a_coin():
    return rd.randint(0,1)

head = 0
tail = 0
spins = 10
#Start with spins at 10 and then add a zero and rerun and see how the difference between heads vs tails changes as you increase spins


for i in range(spins):
    num = flip_a_coin()
    if(num == 0):
        head += 1 #0 represents a head
    else:
        tail +=1 #1 respresents a tail


#print(head)
#print(tail)

difference = head-tail
percent_diff = abs(difference/spins) * 100
print(percent_diff)