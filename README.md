# 🧩 Customer Segmentation on US

Welcome to the **Customer Segmentation on US** project!

In this project, I explore real-world financial data from the **2019 Survey of Consumer Finances (SCF)** to identify and analyze credit-challenged households in the United States.  
The main idea is to apply **unsupervised learning (K-Means Clustering)** to segment households based on their financial and demographic attributes, and to visualize insights that help understand different consumer groups in the U.S. economy.

---

## 📊 Overview

The main goal of this project is to:
1. Identify households with difficulties accessing credit.
2. Cluster these households into meaningful subgroups using K-Means.
3. Build interactive visualizations to analyze and communicate insights.

This process covers all the main stages of data science — from **data exploration** and **preprocessing** to **modeling** and **visualization**.

Such an analysis can be applied in:
- Marketing and customer segmentation.
- Sociological or economic research.
- Financial risk and lending strategy.

---

## 🧠 What You’ll Learn

By going through this project, you’ll gain experience in:
- Data cleaning and preprocessing of real-world financial datasets.
- Feature selection based on variance and correlation.
- Applying **K-Means clustering** and evaluating results with:
  - Inertia
  - Silhouette Score
- Using **Principal Component Analysis (PCA)** for dimensionality reduction.
- Visualizing data using **Plotly Express**, **matplotlib**, and **seaborn**.
- Structuring your project modularly using **SOLID principles**.

---


## 🧩 Methodology

### 1. **Data Exploration (1_Data_Exploration.ipynb)**
- The data used comes from the **2019 Survey of Consumer Finances (SCF)**, published by the **Federal Reserve Board of the United States**.  
  This dataset provides detailed information on U.S. households’ balance sheets, income, debt, and demographic characteristics.
- In this stage:
  - Reviewed the data dictionary to understand feature meanings.
  - Focused on both **demographic** (e.g., `AGE`, `RACE`, `EDUCATION`)  
    and **financial** variables (e.g., `INCOME`, `DEBT`, `ASSETS`, `HOUSES`).
  - Conducted exploratory visualizations using `matplotlib`, `seaborn`, and `plotly.express`.

---

### 2. **Data Preparation (2_Data_preparation.ipynb)**
- Performed **data cleaning** and **feature selection**:
  - Removed irrelevant or redundant variables.
  - Selected top 10 features based on variance, then refined to 5 after handling outliers.
  - Used **trimmed variance** to avoid distortion from extreme values.
- Final dataset shape: **(28885, 351)** → reduced to top **5 informative features** for clustering.
- Saved the cleaned data in `data.csv` for the next stage.

---

### 3. **Modeling (3_Modeling.ipynb)**
- Built a **K-Means clustering pipeline** using:
  - `StandardScaler` for normalization.
  - `KMeans` for unsupervised learning.
- Implemented a function (in `model_selection.py`) to loop through cluster numbers (from 2 to 12) and record:
  - **Inertia values**
  - **Silhouette scores**
- Visualized both metrics to choose the optimal cluster count.
- Selected the model with the best silhouette score.

#### 🧩 Visualization & Insights
- Grouped features by cluster and calculated averages to compare cluster behaviors.
- Used bar charts to show financial differences between clusters.
- Applied **PCA** to reduce data dimensions and visualize clusters in 2D.
- Visualized cluster distribution with interactive **Plotly** scatter plots to understand how each variable affects the segmentation.

---

## 🛠️ Technologies Used

| Category | Tools / Libraries |
|-----------|------------------|
| Language | Python |
| Data Analysis | pandas, numpy |
| Visualization | matplotlib, seaborn, plotly.express |
| Machine Learning | scikit-learn |
| Dimensionality Reduction | PCA |
| Environment | Google Colab |
| Version Control | Git & GitHub |

---

## 🚀 How to Run the Project

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Mo7amedMok5tar/Customer-Segmentation-on-US.git
cd Customer-Segmentation-on-US

# 2️⃣ Open the notebooks in Google Colab or Jupyter Notebook
# 3️⃣ Run each notebook in order:
1_Data_Exploration.ipynb
2_Data_preparation.ipynb
3_Modeling.ipynb

# 4️⃣ Explore the visualizations and interpret the clustering results

--- 
🧾 **License**  
This project is for educational and research purposes only.  
You can reuse, modify, or expand it for learning or analysis.  

---

👨‍💻 **Author**  
**Mohamed Mokhtar**  
Data Science & Machine Learning  

📞 0155562027  
📧 mohamedmokhtar26027@gmail.com  
🔗 [linkedin.com/in/mohamed-mokhtar-779b4a254](https://www.linkedin.com/in/mohamed-mokhtar-779b4a254)

