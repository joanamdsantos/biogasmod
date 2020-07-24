class Model:
    def __init__(self, M, L0, t0, t)
    
        """ Generic model class for calculating biogas
        or methane generation rate over time, which can
        be classified into zero-order, first-order,
        second-order, with multiphase or single phase.

        -----
        Atributes :
            mass (float) representing the mass of waste in place,
                unit in mass
            methane_pot (float) representing the methane generation 
                potential, units of volume per mass
            lag_time (float) time when methane generation starts
            time_waste (float) age of the waste deposited, unit in years
            data_list (list of floats) a list of floats of mass per year extracted
                from the data file
        ------

        """

        self.mass = M
        self.methane_pot = L0
        self.lag_time = t0
        self.time_waste = t
        self.data = []
    
    def read_data_file(self, file_name):
   
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
               
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
            
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
        self.data = data_list
