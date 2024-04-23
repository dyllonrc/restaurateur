// Node imports
import axios from "axios";
import { useEffect, useState } from "react";

// Project imports
import Restaurant from "../../models/Restaurant";

// TODO create reusable API access utilities
const BACKEND_URL = "http://127.0.0.1:8000/";

function RestaurantTable() {
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    axios.get(BACKEND_URL).then(
      (response) => {
        setIsLoaded(true);
        setRestaurants(response.data);
        console.log(response.data);
      },
      (error) => {
        setError(error);
      },
    );
  }, []);

  if (error) {
    console.log(error);
    return <div>Error, check console</div>;
  }

  if (!isLoaded) {
    return <h1>Loading...</h1>;
  }

  console.log(restaurants);
  return (
    <table className="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Price Tier</th>
          <th>User Rating</th>
        </tr>
      </thead>
      <tbody className="table-group-divider">
        {(restaurants as Restaurant[]).map((item) => (
          <tr>
            <td>{item.name}</td>
            <td>{item.priceTier}</td>
            <td>{item.userRating}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default RestaurantTable;
