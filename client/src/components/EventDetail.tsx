import React from 'react';
import { useParams } from 'react-router-dom';
import { gql, useQuery } from '@apollo/client';
import { Event } from '../utils/types';

const EVENT_DETAIL = gql`
  query eventDetail($id: Int!) {
    event(id: $id) {
      eventType
      store {
        id
        name
      }
      description
      inventorychangeSet {
        id
        product {
          id
          name
        }
        count
      }
    }
  }
`;

const EventDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const { loading, error, data } = useQuery<{
    event: Event;
  }>(EVENT_DETAIL, { variables: { id: +id } });
  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  const {
    event: { eventType, store, description, inventorychangeSet },
  } = data;
  return (
    <div>
      <h3>Event Detail</h3>
      <hr />
      <div>
        <span>event type: </span>
        <span>{eventType}</span>
      </div>
      {store && (
        <div>
          <span>store: </span>
          <span>{store.name}</span>
        </div>
      )}
      {description && (
        <div>
          <span>description: </span>
          <span>{description}</span>
        </div>
      )}
      <hr />
      <ul>
        {inventorychangeSet.map((inventoryChange) => (
          <li
            key={inventoryChange.id}
          >{`${inventoryChange.product.name} : ${inventoryChange.count}`}</li>
        ))}
      </ul>
    </div>
  );
};

export default EventDetail;
