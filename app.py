import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Load data from the CSV file
    df = pd.read_csv('amazon_data.csv')

    # Create a bar chart of product ratings
    rating_bar_chart = px.bar(df, x='title', y='rating', title='Product Ratings')
    print(type(rating_bar_chart))

    # Create a scatter plot of product prices vs. ratings
    price_rating_scatter = px.scatter(df, x='price', y='rating', title='Product Prices vs. Ratings', color='availability')

    # Create a table of product details
    product_table = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df.title, df.price, df.rating, df.reviews, df.availability],
                   fill_color='lavender',
                   align='left'))
    ])
    product_table.update_layout(title='Product Details')

    # Render the HTML template with the dashboard
    return render_template('dashboard.html', rating_bar_chart=rating_bar_chart.to_json(), price_rating_scatter=price_rating_scatter.to_json(), product_table=product_table)

if __name__ == '__main__':
    app.run(debug=True)
