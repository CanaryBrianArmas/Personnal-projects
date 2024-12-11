import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Function for One-Variable Categorical Data Analysis (Bar Plot)
def plot_one_variable_categorical(data, column, title = None, figsize = (8, 5), palette = "Set2"):
    """
    Visualizes one-variable categorical data using a bar plot(countplot).
    
    Parameters:
    - data: pandas DataFrame
    - column: column name (string)
    - title: title for the plot (default: None)
    - figsize: figure size (default: (8, 5))
    - palette: color palette for the bar plot (default: "Set2")
    """
    if type(column) != str:
        raise TypeError(f"Column '{column}' must be string.")

    if column not in data.columns:
        raise ValueError(f"Column '{column}' is not in the DataFrame.")

    
    plt.figure(figsize = figsize)
    sns.countplot(data = data, x = column, order = data[column].value_counts().index,
                  palette = palette)
  
    plt.title(title or f"Distribution of {column}", fontsize = 14)
    plt.xlabel(column, fontsize = 12)
    plt.ylabel("Count", fontsize = 12)
    plt.xticks(rotation = 45, ha = 'right')
  
    plt.tight_layout()
  
    plt.show()



# Function for Two-Variable Categorical Data Analysis (Count Plot with hue)
def plot_two_variable_categorical(data, x_column, hue_column, title = None,
                                 figsize = (10, 6), palette = "coolwarm"):
    """
    Visualizes two-variable categorical data using a count plot with hue.
    
    Parameters:
    - data: pandas DataFrame
    - x_column: column name for the x-axis (string)
    - hue_column: column name for hue (string)
    - title: title for the plot (default: None)
    - figsize: figure size (default: (10, 6))
    - palette: color palette for the count plot (default: "coolwarm")
    """
    if type(x_column) != str or type(hue_column) != str:
        raise TypeError(f"Column '{x_column}' and '{hue_column}' must be string.")

    if x_column not in data.columns or hue_column not in data.columns:
        raise ValueError(f"Column '{x_column}' or '{hue_column}' is not in the DataFrame.")
    
    plt.figure(figsize = figsize)
    sns.countplot(data = data, x = col1, hue = col2, palette = palette,
                  order = data[col1].value_counts().index)
    plt.title(title or f"Relationship between {col1} and {col2}", fontsize = 14)
    plt.xlabel(col1, fontsize = 12)
    plt.ylabel("Count", fontsize = 12)
    plt.xticks(rotation = 45, ha = 'right')
    plt.legend(title = col2, fontsize = 10)

    plt.tight_layout()

    plt.show()


# Function for Multi-Variable Numeric Data Analysis (Pair Plot)
def plot_multi_variable_numeric(data, columns, color = "blue"):
    """
    Visualizes multi-variable numeric data using a pair plot.
    
    Parameters:
    - data: pandas DataFrame
    - columns: list of column names (list of strings)
    - color: singlecolor or list of colors for the pair plot (default: "blue")
    """
    if not all(col in data.columns for col in columns):
        raise ValueError("Some columns are not in the DataFrame.")

    sns.pairplot(data[columns], color = color)
    plt.title("Multi-Variable Numeric Data Analysis (Pair Plot)")
    plt.suptitle("Pairwise Relationships", y =1.02)

    plt.show()


# Function for Multi-Variable Data Analysis (Categorical and Numeric)
def plot_multi_variable_mixed(data, numeric_column, categorical_column, palette = "Set2"):
    """
    Visualizes a numeric column against a categorical column (violin plot).
    
    Parameters:
    - data: pandas DataFrame
    - numeric_column: numeric column name (string)
    - categorical_column: categorical column name (string)
    - palette: color palette for the violin plot (default: "Set2")
    """
    if numeric_column and categorical_column != str:
        raise TypeError(f"Column '{numeric_column}' and '{categorical_column}' must be string.")
    
    plt.figure(figsize = (8, 6))
    sns.violinplot(data = data, x = categorical_column, y = numeric_column,
                    palette = palette)

    plt.title(f"{numeric_column} by {categorical_column}")
    plt.xlabel(categorical_column)
    plt.ylabel(numeric_column)

    plt.show()


# Function for Heatmap of Correlation Matrix (for numeric data)
def plot_heatmap_correlation(data, columns, annot = True, cmap = "coolwarm",
                              fmt = ".2f", linewidths = 0.5):
    """
    Visualizes the correlation matrix of numeric data using a heatmap.
    
    Parameters:
    - data: pandas DataFrame
    - columns: list of column names (list of strings)
    - annot: boolean (default: True)
    - cmap: color map for the heatmap (default: "coolwarm")
    - fmt: format for the heatmap values (default: ".2f")
    - linewidths: width of the heatmap lines (default: 0.5)
    """
    correlation_matrix = data[columns].corr()
    plt.figure(figsize = (10, 8))

    sns.heatmap(correlation_matrix, annot = annot, cmap = cmap,
                 fmt = fmt, linewidths = linewidths)
    plt.title("Correlation Heatmap")

    plt.show()


