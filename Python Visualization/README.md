# Movie Dataset Analysis and Cleaning

## Overview

This project involves analyzing and cleaning a movie dataset to uncover trends, correlations, and insights. The dataset contains various attributes related to movies, such as titles, genres, ratings, release dates, budgets, revenues, and more. The project demonstrates techniques for cleaning and visualizing data, making it suitable for showcasing in a portfolio.

## Features

- **Data Loading**: The dataset is loaded using `pandas` for efficient manipulation.
- **Missing Data Handling**:
  - Calculated the percentage of missing values for each column.
  - Addressed missing values using appropriate techniques, such as replacing or dropping entries.
- **Data Type Conversion**:
  - Converted columns (e.g., `budget` and `gross`) to suitable data types for analysis.
- **Visualization**: Created insightful visualizations using `matplotlib` and `seaborn` to explore relationships within the dataset.
- **Correlation Analysis**: Analyzed numerical correlations between movie attributes such as budget, gross revenue, and ratings.

## Key Libraries Used

- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations.
- **Matplotlib**: Visualization.
- **Seaborn**: Advanced visualization for statistical insights.

## Sample Workflow

1. **Inspecting the Dataset**: Checked the first few rows of the dataset to understand its structure.
2. **Identifying Missing Data**: Calculated the percentage of missing values in each column.
3. **Cleaning**:
   - Fixed missing values in critical columns.
   - Converted data types for consistency.
4. **Visualization**:
   - Created scatter plots and heatmaps to analyze correlations.
   - Generated distribution plots for key numerical attributes.
5. **Correlation Analysis**: Explored relationships between budget, gross revenue, and ratings.

## Results

- Discovered meaningful correlations between budget and revenue.
- Identified genres and directors associated with high-grossing movies.
- Visualized trends over time, such as the evolution of movie ratings.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movies-data-cleaning.git
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook "Movie Correlation.ipynb"
   ```

## Screenshots

- Heatmap showing correlations between numerical columns.
- Scatter plot of budget vs. gross revenue.

## Future Work

- Incorporate advanced statistical analysis.
- Expand visualizations to include interactive dashboards.
- Use machine learning to predict movie revenue based on available data.

---

