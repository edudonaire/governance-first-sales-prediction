from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"


def load_data(layer: str, filename: str) -> pd.DataFrame:
    """
    Load dataset from a specific data layer.

    layer: bronze | raw | silver | gold
    filename: file name (with extension)
    """
    path = DATA_DIR / layer / filename

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    return pd.read_csv(path)


def save_data(df: pd.DataFrame, layer: str, filename: str):
    """
    Save dataset to a specific data layer.
    """
    path = DATA_DIR / layer / filename
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)
