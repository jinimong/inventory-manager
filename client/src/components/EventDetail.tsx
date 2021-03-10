import React from 'react';
import { useParams } from 'react-router-dom';
import { gql, useQuery } from '@apollo/client';
import { Event } from './Events';

type EventDetail = {
  event: Event;
};

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

const EventDetail = () => {
  const { id } = useParams<{ id: string }>();
  const { loading, error, data } = useQuery<EventDetail>(EVENT_DETAIL, {
    variables: { id: +id },
  });
  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  const {
    event: { eventType, store, description, inventorychangeSet },
  } = data;
  return (
    <div>
      <h3>Event Detail</h3>
      {store && (
        <div>
          <label>store: </label>
          <span>{store.name}</span>
        </div>
      )}
      <div>
        <label>description: </label>
        <span>{description}</span>
      </div>
      <div>
        <label>event type: </label>
        <span>{eventType}</span>
      </div>
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
