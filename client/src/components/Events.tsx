import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { gql, useQuery } from '@apollo/client';

type Product = {
  id: number;
  name: string;
  count: number;
};

type InventoryChange = {
  id: number;
  product: Product;
  count: number;
};

type Store = {
  id: number;
  name: string;
  description: string;
  eventSet: Event[];
};

export type Event = {
  id: number;
  eventType: string;
  createdAt: string;
  updatedAt: string;
  description: string;
  store: Store;
  inventorychangeSet: InventoryChange[];
};

type AllEvents = {
  allEvents: Event[];
};

const EVENTS = gql`
  query {
    allEvents {
      id
      eventType
      createdAt
    }
  }
`;

const Events = () => {
  const { loading, error, data } = useQuery<AllEvents>(EVENTS);
  const { pathname } = useLocation();
  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  return (
    <div>
      <h3>Events</h3>
      <ul>
        {data.allEvents.map((event) => (
          <li key={event.id}>
            <Link to={`${pathname}/${event.id}`}>{event.eventType}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Events;
