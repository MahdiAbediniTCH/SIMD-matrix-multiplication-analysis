import matplotlib.pyplot as plt

import struct

MAX_N = 1024
N_RESULTS = MAX_N // 4
TRIM = 1
LAST_IND = N_RESULTS - TRIM
def read_results(file_name):

    with open(file_name, "rb") as file:
        data = file.read()

    num_doubles = N_RESULTS
    format_string = f"{num_doubles}d"

    return list(struct.unpack(format_string, data))


input_sizes = list(range(4, MAX_N + 1 - 4 * TRIM, 4)) # trim the last entry
rt_gcc_o0 = read_results("data_1024/results_gcc_O0.bin")[:LAST_IND]
rt_cache_o0 = read_results("data_1024/results_cache_efficient_gcc_O0.bin")[:LAST_IND]
rt_gcc_o3 = read_results("data_1024/results_gcc_O3.bin")[:LAST_IND]
rt_cache_o3 = read_results("data_1024/results_cache_efficient_gcc_O3.bin")[:LAST_IND]
rt_asm = read_results("data_1024/results_asm_matrix_mul.s.bin")[:LAST_IND]
rt_cache_asm = read_results("data_1024/results_asm_matrix_mul_cache_efficient.s.bin")[:LAST_IND]
rt_asm_simd = read_results("data_1024/results_simd_matrix_mul.s.bin")[:LAST_IND]

# Check that the lists are all the same length
assert len(input_sizes) == len(rt_gcc_o0) == len(rt_gcc_o3) == len(rt_asm)

# Set the plot style
plt.style.use('seaborn-v0_8-whitegrid')

# Create the plot
fig, ax = plt.subplots()

# Define modern color palette
colors = ['#002cb1', '#1884bb', '#7923b0', '#029c6e']


# Plot the runtimes with distinct styles (without markers)
ax.plot(input_sizes, rt_gcc_o0, color=colors[0], alpha=0.3, label='GCC -O0')
ax.plot(input_sizes, rt_cache_o0, color=colors[0], label='GCC -O0 cache efficient')
ax.plot(input_sizes, rt_gcc_o3, color=colors[1], alpha=0.3, label='GCC -O3')
ax.plot(input_sizes, rt_cache_o3, color=colors[1], label='GCC -O3 cache efficient')
ax.plot(input_sizes, rt_asm, color=colors[2], alpha=0.3, label='Linear assembly')
ax.plot(input_sizes, rt_cache_asm, color=colors[2], label='Linear assembly cache efficient')
ax.plot(input_sizes, rt_asm_simd, color=colors[3], label='SIMD assembly')

# Add shadow effect
# ax.fill_between(input_sizes, rt_gcc_o0, alpha=0.5, color=colors[0])
# ax.fill_between(input_sizes, rt_gcc_o3, alpha=0.5, color=colors[1])
# ax.fill_between(input_sizes, rt_asm, alpha=0.5, color=colors[2])
# ax.fill_between(input_sizes, rt_asm_simd, alpha=0.3, color=colors[3])

# Add titles and labels
ax.set_title('Runtime of functions (Average of 5 runs)', fontsize=15)
ax.set_xlabel('Matrix dimension (n)', fontsize=12)
ax.set_ylabel('Runtime', fontsize=12)

# Add a legend
ax.legend()

# Display the plot
plt.show()
