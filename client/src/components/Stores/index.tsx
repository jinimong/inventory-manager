import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useQuery } from '@apollo/client';
import { Store } from '../../utils/types';
import query from './query';
import CreateStore from '../CreateStore';

const Stores: React.FC = () => {
  const { loading, error, data } = useQuery<{
    allStores: Store[];
  }>(query);
  const { pathname } = useLocation();
  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  return (
    <div>
      <h3>Stores</h3>
      <hr />
      <CreateStore />
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
