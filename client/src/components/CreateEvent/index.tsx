import React from 'react';
import { gql, useMutation } from '@apollo/client';
import { useForm } from 'react-hook-form';
import { useHistory } from 'react-router-dom';
import {
  EventType,
  EventTypeMap,
  eventTypesAboutStore,
} from '../../utils/types';
import { EventInput } from './types';
import InventoryChangeFields from './InventoryChangeFields';
import StoreIdField from './StoreIdField';

const CREATE_EVENT = gql`
  mutation CreateEvent($eventInput: EventInput) {
    createEvent(eventInput: $eventInput) {
      event {
        id
      }
    }
  }
`;

const CreateEvent: React.FC = () => {
  const defaultValues = {
    eventType: '',
    storeId: undefined,
    description: '',
    inventorychangeSet: [{ productId: undefined, value: 1 }],
  };
  const [createEvent] = useMutation(CREATE_EVENT);

  const form = useForm<EventInput>({ defaultValues, shouldUnregister: false });
  // eslint-disable-next-line @typescript-eslint/unbound-method
  const { register, watch, handleSubmit } = form;

  const history = useHistory();

  const watchEventType = watch('eventType');
  const onSubmit = (eventInput: EventInput) =>
    createEvent({
      variables: { eventInput },
    }).then(() => history.push('/events'));

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <select name="eventType" ref={register} required>
        {Array.from(EventTypeMap).map(([key, value]) => (
          <option key={key} value={key}>
            {value}
          </option>
        ))}
      </select>
      {eventTypesAboutStore.includes(watchEventType as EventType) && (
        <StoreIdField {...form} />
      )}
      <textarea placeholder="메모" name="description" ref={register} />
      <InventoryChangeFields {...form} />
      <button type="submit">Submit</button>
    </form>
  );
};

export default CreateEvent;
