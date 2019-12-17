from simulation.workflow import Initial_Simulation
from workflow.workflow import Workflow
from scheduler.simplistic import Simplistic
from scheduler.random import Random
from scheduler.extreme import MaxResource, MinResource
from scheduler.genetic_algorithm import GeneticScheduler
from scheduler.depth_scheduler import DepthScheduler
from scheduler.simplistic2 import Simplistic2
import matplotlib.pyplot as plt
import time
import numpy as np

colors = {
    'max resource': 'blue',
    'min resource': 'green',
    'simplistic 1': 'teal',
    'simplistic 2': 'orange',
    'depth': 'gold',
    'genetic': 'navy'
}

def run_simulation(number_points, distribution, connections, simulation_id):
    sim = Initial_Simulation(number_points, distribution, connections)
    points = []

    fig, ax = plt.subplots()
    plt.xlabel('Time')
    plt.ylabel('Cost')

    def run_scheduler(scheduler, label):
        if label is not 'genetic':
            scheduler.schedule()
        else:
            scheduler.schedule(ax)

        total_time, total_cost = scheduler.emulate()
        ax.scatter(total_time, total_cost, label=label, color=colors[label])
        print('Total time {0}'.format(total_time))
        print('Total Cost {0}'.format(total_cost))


    workflow = Workflow(sim.edges, sim.weights)

    maxResource = MaxResource(0, 0, workflow)
    print('\nMax Resource')
    run_scheduler(maxResource, 'max resource')

    minResource = MinResource(0, 0, workflow)
    print('\nMin Resource')
    run_scheduler(minResource, 'min resource')

    genetic = GeneticScheduler(0, 0, workflow)
    print('\nGenetic')

    run_scheduler(genetic, 'genetic')

    simplistic = Simplistic(0, 0, workflow) # First approach
    print('\n\nSimple scheduling')

    run_scheduler(simplistic, 'simplistic 1')

    depthScheduler = DepthScheduler(0, 0, workflow)
    print('\n\nDepth scheduling')
    run_scheduler(depthScheduler, 'depth')

    simplistic2 = Simplistic2(0, 0, workflow)
    print('\n\nSimplistic2 scheduling')
    run_scheduler(simplistic2, 'simplistic 2')

    ax.legend()
    ax.grid(True)
    fig.savefig('simulation_{0}.png'.format(simulation_id))

##
## Dif dist
##

run_simulation(200, [0.4, 0.3, 0.2, 0.1, 0.1], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_200_left')

run_simulation(100, [0.4, 0.3, 0.2, 0.1, 0.1], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_100_left')

run_simulation(50, [0.4, 0.3, 0.2, 0.1, 0.1], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_50_left')

run_simulation(20, [0.4, 0.3, 0.2, 0.1, 0.1], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_20_left')


run_simulation(200, [0.1, 0.1, 0.2, 0.3, 0.4], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_200_mid')

run_simulation(100, [0.1, 0.1, 0.2, 0.3, 0.4], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_100_mid')

run_simulation(50, [0.1, 0.1, 0.2, 0.3, 0.4], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_50_mid')

run_simulation(20, [0.1, 0.1, 0.2, 0.3, 0.4], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_20_mid')


run_simulation(200, [0.1, 0.2, 0.4, 0.2, 0.1], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_200_right')

run_simulation(100, [0.1, 0.2, 0.4, 0.2, 0.1], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_100_right')

run_simulation(50, [0.1, 0.2, 0.4, 0.2, 0.1], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_50_right')

run_simulation(20, [0.1, 0.2, 0.4, 0.2, 0.1], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]], 'n_20_right')


##
## Dif dist
##

run_simulation(200, [0.4, 0.3, 0.2, 0.1, 0.1], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_200_left')

run_simulation(100, [0.4, 0.3, 0.2, 0.1, 0.1], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_100_left')

run_simulation(50, [0.4, 0.3, 0.2, 0.1, 0.1], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_50_left')

run_simulation(20, [0.4, 0.3, 0.2, 0.1, 0.1], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_20_left')


run_simulation(200, [0.1, 0.1, 0.2, 0.3, 0.4], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_200_mid')

run_simulation(100, [0.1, 0.1, 0.2, 0.3, 0.4], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_100_mid')

run_simulation(50, [0.1, 0.1, 0.2, 0.3, 0.4], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_50_mid')

run_simulation(20, [0.1, 0.1, 0.2, 0.3, 0.4], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_20_mid')


run_simulation(200, [0.1, 0.2, 0.4, 0.2, 0.1], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_200_right')

run_simulation(100, [0.1, 0.2, 0.4, 0.2, 0.1], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_100_right')

run_simulation(50, [0.1, 0.2, 0.4, 0.2, 0.1], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_50_right')

run_simulation(20, [0.1, 0.2, 0.4, 0.2, 0.1], [[.1, .1, .1, .1], [.1, .1, .1], [.1, 0.1], [0.1]], 'm_20_right')
