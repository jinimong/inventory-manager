import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
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
      </ul>
    </div>
  );
};

export default Home;
