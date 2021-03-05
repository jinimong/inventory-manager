import React from 'react';
import { useParams } from 'react-router-dom';

const EventDetail = () => {
  const { id } = useParams<{ id: string }>();
  return <div>Event Detail : {id}</div>;
};

export default EventDetail;
