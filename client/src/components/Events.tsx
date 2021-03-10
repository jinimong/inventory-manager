import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { gql, useQuery } from '@apollo/client';
import { Event } from '../utils/types';

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
  const { loading, error, data } = useQuery<{
    allEvents: Event[];
  }>(EVENTS);
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
