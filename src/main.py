from simulation.workflow import Initial_Simulation
from workflow.workflow import Workflow
from scheduler.simplistic import Simplistic
from scheduler.random import Random
from scheduler.extreme import MaxResource, MinResource
from scheduler.genetic_algorithm import GeneticScheduler
from scheduler.depth_scheduler import DepthScheduler
from scheduler.simplistic2 import Simplistic2
import time


def run_scheduler(scheduler):
    scheduler.schedule()
    total_time, total_cost = scheduler.emulate()

    print('Total time {0}'.format(total_time))
    print('Total Cost {0}'.format(total_cost))


sim = Initial_Simulation(100, [0.4, 0.3, 0.2, 0.1, 0.1], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]])
workflow = Workflow(sim.edges, sim.weights)

maxResource = MaxResource(0, 0, workflow)
print('\nMax Resource')
run_scheduler(maxResource)

minResource = MinResource(0, 0, workflow)
print('\nMin Resource')
run_scheduler(minResource)

genetic = GeneticScheduler(0, 0, workflow)
print('\nGenetic')

run_scheduler(genetic)

simplistic = Simplistic(0, 0, workflow) # First approach
print('\n\nSimple scheduling')

run_scheduler(simplistic)

depthScheduler = DepthScheduler(0, 0, workflow)
print('\n\nDepth scheduling')
run_scheduler(depthScheduler)

simplistic2 = Simplistic2(0, 0, workflow)
print('\n\nSimplistic2 scheduling')
run_scheduler(simplistic2)
