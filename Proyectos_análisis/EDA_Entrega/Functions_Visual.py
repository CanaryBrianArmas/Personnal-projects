import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set default styles
sns.set_theme(style = "whitegrid")

# Function for One-Variable Categorical Data Analysis (Bar Plot)
def plot_one_variable_categorical(data, column, palette = "Set2"):
    """
    Visualizes one-variable categorical data using a bar plot(countplot).
    
    Parameters:
    - data: pandas DataFrame
    - column: column name (string)
    - palette: color palette for the bar plot (default: "Set2")
    """
    if column not in data.columns:
        raise ValueError(f"Column '{column}' is not in the DataFrame.")
    if type(column) != str:
        raise TypeError(f"Column '{column}' must be string.")
    
    plt.figure(figsize = (8, 6))
    sns.countplot(data = data, x = column, palette = palette)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()



# Function for Two-Variable Categorical Data Analysis (Count Plot with hue)
def plot_two_variable_categorical(data, x_column, hue_column, palette = "coolwarm"):
    """
    Visualizes two-variable categorical data using a count plot with hue.
    
    Parameters:
    - data: pandas DataFrame
    - x_column: column name for the x-axis (string)
    - hue_column: column name for hue (string)
    - palette: color palette for the count plot (default: "coolwarm")
    """
    if x_column not in data.columns:
        raise ValueError(f"Column '{x_column}' is not in the DataFrame.")
    if type(x_column) != str:
        raise TypeError(f"Column '{x_column}' must be string.")
    
    plt.figure(figsize = (8, 6))
    sns.countplot(data = data, x = x_column, hue = hue_column, palette = palette)
    plt.legend(title = hue_column)
    plt.title(f"Distribution of {x_column} by {hue_column}")
    plt.xlabel(x_column)
    plt.ylabel("Count")
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


