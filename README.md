# Red Wine Dataset Analysis

This repository presents an in-depth analysis of the Red Wine Quality dataset. The primary objective is to explore the dataset's characteristics and develop predictive models to estimate wine quality based on physicochemical properties.

## Table of Contents

- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The analysis utilizes the [Red Wine Quality dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) from the UCI Machine Learning Repository. This dataset comprises 1,599 instances of red wine samples, each characterized by 11 physicochemical attributes and a quality score ranging from 0 to 10.

## Project Structure

The repository is organized as follows:

```
Red_Wine_Dataset/
├── data/
│   └── winequality-red.csv
├── notebooks/
│   ├── eda.ipynb
│   ├── rf_model.ipynb
│   └── svc_model.ipynb
├── src/
│   ├── gradio_app.py
│   ├── gradio/
├── Outputs/
│   ├── models/
│   ├── plots/
├── requirements.txt
└── README.md
```

- **data/**: Contains the raw dataset file.
- **notebooks/**: Jupyter notebooks detailing each step of the analysis.
- **src/**: Python scripts for data modeling and application interface.
- **requirements.txt**: Lists the Python dependencies required to run the project.
- **Outputs/**: Contains all the plots and models trained.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Saber0722/Red_Wine_Dataset.git
   cd Red_Wine_Dataset
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Exploratory Data Analysis:**

   Use the `eda.ipynb` notebook to visualize and understand the relationships between different features.

2. **Model Training:**

   Execute the `rf_model.ipynb` and `svc_model.ipynb` notebooks to train machine learning models and evaluate their performance in predicting wine quality.

## Results

The analysis includes:

- Identification of key features influencing wine quality.
- Performance metrics of various machine learning models.
- Visualizations illustrating feature distributions and model predictions.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
