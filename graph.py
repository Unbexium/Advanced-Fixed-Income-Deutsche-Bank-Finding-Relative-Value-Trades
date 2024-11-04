import numpy as np
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_key_rate_durations(df, key_rate_durations, weight):


    fig = go.Figure(
        go.Bar(
            x=df['Time to Maturity'],
            y=key_rate_durations,
            marker=dict(color='rgb(0, 71, 102)', line=dict(color='black', width=1)),
            width=0.5,
            name='Key Rate Duration'
        )
    )

    fig.update_layout(
        title='Key Rate Durations of the Portfolio for a shock of 50bps in function of shocked maturity',
        plot_bgcolor='rgba(255,255,255,1)',
        title_x=0.5,
        width=900,
        height=500,
        xaxis_title="Shocked Maturity",
        yaxis_title="Key Rate Duration $",
        font=dict(
            family="Times New Roman",
            size=15,
            color="Black"
        ),
        xaxis=dict(
            showline=True,
            linewidth=1,
            linecolor='black',
            tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25],
        ),
        yaxis=dict(
            showline=True,
            linewidth=1,
            linecolor='Grey',
            gridcolor="rgba(38,38,38,0.15)"
        )
    )

    fig.show()



def plot_yield_difference(maturity_range, yield_difference):
    
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=maturity_range,
            y=yield_difference, 
            mode='lines',
            name='Yield Difference (Shocked - Original)',
            line=dict(color='rgb(2, 130, 2)'),
        )
    )

    fig.add_shape(
        type="line",
        x0=10,
        y0=min(yield_difference),
        x1=10,
        y1=max(yield_difference),
        line=dict(color="gray", dash="dash"),
        name="10-Year Maturity"
    )


    fig.update_layout(
        title='Difference in Yield Curve After 50bps Shock at 10-Year Maturity',
        plot_bgcolor='rgba(255,255,255,1)',
        title_x=0.5,
        width=900,
        height=500,
        xaxis_title="Time to Maturity (Years)",
        yaxis_title="Yield Difference (bps)",

        font=dict(
            family="Times New Roman",
            size=15,
            color="Black"
        ),

        xaxis=dict(
            showline=True, 
            linewidth=1, 
            linecolor='black',
            range=[0, max(maturity_range)],
            ticks="inside",
            tickson="boundaries",
            ticklen=5,
            tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25]
        ),

        yaxis=dict(
            showline=True, 
            linewidth=1, 
            linecolor='Grey',
            gridcolor="rgba(38,38,38,0.15)",
            zeroline=True,               
            zerolinewidth=1,              
            zerolinecolor="black",
            range=[-10, 55] 
        ),
        legend=dict(
            yanchor="top",
            xanchor="left",
            bgcolor='rgba(255,255,255,1)'
        )
    )

    fig.show()

def plot_shocked_vs_original_yields(DataKRD, original_zero_coupon_yields, zero_coupon_yields_shocked, maturity_range, original_yields_interp, shocked_yields_interp):
    
    fig = go.Figure()

    # Plot the original yield curve as a line
    fig.add_trace(
        go.Scatter(
            x=maturity_range,
            y=original_yields_interp * 100,  # Convert to percentage
            mode='lines',
            name='Original interpolate Yield Curve',
            line=dict(color='rgb(0, 71, 102)')
        )
    )

    # Plot the shocked yield curve as a line
    fig.add_trace(
        go.Scatter(
            x=maturity_range,
            y=shocked_yields_interp * 100,  # Convert to percentage
            mode='lines',
            name='Shocked Yield Curve (+50bps at 10Y)',
            line=dict(color='red')
        )
    )

    # Scatter plot for original zero-coupon yields
    fig.add_trace(
        go.Scatter(
            x=DataKRD['Time to Maturity'],
            y=original_zero_coupon_yields * 100,  # Convert to percentage
            mode='markers',
            showlegend=False,
            marker=dict(size=8, color='rgb(0, 71, 102)')
        )
    )

    # Scatter plot for shocked zero-coupon yields
    fig.add_trace(
        go.Scatter(
            x=DataKRD['Time to Maturity'],
            y=zero_coupon_yields_shocked * 100,  # Convert to percentage
            mode='markers',
            showlegend=False,
            marker=dict(size=8, color='red')
        )
    )

    # Layout settings
    fig.update_layout(

        title='Impact of 50bps Shock at 10-Year Maturity on Yield Curve',
        plot_bgcolor='rgba(255,255,255,1)',
        title_x=0.5,
        width=900,
        height=500,
        xaxis_title="Time to Maturity (Years)",
        yaxis_title="Yield (%)",

        font=dict(
            family="Times New Roman",
            size=15,
            color="Black"
        ),

        xaxis=dict(
            showline=True, 
            linewidth=1, 
            linecolor='black',
            range=[0, 22],
            ticks="inside",
            tickson="boundaries",
            ticklen=5,
            tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25]
        ),

        yaxis=dict(
            showline=True, 
            linewidth=1, 
            linecolor='Grey',
            gridcolor="rgba(38,38,38,0.15)"
        ),

        legend=dict(
            yanchor="top",
            xanchor="left",
            bgcolor='rgba(255,255,255,0)'
        )
    )

    # Display the plot
    fig.show()



def plot_yield_contributions(t_plot, contribution1, contribution2, contribution3, contribution4, y_model_plot):
    
    fig = go.Figure()
    
    color1 = 'rgb(0, 71, 102)'  
    color2 = 'red'              
    color3 = 'rgb(153, 100, 50)' 
    color4 = 'rgb(2, 130, 2)'    
    color_total = 'black'        

    fig.add_trace(go.Scatter(x=t_plot, y=contribution1 * 100, mode='lines', name='Level Contribution', line=dict(color=color1)))
    fig.add_trace(go.Scatter(x=t_plot, y=contribution2 * 100, mode='lines', name='Slope Contribution', line=dict(color=color2)))
    fig.add_trace(go.Scatter(x=t_plot, y=contribution3 * 100, mode='lines', name='Curvature 1 Contribution', line=dict(color=color3)))
    fig.add_trace(go.Scatter(x=t_plot, y=contribution4 * 100, mode='lines', name='Curvature 2 Contribution', line=dict(color=color4)))
    
    fig.add_trace(go.Scatter(x=t_plot, y=y_model_plot * 100, mode='lines', name='Total Model Yield', line=dict(color=color_total, dash='dash')))

    fig.update_layout(
        title='Contributions from Each Factor to the Yield Curve',
        xaxis_title='Time to Maturity (Years)',
        yaxis_title='Yield Contribution (%)',
        plot_bgcolor='rgba(255,255,255,1)',
        title_x=0.5,
        width=1000,
        font=dict(
            family="Times New Roman",
            size=15,
            color="Black"
        ),
        xaxis=dict(
            showline=True, 
            linewidth=1, 
            linecolor='black',
            range=[0, 27],
            ticks="inside",
            tickson="boundaries",
            ticklen=5,
            tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25]
        ),
        yaxis=dict(
            showline=True, 
            linewidth=1, 
            linecolor='Grey',
            gridcolor="rgba(38,38,38,0.15)"
        ),
        legend=dict(
            yanchor="top",
            bgcolor='rgba(255,255,255,0)'
        )
    )
    
    fig.show()



def plot_factor_loadings(t_plot, loading1, loading2, loading3, loading4):

    fig = go.Figure()
    
    color1 = 'rgb(0, 71, 102)' 
    color2 = 'red'    
    color3 = 'rgb(153, 100, 50)'  
    color4 = 'rgb(2, 130, 2)' 

    fig.add_trace(go.Scatter(x=t_plot, y=loading1, mode='lines', name='Level Factor Loading (β0)', line=dict(color=color1)))
    fig.add_trace(go.Scatter(x=t_plot, y=loading2, mode='lines', name='Slope Factor Loading (β1)', line=dict(color=color2)))
    fig.add_trace(go.Scatter(x=t_plot, y=loading3, mode='lines', name='Curvature Factor 1 Loading (β2)', line=dict(color=color3)))
    fig.add_trace(go.Scatter(x=t_plot, y=loading4, mode='lines', name='Curvature Factor 2 Loading (β3)', line=dict(color=color4)))

 
    fig.update_layout(

            title='Factor Loadings in the NSS Model',
            xaxis_title='Time to Maturity (Years)',
            yaxis_title='Factor Loading',
            plot_bgcolor='rgba(255,255,255,1)',
            title_x=0.5,
            width=1000,
            
            font=dict(
                family="Time New Roman",
                size=15,  # Set the font size here
                color="Black"
            ),

            xaxis=dict(
                showline=True, 
                linewidth=1, 
                linecolor='black',
                range=[0,27],
                ticks="inside",
                tickson="boundaries",
                ticklen=5,
                tickvals = [1, 2, 3, 4, 5,6,7,8,9,10,15,20,25]
            
            ),

            yaxis=dict(
                showline=True, 
                linewidth=1, 
                linecolor='Grey',
                gridcolor="rgba(38,38,38,0.15)", 
                
            ),
            legend=dict(
            yanchor="top",
        
            bgcolor = 'rgba(255,255,255,0)',
            
        )
            
        )
    
    fig.show()



def Graph_Curve(Yield, DBvsYield) :

    z = np.polyfit(Yield['Time to Maturity'], Yield['Zero-Coupon Yield'], 3)
    f = np.poly1d(z)

    x_new = np.linspace(0, 26, 50)
    y_new = f(x_new)

    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.7, 0.3],
        horizontal_spacing=0.05,
        specs=[[{"type": "scatter"},
            {"type": "table"}]]
    )

    fig.add_trace(
        go.Scatter(
            x=Yield['Time to Maturity'],
            y=Yield['Zero-Coupon Yield'],
            mode='markers',
            name='Zero-Coupon Yields',
            marker=dict(
                size=8,
                color='rgb(0, 71, 102)'
            )),

        row=1, col=1
    
    )

    fig.add_trace(
        go.Scatter(
            x=DBvsYield['Time to Maturity'],
            y=DBvsYield['Model Prediction (BEY)'],
            mode='markers',
            marker=dict(
                size=5,
                color='red'
            ),
            name='Model Prediction by DB',
        ),  

        row=1, col=1

        )

    fig.add_trace(
        go.Scatter(
            x=x_new,
            y=y_new,
            mode='lines',
            line=dict(
                color='rgb(0, 0, 0)',
                width=2
            ),
            name='Polyfit Zero-Coupon Yield'
        ),
        
        row=1, col=1
    )

    fig.update_layout(
        title='Zero-Coupon Yield Curve over 25 Years',
        plot_bgcolor='rgba(255,255,255,1)',
        title_x=0.5,
        width=900,
        height=585,
        xaxis_title="Time to Maturity (Years)",
        yaxis_title="Rate (%)",

        font=dict(
            family="Time New Roman",
            size=15,  # Set the font size here
            color="Black"
        ),

        xaxis=dict(
            showline=True, 
            linewidth=1, 
            linecolor='black',
            range=[0,27],
            ticks="inside",
            tickson="boundaries",
            ticklen=5,
            tickvals = [1, 2, 3, 4, 5,6,7,8,9,10,15,20,25]
        
        ),

        yaxis=dict(
            showline=True, 
            linewidth=1, 
            linecolor='Grey',
            gridcolor="rgba(255,255,255,1)", 
            
        ),
        legend=dict(
        yanchor="top",
        y=0.75,
        xanchor="left",
        x=0.39,
        bgcolor = 'rgba(255,255,255,0)',
        
    )
        
    )
    fig.add_trace(
        go.Table(
            header=dict(values=[' <b>Maturity ', '<b>Model DB', '<b>Yield ZC'],
                        fill_color='white',
                        align='center',
                        line_color='rgb(0, 71, 102)',
                        line_width=1.5)
                        ,
            cells=dict(values=[DBvsYield['Time to Maturity'],DBvsYield['Model Prediction (BEY)'], DBvsYield['Zero-Coupon Yield']],
                    fill_color='white',
                    align='center',
                    line_color='rgb(0, 71, 102)',
                    height=27
                    ),
                    
            
        ),
    row=1, col=2     
    )                  

    fig.show()


def Graph_EstimationVSZero(Yield,y_yield, x_new, y_new,Title,Model):
    
    fig = go.Figure()

    fig.add_trace(
            go.Scatter(
                x=Yield['Time to Maturity'],
                y=y_yield,
                mode='markers',
                name='Zero-Coupon Yields',
                marker=dict(
                    size=8,
                    color='rgb(0, 71, 102)'
                ))
        
        )

    fig.add_trace(
            go.Scatter(
                x=x_new,
                y=y_new,
                mode='lines',
                marker=dict(
                    size=5,
                    color='red'
                ),
                name=Model
            )

            )

    fig.update_layout(
            title=Title,
            plot_bgcolor='rgba(255,255,255,1)',
            title_x=0.5,
            width=900,
            height=500,
            xaxis_title="Time to Maturity (Years)",
            yaxis_title="Yield (%)",

            font=dict(
                family="Time New Roman",
                size=15,  # Set the font size here
                color="Black"
            ),

            xaxis=dict(
                showline=True, 
                linewidth=1, 
                linecolor='black',
                range=[0,27],
                ticks="inside",
                tickson="boundaries",
                ticklen=5,
                tickvals = [1, 2, 3, 4, 5,6,7,8,9,10,15,20,25]
            
            ),

            yaxis=dict(
                showline=True, 
                linewidth=1, 
                linecolor='Grey',
                gridcolor="rgba(38,38,38,0.15)", 
                
            ),
            legend=dict(
            yanchor="top",
            xanchor="left",
            bgcolor = 'rgba(255,255,255,0)',
            
        )
            
        )
            
    fig.show()


def graph_discount(maturity,discount_function,Title,Name):
    
    fig = go.Figure()

    fig.add_trace(
            go.Scatter(
                x= maturity,
                y= discount_function,
                mode='lines',
                name=Name,
                marker=dict(
                    size=8,
                    color='rgb(0, 71, 102)'
                ))
        
        )


    fig.update_layout(

            title=Title,
            
            plot_bgcolor='rgba(255,255,255,1)',
            title_x=0.5,
            width=900,
            height=500,
            xaxis_title="Time to Maturity (Years)",
            yaxis_title="Discount Factors",
            showlegend=True,
           
            font=dict(
                family="Time New Roman",
                size=15,  # Set the font size here
                color="Black"
            ),

            xaxis=dict(
                showline=True, 
                linewidth=1, 
                linecolor='black',
                range=[0,27],
                ticks="inside",
                tickson="boundaries",
                ticklen=5,
                tickvals = [1, 2, 3, 4, 5,6,7,8,9,10,15,20,25]
            
            ),

            yaxis=dict(
                showline=True, 
                linewidth=1, 
                linecolor='Grey',
                gridcolor="rgba(38,38,38,0.15)", 
                
            ),
            
            legend=dict(
           
            bgcolor="rgba(0, 0, 0, 0)",
            
        )
            
        )
            
    fig.show()


def graph_discount2(maturity,discount_function,maturity2,discount_function2,Title,yaxis,name1,name2):
    
    fig = go.Figure()

    fig.add_trace(
            go.Scatter(
                x= maturity,
                y= discount_function,
                mode='lines',
                name=name1,
                marker=dict(
                    size=8,
                    color='rgb(0, 71, 102)'
                ))
        
        )

    fig.add_trace(
            go.Scatter(
                x= maturity2,
                y= discount_function2,
                mode='lines',
                name=name2,
                marker=dict(
                    size=8,
                    color='rgb(255, 0, 0)'
                ))
        
        )

    fig.update_layout(

            title=Title,
            
            plot_bgcolor='rgba(0,0,0,0)',
            title_x=0.5,
            width=900,
            height=500,
            xaxis_title="Time to Maturity (Years)",
            yaxis_title=yaxis,
            showlegend=True,

            font=dict(
                family="Time New Roman",
                size=15,  # Set the font size here
                color="Black"
            ),

            xaxis=dict(
                showline=True, 
                linewidth=1, 
                linecolor='black',
                range=[0,27],
                ticks="inside",
                tickson="boundaries",
                ticklen=5,
                tickvals = [1, 2, 3, 4, 5,6,7,8,9,10,15,20,25]
            
            ),

            yaxis=dict(
                showline=True, 
                linewidth=1, 
                linecolor='Grey',
                gridcolor="rgba(38,38,38,0.15)", 
                
            ),
            
            legend=dict(
            bgcolor="rgba(0, 0, 0, 0)",  # Light background for visibility
        )
            
        )
            
    fig.show()