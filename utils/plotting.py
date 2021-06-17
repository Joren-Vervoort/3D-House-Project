import plotly.graph_objects as go #Used for 3D-Surface plot

class Plotting:

    def __init__(self, clipped_CHM):
        self.clipped_CHM = clipped_CHM
    
    def surface_plot_3d(self):
        
        """
        Function that will plot the Canopy Height Model (CHM) in 3D
        :attrib fig will contain go.Figure function
            - x-axis = latitude coordinates containing the polygon of the house
            - y-axis = longitude coordinates containing the polygon of the house
            - z-axis = heights given by the CHM
        This function will return the 3D plot of the house
        """
        
        fig = go.Figure(data=[go.Surface(x = self.clipped_CHM['x'],
                                         y = self.clipped_CHM['y'],
                                         z = self.clipped_CHM[0])])

        fig.update_layout(title='3D plot house',
                          scene = {"aspectratio": {"x": 1, "y": 1, "z": 0.5}})
        fig.show()