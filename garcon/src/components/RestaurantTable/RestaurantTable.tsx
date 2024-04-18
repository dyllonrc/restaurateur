const dummyList: string[][] = [
  ["McDonald's", "$", "3/5"],
  ["Five Guys", "$$", "3.5/5"],
  ["Emmy Squared Pizzeria", "$$$", "4/5"],
  ["Eleven Madison Park", "$$$$", "4.9/5"],
];

function RestaurantTable() {
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
        {dummyList.map((item) => (
          <tr>
            <td>{item[0]}</td>
            <td>{item[1]}</td>
            <td>{item[2]}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default RestaurantTable;
