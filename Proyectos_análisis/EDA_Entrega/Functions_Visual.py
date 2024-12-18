import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Function for One-Variable Categorical Data Analysis (Bar Plot)
def plot_one_variable_categorical(data, column, title = None, figsize = (8, 5), palette = "Set2", relative = False):
    """
    Visualizes one-variable categorical data using a bar plot(countplot).
    
    Parameters:
    - data: pandas DataFrame
    - column: column name (string)
    - title: title for the plot (default: None)
    - figsize: figure size (default: (8, 5))
    - palette: color palette for the bar plot (default: "Set2")
    - relative: whether to show relative frequencies (default: False)
    """
    if type(column) != str:
        raise TypeError(f"Column '{column}' must be string.")

    if column not in data.columns:
        raise ValueError(f"Column '{column}' is not in the DataFrame.")

    plt.figure(figsize = figsize)

    if relative:
         count_data = data[column].value_counts(normalize = True) 
         sns.barplot(x = count_data.index, y = count_data.values,
                      palette = palette, hue = count_data.index) 
         plt.ylabel("Proportion", fontsize = 12)
    
    else: 
        sns.countplot(data = data, x = column, hue = column,
                       order = data[column].value_counts().index, palette = palette)
        plt.ylabel("Count", fontsize = 12)

    plt.title(title or f"Distribution of {column}", fontsize = 14)
    plt.xlabel(column, fontsize = 12)
    plt.xticks(rotation = 45, ha = 'right')
  
    plt.tight_layout()
  
    plt.show()



# Function for Two-Variable Categorical Data Analysis (Count Plot with hue)
def plot_two_variable_categorical(data, x_column, hue_column, title = None,
                                 figsize = (10, 6), palette = "coolwarm", relative = False):
    """
    Visualizes two-variable categorical data using a count plot with hue.
    
    Parameters:
    - data: pandas DataFrame
    - x_column: column name for the x-axis (string)
    - hue_column: column name for hue (string)
    - title: title for the plot (default: None)
    - figsize: figure size (default: (10, 6))
    - palette: color palette for the count plot (default: "coolwarm")
    - relative: whether to show relative frequencies (default: False)
    """
    if type(x_column) != str or type(hue_column) != str:
        raise TypeError(f"Column '{x_column}' and '{hue_column}' must be string.")

    if x_column not in data.columns or hue_column not in data.columns:
        raise ValueError(f"Column '{x_column}' or '{hue_column}' is not in the DataFrame.")
    
    plt.figure(figsize = figsize)
   
    if relative:
        # Calcular las frecuencias relativas
        df_copy_exploded = data.copy()
        grouped_data = df_copy_exploded.groupby(x_column, as_index=False)[hue_column].value_counts(normalize=True)
        grouped_data["proportion"] = grouped_data["proportion"] * 100
        sns.barplot(x = x_column, y = 'proportion', hue = hue_column,
                     data = grouped_data, palette = palette)
        plt.ylabel("Proportion (%)", fontsize=12)
    else:
        sns.countplot(data = data, x = x_column, hue = hue_column, palette = palette,
                       order = data[x_column].value_counts().index)
        plt.ylabel("Count", fontsize = 12)

    plt.title(title or f"Relationship between {x_column} and {hue_column}", fontsize = 14)
    plt.xlabel(x_column, fontsize = 12)
    plt.xticks(rotation = 45, ha = 'right')
    plt.legend(title = hue_column, fontsize = 10)

    plt.tight_layout()

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


