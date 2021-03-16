import React from 'react';
import { gql, useMutation } from '@apollo/client';
import { useForm } from 'react-hook-form';

type InventoryChangeInput = {
  productId: number;
  value: number;
};

type EventInput = {
  eventType: string;
  storeId?: number;
  description?: string;
  inventorychangeSet: InventoryChangeInput[];
};

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
    inventorychangeSet: [],
  };
  const [createEvent] = useMutation(CREATE_EVENT);

  // eslint-disable-next-line @typescript-eslint/unbound-method
  const { control, register, handleSubmit, reset } = useForm<EventInput>({
    defaultValues,
  });
  const onSubmit = (eventInput: EventInput) => console.log(eventInput);
  // createEvent({
  //   variables: { eventInput },
  //   refetchQueries: [{ query }],
  // }).then(() => reset());
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input placeholder="Type" name="eventType" ref={register} required />
      <input placeholder="입점처" name="storeId" ref={register} />
      <textarea placeholder="메모" name="description" ref={register} />
      <button type="submit">Submit</button>
    </form>
  );
};

export default CreateEvent;
