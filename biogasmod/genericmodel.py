from .waste import Waste


class Model():

    def __init__(self, q, m, l0, k, t0, t, tf):
        """ Generic model class for calculating biogas
        or methane generation rate over time, which can
        be classified into zero-order, first-order,
        second-order, with multiphase or single phase.

        -----
        Atributes :

            mass (float) representing the mass of waste in place (m),
                unit in mass
            methane_pot (float) representing the methane generation
                potential (l0), units of volume per mass (m3/Mg)
            gas_rate (float) first-order gas production rate constant (k)
                in reciprocal time
            lag_time (float)  time to methane generation start after
                disposal (t0) (years)
            time_waste (float)  age of the waste deposited, unit in
                time (t) (years)
            time_to_end (float): time to end-point of generation (tf)
            data_list (a dataframe of integers and floats) a dataframe
            of year and mass deposited extracted from the data file
        ------

        """

        Waste.__init__(self, m, l0, k)

        self.methane_gen = q
        self.lag_time = t0
        self.time_waste = t
        self.time_end = tf
