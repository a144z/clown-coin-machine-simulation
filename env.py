import numpy
import random
global array
array=[0,0,0,0,0,0,0,0,0]
global coin
coin=176
def reset():
    global array
    array=[0,0,0,0,0,0,0,0,0]

def count_array(array):
    counter=0
    reward_counter=[]
    for each in array:
        if each==1:
            counter+=1
        elif counter!=0:
            reward_counter.append(counter)
            counter=0
    reward_counter.sort()
    return reward_counter

def claim_or_not(array):
    for element in array:
        if element!=1:
            return True
    return False
def claim(array):
    if array==[2] or array==[1,2] or array==[1,1,2]:
        return 20
    elif array==[3] or array==[1,3] or array==[1,1,3]:
        return 30
    elif array==[4] or array==[1,4]:
        return 100
    elif array==[5] or array==[1,5]:
        return 300
    elif array==[6]:
        return 600
    elif array==[7]:
        return 1200
    elif array==[2,2] or array==[1,2,2]:
        return 40
    elif array==[2,3]:
        return 50
    elif array==[2,4]:
        return 120
    elif array==[3,3]:
        return 60
        
def step(action):
    if action==0:
        val = numpy.random.choice(numpy.arange(1, 6), p=[14/70, 28/70, 20/70, 7/70, 1/70])
    elif action==1:
        val = numpy.random.choice(numpy.arange(1, 7), p=[14/112, 34/112, 35/112, 21/112, 7/112, 1/112])
    elif action==2:
        val = numpy.random.choice(numpy.arange(1, 8), p=[6/126, 21/126, 35/126, 35/126, 21/126, 7/126, 1/126])
    elif action==3:
        val = numpy.random.choice(numpy.arange(1, 9), p=[1/128, 7/128, 21/128, 35/128, 35/128, 21/128, 7/128, 1/128])
    elif action==4:
        val = numpy.random.choice(numpy.arange(2, 10), p=[1/128, 7/128, 21/128, 35/128, 35/128, 21/128, 7/128, 1/128])
    elif action==5:
        val = numpy.random.choice(numpy.arange(3, 10), p=[1/126, 7/126, 21/126, 35/126, 35/126, 21/126, 6/126])
    elif action==6:
        val = numpy.random.choice(numpy.arange(4, 10), p=[1/112, 7/112, 21/112, 35/112, 34/112, 14/112])
    elif action==7:
        val = numpy.random.choice(numpy.arange(5, 10), p=[1/70, 7/70, 20/70, 28/70, 14/70])


            
        ##else:
        ##    print("NO REWARD")
    if array[val-1]!=0:
        ##print("game lost")
        reset()
        return array, 0, True , 0
    elif val > 1 and val < 9:
        array[val-1]=1
        reward_counter = count_array(array)
        if (claim_or_not(reward_counter)):
            reward=claim(reward_counter)
            #print("GET REWARD: "+str(reward))
            return array, reward, False , 0
    return array, 0, False , 0
    ##else:
    ##    print("lucky draw: "+ str(val))
    ##print(array)
    
def action_space():
    action = random.randrange(0, 8)
    return action
def main():
    for episode in range(100):
        reset()
        observation=[0,0,0,0,0,0,0,0,0]
        for t in range(100):
            action = int(input("enter: "))
            global coin
            coin-=1
            observation, reward, done, info = step(action)
            print(observation)
            #print(reward/10)
            coin+=(reward/10)
            print(coin)
            if done:
                break
main()
