from simulation.workflow import Initial_Simulation
from workflow.workflow import Workflow
from scheduler.simplistic import Simplistic
from scheduler.random import Random
from scheduler.extreme import MaxResource, MinResource
from scheduler.genetic_algorithm import GeneticScheduler
import time


def run_scheduler(scheduler):
    start = time.time()
    scheduler.schedule()
    total_time, total_cost = scheduler.run()
    end = time.time()

    print('Total time {0}'.format(total_time))
    print('Total Cost {0}'.format(total_cost))
    print('Total Time {0}'.format(end - start))


sim = Initial_Simulation(50, [0.2, 0.3, 0.2, 0.2, 0.2], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]])
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

#time_asked = input('Time: ')
#cost_asked = input('Cost: ')

simplistic = Simplistic(0, 0, workflow) # First approach
print('\n\nSimple scheduling')

run_scheduler(simplistic)

#random = Random(time_asked, cost_asked, workflow)
#print('\n\nRandom scheduling')
#run_scheduler(random)
