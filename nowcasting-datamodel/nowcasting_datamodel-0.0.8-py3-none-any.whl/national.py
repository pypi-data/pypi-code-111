""" Make national forecasts """
import logging
from typing import List

import pandas as pd

from nowcasting_datamodel import N_GSP
from nowcasting_datamodel.models import (
    Forecast,
    ForecastSQL,
    ForecastValue,
    Location,
    national_gb_label,
)

logger = logging.getLogger(__name__)


def make_national_forecast(forecasts: List[Forecast], n_gsps: int = N_GSP) -> ForecastSQL:
    """This takes a list of forecast and adds up all the forecast values

    Note that a different method to do this, would be to do this in the database
    """
    assert (
        len(forecasts) == n_gsps
    ), f"The number of forecast was only {len(forecasts)}, it should be {n_gsps}"

    # check the gsp ids are unique
    gsps = [int(f.location.gsp_id) for f in forecasts]
    seen = set()
    dupes = [x for x in gsps if x in seen or seen.add(x)]
    assert len(seen) == n_gsps, f"Found non unique GSP ids {dupes}"

    location = Location(label=national_gb_label)

    # make pandas dataframe of all the forecast values with a gsp id
    forecast_values_flat = []
    for forecast in forecasts:

        gsp_id = forecast.location.gsp_id

        one_gsp = pd.DataFrame(
            [ForecastValue.from_orm(value).dict() for value in forecast.forecast_values]
        )
        one_gsp["gps_id"] = gsp_id
        # this is a data frame with the follow columns
        # - gps_id
        # - target_time
        # - expected_power_generation_megawatts

        forecast_values_flat.append(one_gsp)

    forecast_values = pd.concat(forecast_values_flat)
    forecast_values[
        "count"
    ] = 1  # this will be used later to check that there are 338 forecasts for each target_time

    # group by target time
    forecast_values = forecast_values.groupby(["target_time"]).sum()
    forecast_values.reset_index(inplace=True)
    if (forecast_values["count"] != n_gsps).all():
        m = f'The should should be {n_gsps}, but instead it is {forecast_values["count"]}'
        logger.debug(m)
        raise Exception(m)

    # change back to ForecastValue
    forecast_values = [
        ForecastValue(**forecast_value) for forecast_value in forecast_values.to_dict("records")
    ]

    return Forecast(
        forecast_values=forecast_values,
        location=location,
        model=forecasts[0].model,
        input_data_last_updated=forecasts[0].input_data_last_updated,
        forecast_creation_time=forecasts[0].forecast_creation_time,
    ).to_orm()
