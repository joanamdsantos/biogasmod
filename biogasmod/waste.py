import math
import pandas as pd

class Waste():
    
    def __init__(self, m, l0, k, mean, stdv):
    
        """ Class for characterizing waste deposited in the landfill,
        in terms of mass deposited per year, mean and standard deviation,
        methane generation potential (l0) values, gas rate production values
        (k) and plotting waste deposition over time.
        
         Atributes :
            
            mass (float) representing the mass of waste in place (m),
                unit in mass
            methane_pot (float) representing the methane generation 
                potential (l0), units of volume per mass (m3/Mg)
            gas_rate (float) first-order gas production rate constant (k)
                in reciprocal time
            
        """
        self.mass = m
        self.methane_pot = l0
        self.gas_rate = k
        self.data = pd.dataframe()
        self.mean = mean
        self.stdev = stdev
        
    def read_data_file(self, file_name):
   
        """Function to read in data from a csv file, using the comma delimeter. 
       The csv file should have two columnns, the first with the years of waste 
       deposition and the other with the corresponding mass deposited in each in Mg. 
       The numbers are stored in the data attribute.
               
        Args:
            file_name (string) name of a file to read from
        
        Returns:
            None
        
        """
            
        data_waste = pd.read_csv(filepath_or_buffer=file_name, index_col = 0, sep=',')
        data_waste.columns =[Year, Waste (Mg)]
    
        self.data = data_waste
    
    def calculate_mean(self):
        
        """ Function to calculate the mean of the waste deposited per year.
        
        Args:
            None
            
        Returns:
            float: mean of waste deposited per year
            
        """
        
        avg = sum(self.data[Waste (Mg)])/len(self.data)
        
        return self.mean
    
   
    def calculate_stdev(self):
        
        """ Function to calculate the standard deviation of the waste deposited per year.
        
        Args:
            None
            
        Returns:
            float: standard deviation of the waste deposited per year
            
        """
        
        #calculate mean:
        mean = self.calculate_mean()
        
        #number of years of deposition
        n = len(self.data)
        
        stdev = 0
        
        for w in self.data[[Waste (Mg)]:
            stdev += (w - mean) ** 2
        
        stdev = math.sqrt(stdev / n)
        
        return self.stdev


    def plot_data(self, t=30):
    
        """ Function to plot the waste yearly waste deposition data.
        
        Args:
            t (integer): number of years to plot
            
        Returns:
            None
            
        """
               
        #t[Year) = pd.date_range(tz, periods=(tf+2), freq='A')
    
        min_range = min(self.data["Year"])
        max_range= pd.timedelta_range(min_range, periods=(t), freq="A")
        self.data["Year"] = max_range
        
        sns.set_style("whitegrid")
        g = sns.relplot(x="Years", y="Waste (Mg)", kind="line", data=self.data).set_title('Waste deposition')
        g.fig.autofmt_xdate()
       
   