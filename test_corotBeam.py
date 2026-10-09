import numpy as np
from CorotBeam_with_TODO import beam2corot_Ke_and_Fe

"""
Testing of ceamCorot_Ke_and_Fe
"""

ex = np.array([0.0, 2.0])
ey = np.array([0.0, 0.0])
ep = np.array([210e9, 1e-3, 1e-6])

# DOFs are [u1, v1, rotation1, u2, v2, rotation2]
u = np.array([0.0, 0.0, 0.0, 0.001, 0.0, 0.0])

K, f_int = beam2corot_Ke_and_Fe(ex, ey, ep, u)

print("Internal force =", f_int)

# Axial stiffness is EA/L, so the force magnitude is 105,000 N.
expected_f_int = np.array([-105000.0, 0.0, 0.0, 105000.0, 0.0, 0.0])
np.testing.assert_allclose(f_int, expected_f_int, rtol=1e-8, atol=1e-8)
print("Axial-stretch test passed")

# K, f_int = beam2corot_Ke_and_Fe(ex, ey, ep, u)

# assert K.shape == (6, 6)
# assert f_int.shape == (6,)
# np.testing.assert_allclose(K, K.T)
# np.testing.assert_allclose(f_int, np.zeros(6), atol=1e-8)
# print("Single-element zero-displacement test passed")