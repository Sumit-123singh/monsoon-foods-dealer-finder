import pandas as pd

import config
from utils import haversine_distance, normalize_query


class DealerService:

    def __init__(self):
        """
        Load dealer CSV only once
        when the application starts.
        """

        self.dealers = pd.read_csv(config.CSV_FILE)

    # ----------------------------------------

    def search(self, query: str):

        """
        Search dealer by

        - Name
        - District
        - Pincode
        """

        query = normalize_query(query)

        results = []

        for _, dealer in self.dealers.iterrows():

            if (
                query in str(dealer["name"]).lower()
                or query in str(dealer["district"]).lower()
                or query == str(dealer["pincode"])
            ):

                results.append({
                    "id": dealer.get("id", None),
                    "name": dealer["name"],
                    "district": dealer["district"],
                    "pincode": str(dealer["pincode"]),
                    "phone": str(dealer["phone"]),
                    "latitude": dealer["latitude"],
                    "longitude": dealer["longitude"],
                    "distance": None
                })

        return results

    # ----------------------------------------

    def nearest(
        self,
        latitude: float,
        longitude: float
    ):

        """
        Find nearest dealers.

        Returns only
        MAX_RESULTS dealers.
        """

        dealers = []

        for _, dealer in self.dealers.iterrows():

            distance = haversine_distance(
                latitude,
                longitude,
                dealer["latitude"],
                dealer["longitude"]
            )

            dealers.append({

                "id": dealer.get("id", None),

                "name": dealer["name"],

                "district": dealer["district"],

                "pincode": str(dealer["pincode"]),

                "phone": str(dealer["phone"]),

                "latitude": dealer["latitude"],

                "longitude": dealer["longitude"],

                "distance": distance
            })

        dealers.sort(
            key=lambda dealer: dealer["distance"]
        )

        return dealers[:config.MAX_RESULTS]