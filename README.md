# IPL Statistics Analyzer 🏏📊

An interactive web application for analyzing **Indian Premier League (IPL) cricket statistics** using Python and Streamlit. The project provides player, team, and season analysis along with searching, sorting, comparisons, records, and interactive visualizations.

## 🎯 Aim

To develop an interactive and user-friendly web application that analyzes IPL cricket data and presents meaningful insights through statistics, charts, and dashboards while demonstrating practical searching and sorting algorithms.

## ✨ Features

* 🏏 Player Statistics Analysis
* 🔎 Player Search
* 👥 Player Comparison
* 🏆 Team-wise Analysis
* 📅 Season-wise Analysis
* 📈 Interactive Data Visualizations
* 🏅 IPL Records
* ⚡ Algorithm Playground
* 📊 Statistical Tables and Metrics
* 🎨 User-friendly Streamlit Interface

## 🛠️ Technologies Used

| Technology   | Purpose                 |
| ------------ | ----------------------- |
| Python       | Application development |
| Streamlit    | Web interface           |
| Pandas       | Data processing         |
| NumPy        | Numerical operations    |
| Plotly       | Interactive charts      |
| CSV          | Data storage/source     |
| VS Code      | Development             |
| Git & GitHub | Version control         |

## 🧠 Algorithms Used

The project demonstrates the following searching and sorting algorithms:

* **Linear Search** – searches elements sequentially.
* **Merge Sort** – sorts data using divide-and-conquer.
* **Quick Sort** – efficiently sorts data using a pivot.
* **Heap Sort** – sorts data using a heap data structure.

## 📂 Project Structure

```text
ipl-stat-analyzer/
│
├── algorithms/
│   ├── linear_search.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── heap_sort.py
│   ├── performance.py
│   └── __init__.py
│
├── data/
│   └── IPL CSV datasets
│
├── pages/
│   ├── dashboard.py
│   ├── player_analysis.py
│   ├── player_comparison.py
│   ├── team_analysis.py
│   ├── season_analysis.py
│   ├── records.py
│   ├── visualizations.py
│   └── algorithm_playground.py
│
├── utils/
│   ├── data_loader.py
│   ├── analytics.py
│   ├── charts.py
│   ├── preprocessing.py
│   ├── helpers.py
│   └── __init__.py
│
├── components/
├── assets/
├── screenshots/
├── app.py
├── styles.css
├── requirements.txt
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/1Sanchit/winning-camp.git
```

### 2. Open the project folder

```bash
cd winning-camp
```

### 3. Install dependencies

```bash
py -m pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
py -m streamlit run app.py
```

### 5. Open in Browser

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

## 📊 Data Source

The application currently uses **IPL data stored in CSV files**. Pandas is used to load and process the datasets.

> **Note:** This version does not use an external IPL API or MySQL/MongoDB database.

## 🔄 System Workflow

```text
IPL CSV Dataset
      ↓
Data Loading
      ↓
Data Preprocessing
      ↓
Searching / Sorting
      ↓
Statistical Analysis
      ↓
Streamlit Interface
      ↓
Charts & Results
```

## 🎓 Academic Information

**Project Title:** IPL Statistics Analyzer
**Student:** Sanchit Parmar
**Program:** MCA – Cloud Computing and DevOps
**Semester:** 1st Semester
**Project Guide:** Deepali Saini

## 🔮 Future Scope

* Live IPL API integration
* Machine Learning-based predictions
* MySQL/MongoDB database integration
* Advanced player performance analytics
* Real-time IPL statistics
* Cloud deployment
* Mobile application support

## 👨‍💻 Author

**Sanchit Parmar**

MCA – Cloud Computing and DevOps

## 📄 License

This project is developed for **academic and educational purposes**.
