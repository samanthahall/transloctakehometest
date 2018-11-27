# IPv6 Address Heat Map
  
  This application displays a heatmap of all IPv6 address geolocations as defined by GeoLiteCityv6.csv.
   
  A working example can be seen https://enigmatic-wildwood-58658.herokuapp.com/
  
  ## Notes
  The data was significantly smaller than anticipated. The IPv4 data set defined by GeoCityLite is much much larger. Due to the fact that the IPv6 data was small, I found that no filtering was required to achieve fast client performance. I was able to send all data necessary to display geolocations in just 18kb. 
  
  If the data was larger, I might have needed to setup a database to query using the client's map bounds as parameters. In the case where that still produced a data set too large to be performant (when zoomed worldwide for example) I would aggregate heatmap points to a lower lat/lng resolution. This would for example return the same lat/lng for geolocations in the whole Eastern North Carolina region because at a zoom showing the entire world the user would not be able to distinguish anything more precise on the map.
  
I have not yet had a chance to apply Protocol Buffers in place of the JSON. I have not used Protocol Buffers but in reading about them it seems they could be extremely useful had I plans to expand upon this application.
  
  ## Bonuses
  ### Tests
  I performed manual usability and performance tests. I have not yet set up a framework to define unit tests. Typically I might have written some unit tests beforehand which can help with the design phase. However this project has been a whole new arena for me so I started with a "play phase" to familiarize myself. I also felt my time was best spent delivering the requirements.
  ### Performance
  As mentioned above, I have not implemented anything further to improve performance at this time. I anticipate that given a larger data set my current code would slow down significantly.
  ### Redeployment of the data zip file
  Admittedly my current solution is not ideal because a new data file would require redeployment of the entire application. I appreciate that there could be value in implementing a solution that provides for updating just the data file.
