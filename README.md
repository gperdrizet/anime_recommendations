# Anime Recommendations

This repository demonstrates set-up and deployment of a simple Streamlit web application with a content-based filtering recommendation system that suggests similar anime titles based on genre similarity using the Jaccard distance metric.

View the live deployment here: [anime-recommendations-qtbq.onrender.com](https://anime-recommendations-qtbq.onrender.com)

## Overview

This project implements a simple yet effective anime recommendation engine that:
- Analyzes anime genres to find similar titles
- Uses Jaccard similarity (intersection over union) to measure genre overlap
- Provides an interactive web interface built with Streamlit
- Returns the top 5 most similar anime for any selected title

The dataset includes over 12,000 anime titles with information about genres, ratings, and popularity metrics.

## Try It in GitHub Codespaces

The easiest way to try running this app yourself is using GitHub Codespaces, which provides a fully configured development environment in your browser:

1. **Fork this repository** to your GitHub account
2. **Open in Codespaces**:
   - Click the green `<> Code` button on your forked repository
   - Select the **Codespaces** tab
   - Click **Create codespace on main**
3. **Wait for setup** - The container will automatically install dependencies and run the app
4. **Access the app** - A popup will appear asking to open the browser. Click **Open in Browser**, or visit `http://localhost:8501`

The Codespace includes Python 3.12, all required packages, and VS Code extensions pre-configured.

## Fork, Clone & Run Locally

### Prerequisites
- Python 3.10 or higher
- pip package manager
- Git

### Setup Instructions

1. **Fork the repository** on GitHub (click the Fork button)

2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/anime-recommendations.git
   cd anime-recommendations
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit app**:
   ```bash
   streamlit run src/app.py
   ```

6. **Open your browser** to `http://localhost:8501`

### Explore the Notebook

To explore the data analysis and recommendation algorithm, see `notebooks/content_based_filtering.ipynb`.

## Deploy to Render.com

Deploy your own instance of this app to Render.com for free:

### Step 1: Prepare Your Repository

1. **Fork this repository** to your GitHub account if you haven't already

### Step 2: Deploy on Render

1. **Sign up** for a free account at [render.com](https://render.com)

2. **Create a new Web Service**:
   - Click **New +** → **Web Service**
   - Connect your GitHub account if not already connected
   - Select your forked `anime-recommendations` repository

3. **Configure the service**:
   - **Name**: Choose a unique name (e.g., `my-anime-recommendations`)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run src/app.py --server.port=$PORT --server.address=0.0.0.0`

4. **Set environment settings** (optional):
   - **Instance Type**: `Free` (sufficient for this app)
   - **Auto-Deploy**: Enable to automatically deploy on git push to your fork

5. **Click "Create Web Service"**

6. **Wait for deployment** - Render will:
   - Clone your repository
   - Install dependencies
   - Start the Streamlit app
   - Provide you with a public URL (e.g., `https://my-anime-recommendations.onrender.com`)

### Deployment Notes

- **First load delay**: Free tier instances spin down after inactivity. The first request may take 30-60 seconds to wake up.
- **Custom domain**: You can add a custom domain in Render's settings.
- **Updates**: Push to your GitHub repo to trigger automatic redeployment (if auto-deploy is enabled).

## Project Structure

```
anime-recommendations/
├── data/
│   ├── anime.csv                          # Raw anime dataset
│   └── processed_animes.parquet           # Preprocessed data with genre sets
├── notebooks/
│   └── content_based_filtering.ipynb      # Jupyter notebook with analysis
├── src/
│   └── app.py                             # Streamlit web application
├── .devcontainer/
│   └── devcontainer.json                  # VS Code dev container config
├── requirements.txt                       # Python dependencies
└── README.md
```

## Technology Stack

- **Python 3.12** - Programming language
- **Pandas** - Data manipulation and analysis
- **Streamlit** - Web interface framework
- **Jupyter** - Interactive notebook environment

## Contributing

Feel free to fork this project and customize it.

## License

See [LICENSE](LICENSE) file for details.

## Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Jaccard Similarity](https://en.wikipedia.org/wiki/Jaccard_index)
