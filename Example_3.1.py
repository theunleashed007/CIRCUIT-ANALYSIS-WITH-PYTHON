from PySpice.Logging.Logging import setup_logging
from PySpice.Spice.Netlist import Circuit

# Optional for this circuit
from PySpice.Unit import *

cct = Circuit('Example 3.1')

# Define circuit netlist
cct.R(1, 'v1', cct.gnd, 2)
cct.R(2, 'v1', 'v2', 4)
cct.R(3, 'v2', cct.gnd, 6)
cct.I(1, cct.gnd, 'v2', 10)
cct.I(2, 'v2', 'v1', 5)

simulator = cct.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.operating_point()

# Print result
for node in analysis.nodes.values():
    print(f'{node} = {round(float(node),4)}V')

# Run the code