import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { gql, useQuery } from '@apollo/client';
import moment from 'moment';
import 'moment/locale/ko';
import Tooltip from '@material-ui/core/tooltip';
import { Event, EventTypeMap } from '../utils/types';

const EVENTS = gql`
  query {
    allEvents {
      id
      eventType
      createdAt
    }
  }
`;

const Events: React.FC = () => {
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
      <hr />
      <Link to={`${pathname}/new`}>Create Event</Link>
      <hr />
      <ul>
        {data.allEvents.map((event) => {
          const createdMoment = moment(event.createdAt);
          return (
            <li key={event.id}>
              <Link to={`${pathname}/${event.id}`}>
                <span>{EventTypeMap.get(event.eventType)}</span>
                <Tooltip
                  title={createdMoment.format('YYYY-MM-DD HH:MM')}
                  placement="right"
                >
                  <span>{`(${createdMoment.fromNow()})`}</span>
                </Tooltip>
              </Link>
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default Events;
