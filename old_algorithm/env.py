import numpy
import random
import solution
global episode_counter
episode_counter=0
global total_coin_count_array
total_coin_count_array=[0,0,0,0,0,0,0,0]
global array
array=[0,0,0,0,0,0,0,0,0]
global coin
coin=0
global credit
credit=0
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
        return 24
    elif array==[3] or array==[1,3] or array==[1,1,3]:
        return 36
    elif array==[4] or array==[1,4]:
        return 120
    elif array==[5] or array==[1,5]:
        return 360
    elif array==[6]:
        return 720
    elif array==[7]:
        return 3500
    elif array==[2,2] or array==[1,2,2]:
        return 48
    elif array==[2,3]:
        return 60
    elif array==[2,4]:
        return 144
    elif array==[3,3]:
        return 72
        
##def claim(array):
##    if array==[2] or array==[1,2] or array==[1,1,2]:
##        return 20
##    elif array==[3] or array==[1,3] or array==[1,1,3]:
##        return 30
##    elif array==[4] or array==[1,4]:
##        return 100
##    elif array==[5] or array==[1,5]:
##        return 300
##    elif array==[6]:
##        return 600
##    elif array==[7]:
##        return 1700
##    elif array==[2,2] or array==[1,2,2]:
##        return 40
##    elif array==[2,3]:
##        return 50
##    elif array==[2,4]:
##        return 120
##    elif array==[3,3]:
##        return 60
    
##if action!=9 and action!=1 and action!=8:
##    action+=random.randrange(-1, 2)
##    
##if action!=9:
##        if action==8:
##            action+=random.randrange(-1, 1)
##        elif action==1:
##            action+=random.randrange(0, 2)
##        else:
##            action+=random.randrange(-1, 2)
prob=[451, 343, 251, 139, 61, 37, 10, 5]
prob2=[771, 143, 81, 89, 36, 22, 10, 5]
print(prob)
prob[0]+=320
prob[1]-=200
prob[2]-=170
prob[3]-=50
prob[4]-=25
prob[5]-=15
total=[0,0,0,0]
for i in range(4):
    for k in range(8):
        total[i]+=prob[abs(7-i-k)]
print(total)
print(prob)

def defract(action):
    if action==1:
        val = numpy.random.choice(numpy.arange(0, 8), p=[prob[0]/total[0],prob[1]/total[0],prob[2]/total[0],prob[3]/total[0],prob[4]/total[0],prob[5]/total[0],prob[6]/total[0],prob[7]/total[0]])
    elif action==2:
        val = numpy.random.choice(numpy.arange(-1,7), p=[prob[1]/total[1],prob[0]/total[1],prob[1]/total[1],prob[2]/total[1],prob[3]/total[1],prob[4]/total[1],prob[5]/total[1],prob[6]/total[1]])
    elif action==3:
        val = numpy.random.choice(numpy.arange(-2,6), p=[prob[2]/total[2],prob[1]/total[2],prob[0]/total[2],prob[1]/total[2],prob[2]/total[2],prob[3]/total[2],prob[4]/total[2],prob[5]/total[2]])
    elif action==4:
        val = numpy.random.choice(numpy.arange(-3,5), p=[prob[3]/total[3],prob[2]/total[3],prob[1]/total[3],prob[0]/total[3],prob[1]/total[3],prob[2]/total[3],prob[3]/total[3],prob[4]/total[3]])
    elif action==5:
        val = numpy.random.choice(numpy.arange(-4,4), p=[prob[4]/total[3],prob[3]/total[3],prob[2]/total[3],prob[1]/total[3],prob[0]/total[3],prob[1]/total[3],prob[2]/total[3],prob[3]/total[3]])
    elif action==6:
        val = numpy.random.choice(numpy.arange(-5,3), p=[prob[5]/total[2],prob[4]/total[2],prob[3]/total[2],prob[2]/total[2],prob[1]/total[2],prob[0]/total[2],prob[1]/total[2],prob[2]/total[2]])
    elif action==7:
        val = numpy.random.choice(numpy.arange(-6,2), p=[prob[6]/total[1],prob[5]/total[1],prob[4]/total[1],prob[3]/total[1],prob[2]/total[1],prob[1]/total[1],prob[0]/total[1],prob[1]/total[1]])
    elif action==8:
        val = numpy.random.choice(numpy.arange(-7,1), p=[prob[7]/total[0],prob[6]/total[0],prob[5]/total[0],prob[4]/total[0],prob[3]/total[0],prob[2]/total[0],prob[1]/total[0],prob[0]/total[0]])
    return action+val


def step(action):
    global total_coin_count_array
    global episode_counter

##    if action!=9:
##        prob=random.randrange(0,4)
##        if prob!=0:
##            action+=random.randrange(-2, 3)
##            if action>8:
##                action=16-action
##            elif action<1:
##                action=2-action
    if action!=9:
##        if action==2:
##            action=1
##        if action==7:
##            action=8
##        if action==3:
##            action=2
##        if action==6:
##            action=7
        
        action=defract(action)

    
    if action==1:
        val = numpy.random.choice(numpy.arange(1, 6), p=[14/70, 28/70, 20/70, 7/70, 1/70])
    elif action==2:
        val = numpy.random.choice(numpy.arange(1, 7), p=[14/112, 34/112, 35/112, 21/112, 7/112, 1/112])
    elif action==3:
        val = numpy.random.choice(numpy.arange(1, 8), p=[6/126, 21/126, 35/126, 35/126, 21/126, 7/126, 1/126])
    elif action==4:
        val = numpy.random.choice(numpy.arange(1, 9), p=[1/128, 7/128, 21/128, 35/128, 35/128, 21/128, 7/128, 1/128])
    elif action==5:
        val = numpy.random.choice(numpy.arange(2, 10), p=[1/128, 7/128, 21/128, 35/128, 35/128, 21/128, 7/128, 1/128])
    elif action==6:
        val = numpy.random.choice(numpy.arange(3, 10), p=[1/126, 7/126, 21/126, 35/126, 35/126, 21/126, 6/126])
    elif action==7:
        val = numpy.random.choice(numpy.arange(4, 10), p=[1/112, 7/112, 21/112, 35/112, 34/112, 14/112])
    elif action==8:
        val = numpy.random.choice(numpy.arange(5, 10), p=[1/70, 7/70, 20/70, 28/70, 14/70])
    elif action==9:
        reward_counter = count_array(array)
        #print("reward_CHOOSEN!!!\n")
        if (claim_or_not(reward_counter)):
            reward=claim(reward_counter)
            total_coin_count_array[episode_counter]+=1
            episode_counter=0
            reset()
            #print("GET REWARD: "+str(reward))
            return array, reward, True , 0
            
        ##else:
        ##    print("NO REWARD")
    if action!=9:
        global coin
        coin-=1
        if array[val-1]!=0:
            #print("game lost")
            total_coin_count_array[episode_counter]+=1
            episode_counter=0
            reset()
            return array, 0, True , 0
        elif val > 1 and val < 9:
            array[val-1]=1
            episode_counter+=1
        ##else:
        ##    print("lucky draw: "+ str(val))
    ##print(array)
    return array, 0, False , 0
def action_space():
    reward_counter = count_array(array)
    if (claim_or_not(reward_counter)):
        action = random.randrange(1, 10)
        
    else:
        action = random.randrange(1, 9)
    return action

def main():
    count_reward=[0,0,0,0,0,0,0,0,0,0]
    for episode in range(1000001):
        reset()
        observation=[0,0,0,0,0,0,0,0,0]
        if episode%10000==0:
            global coin
            global credit
            print("Coin: "+ str(coin)+"\n")
            print("Credit: "+ str(credit)+"\n")
        counter=0
        for t in range(1000000):
            #action = int(input("enter: "))
            action = solution.best_solution(observation)
            #if action!=9:
            #    action=action_space()
            #print(action)
            
            observation, reward, done, info = step(action)
            if reward==24:
               count_reward[0]+=1
            elif reward==36:
                count_reward[1]+=1
            elif reward==120:
                count_reward[2]+=1
            elif reward==360:
                count_reward[3]+=1
            elif reward==720:
                count_reward[4]+=1
            elif reward==3500:
                count_reward[5]+=1
            elif reward==48:
                count_reward[6]+=1
            elif reward==60:
                count_reward[7]+=1
            elif reward==144:
                count_reward[8]+=1
            elif reward==72:
                count_reward[9]+=1
            #print(observation)
            #print(reward/10)
            
            credit+=reward
            #print("Coin: "+ str(coin)+"\n")
            if done:
                break
    print(total_coin_count_array)
    print(count_reward)
main()

