import spinsim
import numpy as np
import matplotlib.pyplot as plt

def get_field_larmor(time_sample, field_modifier, field_sample):
   field_sample[0] = 0            # Zero field in x direction
   field_sample[1] = 0            # Zero field in y direction
   field_sample[2] = 1000         # Split spin z eigenstates by 1kHz

simulator_larmor = spinsim.Simulator(get_field_larmor, spinsim.SpinQuantumNumber.HALF, exponentiation_method = spinsim.ExponentiationMethod.LIE_TROTTER)

state_init = np.asarray([1/np.sqrt(2), 1/np.sqrt(2)], np.cdouble)

results_larmor = simulator_larmor.evaluate(0, 0e-3, 100e-3, 100e-9, 500e-9, state_init)

plt.figure()
plt.plot(results_larmor.time, results_larmor.spin)
plt.legend(["x", "y", "z"])
plt.xlim(0e-3, 2e-3)
plt.xlabel("time (s)")
plt.ylabel("spin expectation (hbar)")
plt.title("Spin projection for Larmor precession")
plt.show()

import spinsim
import numpy as np
import matplotlib.pyplot as plt
import math

def get_field_rabi(time_sample, field_modifier, field_sample):
   # Dress atoms from the x direction, Rabi flopping at 1kHz
   field_sample[0] = 2000*math.cos(math.tau*20e3*field_modifier*time_sample)
   field_sample[1] = 0                        # Zero field in y direction
   field_sample[2] = 20e3*field_modifier     # Split spin z eigenstates by 700kHz
   field_sample[3] = 0                        # Zero quadratic shift, found in spin one systems

simulator_rabi = spinsim.Simulator(get_field_rabi, spinsim.SpinQuantumNumber.ONE)

state_init = np.asarray([1, 0, 0], np.cdouble)

result0 = simulator_rabi.evaluate(1, 0e-3, 100e-3, 100e-9, 500e-9, state_init)

plt.figure()
plt.plot(result0.time, result0.spin)
plt.legend(["x", "y", "z"])
plt.xlim(0e-3, 2e-3)
plt.xlabel("time (s)")
plt.ylabel("spin expectation (hbar)")
plt.title("Spin projection for Rabi flopping")
plt.show()

result1 = simulator_rabi.evaluate(2, 0e-3, 100e-3, 100e-9, 500e-9, state_init)

plt.figure()
plt.plot(result1.time, result1.spin)
plt.legend(["x", "y", "z"])
plt.xlim(0e-3, 2e-3)
plt.xlabel("time (s)")
plt.ylabel("spin expectation (hbar)")
plt.title("Spin projection for Rabi flopping")
plt.show()