# Multi dimensional residual analysis application in Python Dash.
Author- Kanishka Narayan
Contact- kanishkan91@gmail.com

Residuals are widely used as a part of statistical analysis. However, there are various dimensions that are available to analyze residuals such as the statistical relationships (relationships with different variables), temporal dimensions (the predicted vs actual value over time), cross-sectional dimensions (the value of individual observations) and metrics over time (summary stats over time). 

This python dashboard helps a user explore these dimensions for residuals (where Logged GDP is used as the IV) that are dynamically generated using a python function. Attached below is a screenshot showing the application-

![Test Image 1](https://github.com/kanishkan91/Residual-analysis-application/blob/master/Residualanalysis.JPG)

The dashboard contains the following features,

## 1.Dropdown selector-
   The user can select one of 5 variables (this can be extended to any number of variables) which will be used to populate the application. This is the first parameter that will be fed into the application.Currently the application is programmed to handle 5 human capital variables (Life expectancy, Education quality, Education years, Health expenditure and Education expenditure).
 
## 2.3D Scatter plot- 
The main plot shows a 3 dimensional scatterplot of the variable, logged GDP and the residuals. The color range of the residual is an added 4th dimension. The user can rotate the view of the 3D scatter plot to compare different combinations of regressions. The user can hover over any point which will populate the time series plot (explained below) for that observation. Changing the year bar under the plot allows the user to reconstruct the plot for any year.

## 3. Year selector-
The year selector updates itself for any selected variable in the drop down. The max, min and the value are generated dynamically and can be updated by the user through clicking. This allows the user to add a 5th temporal dimension.

## 4.Time series-
Hovering over any observation in the main plot will update the time series which shows the predicted versus the actual for the dependent variable for the selected observation. This is an extension of the 5th dimension to an individual observation.

## 5.Summary stats table-
Finally, the summary stats table to the lower right is updated automatically for any selected variable. The summary stats are generated over time as well. 

## 6.Generating residuals using a dynamic python function-
The user can manipulate the GenerateResidualTimeSeries function to generate residuals for any combination  of DVs and IVs to generate the base data for the application.


## Using this application-
This application is deployed on Heroku here- https://residualanalysisfinal.herokuapp.com/ and can also be run locally. If you would like to run this locally, just make one smal change to the application.py file as below,

Change below, 
if __name__ == '__main__':
    application.run_server(debug=True)

to,
if __name__ == '__main__':
    app.run_server(debug=True)

The requirements.txt shows the packages and the relevant versions required for the app. Please feel free to update the versions of any of the packages except the dash-renderer. The heroku app requires that specific version of the package to function correctly.







   

 


