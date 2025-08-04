from src.data_loader import load_and_save_data


def test_data_loading():
    df = load_and_save_data()
    assert df.shape[0] > 0
    assert "MedHouseVal" in df.columns
