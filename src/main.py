from simulation.workflow import Initial_Simulation
from simulation.executer import Executor
from workflow.workflow import Workflow

sim = Initial_Simulation(50, [0.2, 0.3, 0.2, 0.2, 0.2], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]])
workflow = Workflow(sim.edges, sim.weights)
executer = Executor()
resources = executer.init()

policy = {x: 0 for x in range(0, workflow.size)}

executer.run(workflow, resources, policy)
