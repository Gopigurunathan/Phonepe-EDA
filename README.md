# PhonePe Pulse Data Visualization and Exploration

## Objective
The aim of this project is to develop a solution that extracts, transforms, and visualizes data from the PhonePe Pulse GitHub repository.

## libraries used

Streamlit and streamlit-option-menu : were used to create an interactive dashboard and navigation menus, providing a user-friendly interface for data visualization.

Pandas : was employed for data manipulation and analysis, ensuring that the data was cleaned and structured appropriately for visualization and storage.

mysql-connector: facilitated the connection to a MySQL database, allowing for efficient data storage and retrieval.

Plotly: Express enabled the creation of interactive and visually appealing plots and charts, enhancing the dashboard's ability to convey insights.

Requests and JSON : were used to interact with APIs and handle JSON data, enabling the integration of external data sources into the project.

## Project Steps

### Data Extraction
- Method: Scripted the cloning of the PhonePe Pulse GitHub repository.
- Goal: Efficiently collect the raw data required for analysis.

### Data Transformation
- Tools: Python, Pandas.
- Process: Cleaned and structured the data to ensure it was in a usable format for analysis and visualization.

### Database Insertion
- Database: MYSQL.
- Action: Stored the transformed data in a PostgreSQL database for efficient retrieval and querying.


### Dashboard Creation
- Tools: Streamlit, Plotly.
- Development: Built an interactive dashboard to visualize the data dynamically. The dashboard provides various charts, graphs, and interactive elements to explore the data effectively.

### Data Retrieval
- Process: Implemented dynamic data fetching from the PostgreSQL database to ensure the dashboard always presents up-to-date information.

## Results
The project successfully created an interactive dashboard that allows users to explore PhonePe Pulse data in a detailed and user-friendly manner. Key trends and insights were easily identified through the visualizations provided.

## Challenges
- Data Cleaning: Handling inconsistencies and ensuring data integrity during the transformation phase.
- Database Management: Efficiently storing and retrieving large datasets from PostgreSQL.
- Interactive Dashboard: Ensuring real-time updates and smooth interaction within the Streamlit and Plotly environment.

## Impact
This project enhances the understanding of PhonePe Pulse data by providing a clear and interactive platform to explore various metrics and trends.It aids stakeholders in making informed decisions based on comprehensive data analysis.

## Future Work
- Enhanced Visualizations: Incorporating more complex visualizations and analytics.
- Scalability: Improving the system to handle larger datasets and more complex queries.
- User Experience: Adding more features to the dashboard for a better user experience, such as custom queries and predictive analytics.
