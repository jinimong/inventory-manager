import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { gql, useQuery } from '@apollo/client';
import { Store } from '../utils/types';

const STORES = gql`
  query {
    allStores {
      id
      name
    }
  }
`;

const Stores: React.FC = () => {
  const { loading, error, data } = useQuery<{
    allStores: Store[];
  }>(STORES);
  const { pathname } = useLocation();
  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  return (
    <div>
      <h3>Stores</h3>
      <hr />
      <ul>
        {data.allStores.map((store) => (
          <li key={store.id}>
            <Link to={`${pathname}/${store.id}`}>
              <span>{store.name}</span>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Stores;
