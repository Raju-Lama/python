import pandas as pd
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

#  Creating a DataFrame from JSON Data

'''
In the last lesson, we were introduced to the concept of integrating APIs with Pandas for data wrangling. In this lesson, we'll take a step further by learning how to create a DataFrame from JSON data.

Let's have a look at some JSON data below:

json_data = '{"name": ["John", "Anna", "Peter", "Linda"], "age": [28, 23, 34, 32]}'

The json_data string provided above is a JSON object containing two key-value pairs. The keys are name and age, and their corresponding values are lists of names and ages, respectively. JSON arrays (equivalent to Python lists) are used here to represent a collection of data. In this case:

name is associated with a list of four names: ["John", "Anna", "Peter", "Linda"].
age is associated with a list of four ages: [28, 23, 34, 32].
We can now use the Pandas function read_json() to convert JSON data into a DataFrame. When the pd.read_json(json_data) function is called, Pandas interprets the JSON object in the following manner:

It identifies the keys name and age as column headers for the resulting DataFrame.
It takes the lists associated with each key and creates a column in the DataFrame for each list, with the values aligned according to their index in the list.
Because there are equal numbers of names and ages, pandas will create a DataFrame with four rows (one for each pair of name and age) and two columns (one for names and one for ages).


json_data = '{"name": ["John", "Anna", "Peter", "Linda"], "age": [28, 23, 34, 32]}'
df=pd.read_json(json_data)
print(df)

|   | name  | age |
|---|-------|-----|
| 0 | John  |  28 |
| 1 | Anna  |  23 |
| 2 | Peter |  34 |
| 3 | Linda |  32 |


'''

json_data = '{"country": ["Canada", "England", "Japan"], "region": ["North America", "Europe", "Asia"] }'
# it should be in " double quotes for json

df_country = pd.read_json(json_data)

df_total_rows = len(df_country.index)
# lenght of the dataframe, total rows

print(df_country)


# Data Formats in API Retrieval

response = requests.get('https://api-server.dataquest.io/economic_data/countries')

economic_data = response.json()
# json format

print(economic_data)

'''
Reading JSON Data into a DataFrame
Learn
Our previous lesson emphasized the complexities involved in data retrieval from APIs, with a particular emphasis on JSON, which stands for JavaScript Object Notation. JSON is a commonly used format for data exchange, and it is appreciated for its readability and syntactic simplicity, which benefits both humans and machines.

When we issue a GET request to an API, the response is typically in JSON format. This format presents data as a collection of key-value pairs, similar to a dictionary in Python.

We will continue to explore the URL https://api-server.dataquest.io/economic_data/countries, which leads to an API endpoint providing economic data for various countries. As seen in the previous lesson, this endpoint (/countries) returns a JSON array containing objects for each country, including fields such as country_code, short_name, long_name, currency_unit, region, income_group, and other economic indicators.

Previously, the data was not easy to interpret, and we could not quickly discern the information it contained. We can address this issue by reading the data into a DataFrame, allowing us to explore it further.

import requests
import pandas as pd
data=requests.get('https://api-server.dataquest.io/economic_data/countries')
data=data.json()
df = pd.read_json(data)

Explain

Copy
Now that our data is in a structured, tabular format, we can take advantage of pandas' powerful data manipulation capabilities. For instance, to view a few rows within our dataset, we can use df.head(), which by default displays the first five rows, with df being the name of our DataFrame.
'''

response = requests.get('https://api-server.dataquest.io/economic_data/indicators')

data = response.json()

df_economic = pd.read_json(data)

most_frequent_source = df_economic['source'].value_counts().idxmax()
# idxmax() returns the index of the first occurrence of the maximum value
# value_counts() returns a Series containing counts of unique values
# source is the column name
# most_frequent_source is the most frequent source in the source column 

print(most_frequent_source)



'''
Handling Data without APIs
Learn
On the previous screens, we've been focusing on retrieving data using APIs and converting it into a more manageable format, such as a pandas DataFrame. This approach is efficient and straightforward when the data source provides an API. But what happens when we encounter a data source that doesn't offer an API?

This scenario isn't uncommon. Many websites and data sources don't provide APIs due to technical limitations, policy restrictions, or simply a lack of demand. However, this doesn't mean we can't extract the data; it just means we need to be a bit more creative.

One common approach is to extract data directly from a web page's HTML. HTML, which stands for HyperText Markup Language, is the standard language for creating web pages. It uses a series of elements to structure and style content. We can extract the underlying data by parsing a web page's HTML.

Fortunately, pandas provides a convenient function, pd.read_html(), which can extract tabular data from HTML content directly into a DataFrame. This function is particularly useful for scraping data from web pages that contain structured data in the form of HTML tables:

import pandas as pd
import requests
from bs4 import BeautifulSoup
​
​
url = 'https://www.iana.org/help/example-domains' # Example URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')
df = pd.read_html(str(table))[0]
print(df)

Explain

Copy
The code above, for example, performs web scraping by sending an HTTP request to a specified URL, parsing the returned HTML to find the first table, and then using Pandas read_html function to convert that table into a DataFrame, which it prints out.

In the exercise below, we'll work with this Wikipedia page. It has a table that contains a list of countries and dependencies with columns for their rank, country or dependency name, population, percentage of the world's population, date of the information, and the source of the data. This table uses data from various official and authoritative sources, providing a snapshot of population figures, which can be useful for demographic studies, economic analysis, and geopolitical research. The table is a central feature of the page, offering valuable insights into the distribution of the global population.
'''

response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')

soup = BeautifulSoup(response.text, 'html.parser')
# we need to parse html file

table = soup.find('table')

df = pd.read_html(str(table))[0]
# reading into pandas dataframe
'''
Use the pd.read_html() function from pandas to convert the HTML table, which you've converted to a string using str(table), into a DataFrame. The read_html() function will return a list of DataFrames, so access the first one using [0] and assign it to the variable df.
'''


print(df.shape)
# gives (row, column)

df_columns = 7

# or use len(df.columns)

'''
Exploring HTML Pages
Learn
On the previous screen, we focused on using pandas' pd.read_html() function to extract tables from HTML pages. However, web pages are made up of much more than just tables. They include paragraphs, links, lists, and various elements with different attributes that can contain valuable data. To effectively scrape and analyze this data, we need to understand how to navigate and extract from these varied elements.

BeautifulSoup is an incredibly versatile tool that allows us to parse an entire HTML document and extract different data types. It provides methods to search for specific elements and attributes, such as:

Paragraphs (p): These are typically blocks of text. You can extract text content from them.
Links (a): They have an href attribute that you can extract to get the URL they point to.
Classes and IDs: Many HTML elements have class or ID attributes that can be used to identify them uniquely.
Other Elements: Such as span, div, header, footer, etc., that might contain specific data or be used to structure the data in a certain way.
We will continue our exploration with the Wikipedia page. Earlier in this lesson, we learned how to create a DataFrame from JSON data. Other methods for creating DataFrames exist, such as using dictionaries and lists. Let's explore how we can create a DataFrame that contains all the paragraph texts from this Wikipedia page. We'll start by gathering these texts into a list and then use that list to create a pandas DataFrame.

import requests
from bs4 import BeautifulSoup
import pandas as pd
​
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
​
​
# Extracting paragraphs and creating a DataFrame
wikipedia_paragraphs = []
for p in soup.find_all('p'):
    text = p.get_text().strip()  # strip() removes leading and trailing whitespace
    if text:  # Only append non-empty strings
        wikipedia_paragraphs.append(text)
​
wikipedia_df = pd.DataFrame(wikipedia_paragraphs)
print(wikipedia_df)

Explain

Copy
|    | Paragraph Text                                                |
|----|---------------------------------------------------------------|
| 0  | This is a list of countries and dependencies by population... |
| 1  | Figures used in this chart are based on the most up to date...|
| 2  | Where updated national data are not available...              |
| 3  | Because the compiled figures are not collected at the same ...|
| 4  | Areas that form integral parts of sovereign states...         |
| 5  | Note: A numbered rank is assigned to the 193 member states... |

Explain

Copy
From the above, we were able to capture all the paragraph texts in a DataFrame. Having this information in a DataFrame helps us perform various analyses provided by pandas. For example, we can quickly determine the number of paragraphs on this page by simply calling the .shape method on our DataFrame, i.e., wikipedia_paragraphs.shape[0].

Let's now extend this knowledge further. In the following exercise, we'll scrape the same Wikipedia page to extract the text and href attributes from all hyperlink (anchor) elements. We'll store the cleaned text and URLs in separate lists and then combine these lists into a dictionary. This dictionary will then be used to create a pandas DataFrame containing columns for the hyperlink texts and the associated URLs
'''


url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

link_texts = []
link_hrefs = []

for a in soup.find_all('a'):
    text = a.get_text().strip()
#     this will collect link Text
#     strip() to remove trailing spaces 
    
    links = a.get('href')
#     this will collect href's to gather the corresponding urls
    
    if text or links:
        link_texts.append(text)
        link_hrefs.append(links)
        
links_dict = {'Link Text':link_texts,
              'URL':link_hrefs
             }

df_links = pd.DataFrame(links_dict)

print(df_links.head())

'''
Data Analysis with DataFrames
Learn
So far, we've learned how to create a pandas DataFrame from JSON data, dictionaries, and even directly from web pages using pd.read_html(). Now that we have our data in DataFrames, it's time to do some data analysis!

Having successfully structured our data into DataFrames, it is essential to develop a comprehensive understanding of the analytical techniques and capabilities at our disposal. DataFrames, being a central component of the pandas library, offer a robust platform for a wide range of data manipulations and explorations. They are adept at handling complex datasets and providing functionalities for sorting, filtering, and summarizing data, which are crucial for insightful analysis.

We'll work with the DataFrame below, which is saved as df_books.

| | Title| Author   | Genre      |Year Published |Page Count| Read |
|-|------|----------|------------|---------------|----------|------|
|0| Book1| Author1  | Fiction    |          2000 |       200| True |
|1| Book2| Author2  | Non-Fiction|          2005 |       350| False|
|2| Book3| Author3  | Fiction    |          2010 |       250| True |
|3| Book2| Author2  | Non-Fiction|          2005 |       350| False|
|4| Book5| Author5  | Fiction    |           nan |       600| True |
|5|      | Author6  | Fiction    |          2020 |       350| False|

Explain

Copy
So, let's start exploring our DataFrame. If we have a DataFrame, df_books, containing information about a book collection, we can get a quick overview of our data using the .info() method:

df_books.info()

Explain

Copy
This generates a summary of df_books, including the number of entries, column names, number of non-null values in each column, and the data type of each column.

But, before we dive into data analysis, we might need to tidy up our data. Data cleaning often involves:

Dropping columns: Some columns may not be relevant to our analysis. We can remove them using the df.drop(axis=1) method.
Removing duplicates: Duplicates can skew our analysis. We can remove them using the df.drop_duplicates() method.
Dealing with missing values: Missing data can also affect our analysis. We can choose to either remove rows with missing data using df.dropna() or fill in the missing values with df.fillna().
Changing data types: Sometimes, we might need to change the data type of a column to perform certain operations. For this, we can use the Series.astype() method.
To demonstrate, let's imagine that the Year Published column is irrelevant to our current analysis. We can remove it like this:

df_books.drop('Year Published', axis=1, inplace=True)

Explain

Copy
This code eliminates the Year Published column from the df_books DataFrame. The drop method is used here, with the first argument specifying the column name to be removed. The axis=1 argument indicates that we are removing a column (as opposed to a row), and inplace=True ensures that the change is applied directly to the DataFrame without the need to create a new one.

Once our data is clean, we can start to explore it more deeply. Perhaps we want to get some summary statistics for a numerical column. We can use the .describe() method to get the count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum values.

df_books['Page Count'].describe()

'''

print(df_wikipedia.info())

df_wikipedia = df_wikipedia.drop('Notes', axis=1, inplace=True)
df_wikipedia = df_wikipedia.dropna()

cleaned_df = df_wikipedia.drop_duplicates()
print(cleaned_df.describe())


'''
 Advanced Data Analysis with DataFrames
Learn
DataFrames are a central component of the pandas library, providing a platform for various data manipulations and explorations. On this screen, we'll focus on filtering and grouping data and creating visualizations to better understand trends and patterns in our data.

We'll continue working with the cleaned df_books DataFrame we had on the previous screen.

| |Title| Author| Genre      |Year Published|Page Count| Read |
|-|-----|-------|:-----------|--------------|----------|------|
|0|Book1|Author1| Fiction    |         2000 |      200 | True |
|1|Book2|Author2| Non-Fiction|         2005 |      350 | False|
|2|Book3|Author3| Fiction    |         2010 |      250 | True |
|3|Book2|Author2| Non-Fiction|         2005 |      350 | False|
|4|Book5|Author5| Fiction    |          nan |      600 | True |
|5|     |Author6| Fiction    |         2020 |      350 | False|

Explain

Copy
We can filter out specific rows in our DataFrame based on a certain condition. For instance, if we want to filter out books that were published in the year 2010 and above:

df_books_above_2010 = df_books[df_books['Year Published'] >= 2010]

Explain

Copy
This will give us a new DataFrame, df_books_above_2010, which only includes rows where the Year Published value is greater than or equal to 2010.

Grouping data is another powerful feature of pandas. Suppose we want to group our books by Genre and calculate the mean Page Count for each group. We can achieve this using the df.groupby() method and .mean() function:

book_genre = df_books.groupby('Genre')['Page Count'].mean()

Explain

Copy
Finally, once we have performed our analysis, we may want to visualize our results for better understanding. For instance, we can plot the mean page count for each genre using a bar chart:

import matplotlib.pyplot as plt
​
book_genre.plot(kind='bar')
plt.ylabel('Mean Page Count')
plt.title('Mean Page Count by Genre')
plt.show()
'''

# Our cleaned DataFrame. Uncomment the following if you want to use it:
df_wikipedia = df_wikipedia.drop(columns=['Unnamed: 0'], errors='ignore')
df_wikipedia = df_wikipedia.drop_duplicates()

countries_pop_under_10000 = df_wikipedia[df_wikipedia['Population']<10000]

countries_pop_under_10000.plot(kind='bar')
plt.xlabel('Population')
plt.ylabel('Location')

plt.title('Population by Country')
plt.show()

