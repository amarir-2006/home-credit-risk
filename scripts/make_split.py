"Split application_train.csv into train and holdout. Run once"

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

RAW = Path("data/raw/application_train.csv")
OUT = Path("data/interm")
SEED = 42


def main() -> None:
    df = pd.read_csv(RAW)
    train, holdout = train_test_split(
        df, test_size=0.2, stratify=df["TARGET"], random_state=SEED
    )

    OUT.mkdir(parents=True, exist_ok=True)
    train.to_csv(OUT / "train.csv", index=False)
    holdout.to_csv(OUT / "holdout.csv", index=False)

    assert set(train["SK_ID_CURR"]).isdisjoint(holdout["SK_ID_CURR"])
    print(f"train:   {len(train):,} rows, default rate {train['TARGET'].mean():.4f}")
    print(
        f"holdout: {len(holdout):,} rows, default rate {holdout['TARGET'].mean():.4f}"
    )


if __name__ == "__main__":
    main()
