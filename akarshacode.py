import pandas as pd
import matplotlib.pyplot as plt

def read_csv(file_path):
    """Read the CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def extract_data(df, series_name):
    """Extract data for a specific series name."""
    return df[df['Series Name'] == series_name]

def apply_plot_style(title, x_label, y_label):
    """Apply a common style to the plots."""
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()

def plot_multiline_graph(data, x_values, title):
    """
    Create a multiline graph for the provided data.

    Parameters:
    - data: DataFrame, data for multiple countries
    - x_values: list, x-axis values (e.g., years)
    - title: str, title of the graph
    """
    plt.figure(figsize=(12, 8))
    
    for index, row in data.iterrows():
        plt.plot(x_values, row[4:], label=row['Country Name'], marker='o')

    # Apply the common style
    apply_plot_style(title, 'Year', 'Population Growth (annual %)')

    # Show the plot
    plt.show()

def plot_bar_graph(data, x_values, title, country_name):
    """
    Create a bar plot for the provided data.

    Parameters:
    - data: DataFrame, data for a specific country
    - x_values: list, x-axis values (e.g., years)
    - title: str, title of the graph
    - country_name: str, name of the country
    """
    plt.figure(figsize=(12, 8))
    plt.bar(x_values, data.iloc[0, 4:], label=country_name)

    # Apply the common style
    apply_plot_style(title, 'Year', 'Population Growth (annual %)')

    # Show the plot
    plt.show()

def plot_pie_chart(data, title, country_name):
    """
    Create a pie chart for the provided data.

    Parameters:
    - data: DataFrame, data for a specific country
    - title: str, title of the pie chart
    - country_name: str, name of the country
    """
    plt.figure(figsize=(8, 8))
    plt.pie(data.iloc[0, 4:], labels=data.columns[4:], autopct='%1.1f%%', startangle=90)
    plt.title(f'Population Growth Distribution (annual %) in {country_name}')

    # Show the plot
    plt.show()

def main():
    """Main function to demonstrate the usage of the visualization functions."""
    # Example usage for multiline graph
    file_path = r"C:\Users\Population growth (annual %).csv"
    df = read_csv(file_path)

    series_name = 'Population growth (annual %)'
    countries_data = extract_data(df, series_name)

    x_values = df.columns[4:]
    title_multiline = 'Population Growth (annual %) - All Countries'

    plot_multiline_graph(countries_data, x_values, title_multiline)

    # Example usage for bar plot (China)
    china_data = df[df['Country Name'] == 'China']
    title_bar_china = 'Population Growth (annual %) in China'

    plot_bar_graph(china_data, x_values, title_bar_china, 'China')

    # Example usage for pie chart (United States)
    us_data = df[df['Country Name'] == 'United States']
    title_pie_us = 'Population Growth Distribution (annual %) in United States'

    plot_pie_chart(us_data, title_pie_us, 'United States')

    # Example usage for pie chart (India)
    india_data = df[df['Country Name'] == 'India']
    title_pie_india = 'Population Growth Distribution (annual %) in India'

    plot_pie_chart(india_data, title_pie_india, 'India')

# Call the main function
if __name__ == "__main__":
    main()
