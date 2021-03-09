import React from 'react';
import { gql, useQuery } from '@apollo/client';

type Event = {
  id: number;
  eventType: string;
  createdAt: string;
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
  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  return (
    <div>
      <h3>Events</h3>
      <ul>
        {data.allEvents.map((event) => (
          <li key={event.id}>{event.eventType}</li>
        ))}
      </ul>
    </div>
  );
};

export default Events;
