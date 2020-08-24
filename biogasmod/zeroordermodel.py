import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as pltl
import seaborn as sns
from .genericmodel import Model


class ZeroOrder(Model):

    """ Zero-order model class for calculating and
    visualizing landfill biogas and methane production
    in cubic meters per year and cumulative in the time
    to end point of generation.

    -----
    Attributes:
        mass (float) representing the mass of waste in place,
                unit in mass
        methane_pot (float) representing the methane generation
            potential, units of volume per mass
        lag_time (float) time when methane generation starts
            time_waste (float) age of the waste deposited, unit in years
        data_list (list of floats) a list of floats of mass per year extracted
                from the data file
    -----

    """

    def __init__(self, q, m, l0, t0, t, tf):

        Model.__init__(self,  q, m, l0=100, t0=0.5, tf=15)

    def calculate_methanegen(self, m, t):
        """ Function to calculate methane generation rate
        in volume per time (m3/Mg). Uses a zero-order model,
        where the rate of methane production is constant,
        following the SWANA model:

        Q = M*L0/(t0-tf) , for t0 < t < tf

        Q = methane generation in volume per time
        M = waste deposited, mass
        L0 = methane generation potential, in volume per mass
        t0 = lag time
        tf = time to end point of generation


        Reference:
        Comparison of Models for Predicting Landfill Methane
        Recovery  Publication  #GR-LG  0075, The Solid Waste
        Association of North America (SWANA), 1998

        -----
        Args:
            None

        Returns:
            q (dataframe) methane generation in m3 per year, for year t
            and waste mass deposited m

        -----
        """

        #
        m = self.data["Waste(Mg)"]
        t = self.data["Year"]

        # t[Year) = pd.date_range(tz, periods=(tf+2), freq='A')

        min_range = min(t)
        max_range = pd.timedelta_range(min_range, periods=(tf + 2), freq="A")

        # Calculates the interval of time for evaluation
        interval = 1.0 * (max_range - min_range) / (len(self.data) + 2)

        q = pd.dataframe()
        t = pd.Dataframe()

        # Calculates methane generation rate per year:
        # qi = m*l0/(t0-t)

        # Calculate methane genearation rate:
        for i in range(interval):
            for j in m:
                tmp = 0 + interval * i
                t.append(tmp)
                q.append(j * l0 / (t0 - tmp))

        # Merge dataframes
        q = pd.concat([t, q], axis=1)

        return q

    def plot_methanegen_rate(self, tp=50):
        """Function to plot the methane generation rate of the data
        for a predetermined time period.

        Args:
            tp (int): number of years to plot

        Returns:
            list: x values for the waste plot (years)
            list: y values for the waste plot (methane generation rate)

        """
        self.time_periods = tp

        min_year = min(self.data["Year"])
        lag_years = tp - min_year
        max_range = pd.timedelta_range(min_year, periods=(tp - lag_years),
                                       freq="A")
        self.data["Year"] = max_range

        sns.set_style("whitegrid")
        g = sns.relplot(x="Year", y="Waste (Mg)", kind="line",
                        data=self.data).set_title('Waste deposition')
        g.fig.autofmt_xdate()
