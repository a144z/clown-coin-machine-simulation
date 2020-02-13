import env
import random
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import batch_normalization
from statistics import mean, median
from collections import Counter

LR = 1e-3
goal_steps = 300
score_requirement = 0
initial_games = 100000
#
#score_requirement = 2000
#initial_games = 10000

def some_random_games_first():
    for episode in range(10):
        env.reset()
        for t in range(goal_steps):
            action = env.action_space()
            observation, reward, done, info = env.step(action)
            if done:
                break
#some_random_games_first()

def initial_population():
    training_data = []
    scores = []
    accepted_scores = []
    for _ in range(initial_games):
        env.reset()
        if(_%100==0):
            print(_)
        score=0
        game_memory=[]
        prev_observation = [0,0,0,0,0,0,0,0,0]
        for _ in range(goal_steps):
            #print(prev_observation)
            action = env.action_space()
            observation, reward, done, info = env.step(action)
            #print(action)

            if len(prev_observation) > 0:
                game_memory.append([prev_observation, action])

            prev_observation = observation
            score += reward
            if done:
                break
        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1] == 0:
                    output = [1,0,0,0,0,0,0,0]
                elif data[1] == 1:
                    output = [0,1,0,0,0,0,0,0]
                elif data[1] == 2:
                    output = [0,0,1,0,0,0,0,0]
                elif data[1] == 3:
                    output = [0,0,0,1,0,0,0,0]
                elif data[1] == 4:
                    output = [0,0,0,0,1,0,0,0]
                elif data[1] == 5:
                    output = [0,0,0,0,0,1,0,0]
                elif data[1] == 6:
                    output = [0,0,0,0,0,0,1,0]
                elif data[1] == 7:
                    output = [0,0,0,0,0,0,0,1]

                training_data.append([data[0], output])

        
        scores.append(score)

    training_data_save = np.array(training_data)
    np.save('saved2.npy',training_data_save)

    print('Average accepted score:', mean(accepted_scores))
    print('Median accepted score: ', median(accepted_scores))
    print(Counter(accepted_scores))

    return training_data
#initial_population()
def neural_network_model(input_size):
    network = input_data(shape=[None, input_size, 1], name='input')

    network = fully_connected(network, 32, activation='relu')
    network = batch_normalization(network)

    
    #network = fully_connected(network, 8, activation='relu')
    #network = dropout(network, 0.5)

    #network = fully_connected(network, 128, activation='relu')
    #network = dropout(network, 0.5)

    network = fully_connected(network, 8, activation='softmax')
    network = regression(network, optimizer='momentum', learning_rate=LR,
                         loss='categorical_crossentropy', name='targets')
    model = tflearn.DNN(network,tensorboard_dir='log')

    return model

def train_model(training_data, model=False):
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]), 1)
    y = [i[1] for i in training_data]

    if not model:
        #print("new_model")
        model = neural_network_model(input_size = len(X[0]))
        
    model.fit({'input':X}, {'targets':y}, n_epoch=1, snapshot_step=500, show_metric=True, run_id='openaistuff2')

    return model


#training_data = initial_population()
#training_data = np.load('saved2.npy')
#model = train_model(training_data)
#model.save("model2.model")
def test():
    training_data = np.load('saved2.npy')
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]), 1)
    model = neural_network_model(input_size = len(X[0]))
    
    model.load("model2.model")
    scores = []
    choices = []

    for each_game in range(1000):
        score = 0
        game_memory = []
        prev_obs = [0,0,0,0,0,0,0,0,0]
        env.reset()
        for _ in range(goal_steps):
            #if len(prev_obs) == 0:
            #    action = random.randrange(1,10)
            #else:
            action = np.argmax(model.predict(np.array(prev_obs).reshape(-1, len(prev_obs),1))[0])
            #if(action==9):
                #print(action)
            #print(prev_obs)
            print(action)
            choices.append(action)

            new_observation, reward, done, info = env.step(action)
            print(new_observation)
            prev_obs = new_observation
            game_memory.append([new_observation, action])
            score += reward
            if done:
                break
        scores.append(score)

    print('Average Score', sum(scores)/len(scores))
    print('Choice 0: {}, Choice 1: {}, Choice 2: {}, Choice 3: {}, Choice 4: {}, Choice 5: {}, Choice 6: {}, Choice 7: {}'.format(choices.count(0)/len(choices),choices.count(1)/len(choices),choices.count(2)/len(choices),choices.count(3)/len(choices),choices.count(4)/len(choices),choices.count(5)/len(choices),choices.count(6)/len(choices),choices.count(7)/len(choices)))
test()

