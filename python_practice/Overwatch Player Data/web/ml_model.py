from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
import joblib
import os

# --- ML functions ---
def train_pipeline(df, target_stat):
    categorical_cols = ['Season', 'Hero']
    numerical_cols = [c for c in df.columns if c not in categorical_cols + [target_stat]]

    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('model', LinearRegression())
    ])

    X = df.drop(columns=[target_stat])
    y = df[target_stat]
    pipeline.fit(X, y)

    return pipeline

def save_pipeline(pipeline, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    joblib.dump(pipeline, filename)

def load_pipeline(filename):
    return joblib.load(filename)

def predict(pipeline, df_new):
    return pipeline.predict(df_new)

# --- Function to train & save pipelines for all numeric stats ---
def train_and_save_all_pipelines(df, categorical_cols=['Season', 'Hero'], models_dir='models'):
    stats_list = [col for col in df.columns if col not in categorical_cols]
    
    for stat in stats_list:
        pipeline = train_pipeline(df, stat)
        filename = f"{models_dir}/pipeline_{stat.replace(' ', '_')}.pkl"
        save_pipeline(pipeline, filename)
