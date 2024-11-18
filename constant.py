shift = 0.001
num_iterations = 600
error = 10**(-8)

def num_params_on_active_gates(active_gates):
    num_params = 0
    for i in range(0, len(active_gates), 3):
        num_params += (active_gates[i] + active_gates[i+1]) * 3
        num_params += active_gates[i + 2] * 1
    return int(num_params)

def num_params_on_active_blocks(active_blocks):
    num_params = 0
    for _ in range(0, len(active_blocks)):
        num_params += 6
    return int(num_params)