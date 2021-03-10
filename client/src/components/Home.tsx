import React from 'react';
import { Link } from 'react-router-dom';

const Home: React.FC = () => {
  return (
    <div>
      <h3>Home!</h3>
      <hr />
      <ul>
        <li>
          <Link to="/events">Events</Link>
        </li>
        <li>
          <Link to="/products">Products</Link>
        </li>
        <li>
          <Link to="/stores">Stores</Link>
        </li>
      </ul>
    </div>
  );
};

export default Home;
