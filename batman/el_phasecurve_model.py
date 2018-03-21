class Planetary_System_Parameters():
    """
        Object to store the physical parameters of the transiting planetary system. Based on Kreidberg's batman.TransitParams

        :param t0: Time of inferior conjunction. 
        :type t0: float, optional 

        :param t_secondary: Time of secondary eclipse center.
        :type t_secondary: float, optional 

        :param per: Orbital period.
        :type per: float

        :param rp: Planet radius [in stellar radii].
        :type rp: float

        :param a: Semi-major axis [in stellar radii].
        :type a: float

        :param inc: Orbital inclination [in degrees].
        :type inc: float

        :param ecc: Orbital eccentricity.
        :type ecc: float

        :param w: Argument of periapse [in degrees]
        :type w: float

        :param u: List of limb darkening coefficients.
        :type u: array_like 

        :param limb_dark: Limb darkening model (choice of "nonlinear", "quadratic", "exponential", "logarithmic", "squareroot", "linear", "uniform", "power2", or "custom").
        :type limb_dark: str

        :param fp: Planet-to-star flux ratio (for secondary eclipse models).
        :type fp: float, optional

        .. note::  
                - Units for the orbital period and ephemeris can be anything as long as they are consistent (e.g. both in days). 
                - The orbital path is calculated based on `t0` for primary transits and `t_secondary` for secondary eclipses.

        :Example:
        
        >>> import batman
        >>> params = batman.TransitParams()
        >>> params.t0 = 0.                              #time of inferior conjunction
        >>> params.per = 1.                             #orbital period 
        >>> params.rp = 0.1                             #planet radius (in units of stellar radii)
        >>> params.a = 15.                              #semi-major axis (in units of stellar radii)
        >>> params.inc = 87.                            #orbital inclination (in degrees)       
        >>> params.ecc = 0.                             #eccentricity   
        >>> params.w = 90.                              #longitude of periastron (in degrees) 
        >>> params.u = [0.1, 0.3]                       #limb darkening coefficients
        >>> params.limb_dark = "quadratic"              #limb darkening model
    """

    from .transitmodel import TransitParams
    def __init__(self):
        TransitParams.__init__()
