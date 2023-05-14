# To calculate the resistance of the protection circuit

import math

Imax   = 40                                             # Continuous drain current in (A)
Itrip  = 2*Imax                                         # Trip current in A, twice Imax
Rds_on = 6e-3                                           # Drain-source resistance in Ohm
R_OCPA = 1e4*Itrip*Rds_on/math.fabs(3.3-Itrip*Rds_on)   # Protection resistance
