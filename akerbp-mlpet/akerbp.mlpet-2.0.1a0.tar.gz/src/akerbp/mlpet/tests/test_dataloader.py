from cognite.client import CogniteClient

from akerbp.mlpet.dataloader import DataLoader

client = CogniteClient(client_name="test", project="akbp-subsurface")


def test_load_from_cdf():
    dl = DataLoader()
    df = dl.load_from_cdf(
        client=client, metadata={"wellbore_name": "25/2-7", "subtype": "BEST"}
    )
    assert df.shape[0] > 0


def test_load_from_las():
    dl = DataLoader()

    dl.load_from_las(
        [
            "src/akerbp/mlpet/tests/data/15_9-23.las",
            "src/akerbp/mlpet/tests/data/25_2-7.las",
            "src/akerbp/mlpet/tests/data/35_12-1.las",
        ]
    )
