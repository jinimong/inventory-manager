import React from 'react';
import { useParams } from 'react-router-dom';
import { gql, useQuery } from '@apollo/client';
import { Store } from '../utils/types';

const STORE_DETAIL = gql`
  query storeDetail($id: Int!) {
    store(id: $id) {
      name
      description
      storeProducts {
        id
        product {
          id
          name
        }
        count
      }
      events {
        id
        eventType
        createdAt
      }
    }
  }
`;

const StoreDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const { loading, error, data } = useQuery<{
    store: Store;
  }>(STORE_DETAIL, { variables: { id: +id } });

  if (loading || error || !data) {
    return <div>Loading...</div>;
  }

  const {
    store: { name, description, storeProducts, events },
  } = data;

  return (
    <div>
      <h3>Store Detail</h3>
      <hr />
      <div>
        <span>name: </span>
        <span>{name}</span>
      </div>
      {description && (
        <div>
          <span>description: </span>
          <span>{description}</span>
        </div>
      )}
      <hr />
      {storeProducts.length ? (
        <ul>
          {storeProducts.map((storeProduct) => (
            <li key={storeProduct.id}>
              <span>{storeProduct.product.name}</span>
              <span>{storeProduct.count}</span>
            </li>
          ))}
        </ul>
      ) : (
        <div>입고된 상품 없음</div>
      )}
      <hr />
      {events.length ? (
        <ul>
          {events.map((event) => (
            <li key={event.id}>
              <span>{event.eventType}</span>
              <span>{event.createdAt}</span>
            </li>
          ))}
        </ul>
      ) : (
        <div>기록 없음</div>
      )}
    </div>
  );
};

export default StoreDetail;
