

# Search Recommendation System

This project is a web-based **Search Recommendation System** that provides users with two types of recommendations: **content-based** and **semantic-based**. It combines modern web technologies and machine learning techniques to deliver personalized and accurate suggestions.

---

## Features

- **User-Friendly Interface**: A clean and intuitive web interface for entering queries and viewing results.
- **Dual Recommendation System**:
  - **Content-Based Recommendations**: Uses TF-IDF to find titles and authors similar to the query.
  - **Semantic Recommendations**: Utilizes a SentenceTransformer model to provide deeper, meaning-based recommendations.
- **Dynamic Results Display**: Results are categorized into content-based and semantic-based recommendations for easy understanding.
- **Backend Integration**: Seamless interaction between Node.js and Python for efficient data processing and recommendation generation.

---

## Technology Stack

### Frontend
- **HTML**: For structuring the web pages.
- **EJS (Embedded JavaScript)**: For dynamic rendering of pages and data.
- **CSS**: For styling the application.

### Backend
- **Node.js**: For server-side operations and handling user requests.

### Data Processing
- **Python**: For implementing machine learning models and data manipulation.
- **Machine Learning Models**:
  - **TF-IDF**: For content-based recommendations.
  - **SentenceTransformer**: For semantic recommendations.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/search-recommendation-system.git
   cd search-recommendation-system
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up Python environment:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the dataset `books.csv` is placed in the `scripts/searchBook` directory.

---

## Usage

1. Start the Node.js server:
   ```bash
   node app.js
   ```

2. Open the application in your browser:
   ```
   http://localhost:3000
   ```

3. Enter a search query in the input box and click **Search**.

4. View the recommendations displayed on the results page.

---

## File Structure

```
project/
├── public/
│   ├── style.css               # CSS for styling the application
├── routes/
│   ├── index.js                # Node.js routes for handling requests
├── scripts/
│   ├── searchBook/
│       ├── main.py             # Python script for recommendations
│       ├── books.csv           # Dataset of books
├── views/
│   ├── index.ejs               # Homepage template
│   ├── results.ejs             # Results page template
├── app.js                      # Main application entry point
├── package.json                # Node.js package dependencies
├── requirements.txt            # Python dependencies
```

---

## How It Works

1. **Homepage**: Users enter a query in the search box and submit it.
2. **Backend Processing**:
   - Node.js sends the query to a Python script via `child_process`.
   - The Python script processes the query using TF-IDF and SentenceTransformer models.
   - The script returns recommendations in JSON format.
3. **Results Display**:
   - The Node.js server renders the results page using the EJS template engine.
   - Recommendations are displayed in two categories: **content-based** and **semantic-based**.

---

## Sample Output

- **Query**: `world`

### Content-Based Recommendations:
1. The Great World
2. Babar's World Tour
3. Annals of the Former World
4. Rumic World Trilogy Volume 3
5. A History of the World in 6 Glasses

### Semantic Recommendations:
1. The Great World
2. Worlds Apart
3. Dayworld
4. Wicked Dreams
5. A World of Art

---

## Future Improvements

- Add support for additional recommendation algorithms like collaborative filtering.
- Implement a larger, more diverse dataset for better results.
- Enhance the user interface with animations and advanced styling.
- Add pagination for handling larger result sets.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

--- 

Enjoy exploring the **Search Recommendation System**! If you encounter any issues, feel free to open an issue on the repository.
