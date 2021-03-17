import React from 'react';
import { gql, useMutation } from '@apollo/client';
import { useFieldArray, useForm } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';
import { EventType, EventTypeMap, eventTypesAboutStore } from '../utils/types';

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
    inventorychangeSet: [{ productId: undefined, value: 1 }],
  };
  const [createEvent] = useMutation(CREATE_EVENT);

  // eslint-disable-next-line @typescript-eslint/unbound-method
  const {
    control,
    register,
    watch,
    handleSubmit,
    errors,
    reset,
  } = useForm<EventInput>({ defaultValues, shouldUnregister: false });
  const {
    fields: inventoryChangeFields,
    remove,
    append,
  } = useFieldArray<InventoryChangeInput>({
    name: 'inventorychangeSet',
    control,
  });
  const watchEventType = watch('eventType');
  const onSubmit = (eventInput: EventInput) => console.log(eventInput);
  // createEvent({
  //   variables: { eventInput },
  //   refetchQueries: [{ query }],
  // }).then(() => reset());
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
        <input placeholder="입점처" name="storeId" ref={register} />
      )}
      <textarea placeholder="메모" name="description" ref={register} />
      {inventoryChangeFields.map((field, index) => {
        return (
          <div key={field.id}>
            <input
              name={`inventorychangeSet[${index}].productId`}
              ref={register()}
              defaultValue={field.productId}
              required
            />
            <input
              type="number"
              name={`inventorychangeSet[${index}].value`}
              ref={register({
                min: {
                  value: 1,
                  message: '1 이상의 수량만 입력 가능합니다',
                },
              })}
              defaultValue={field.value}
              required
            />
            <button type="button" onClick={() => remove(index)}>
              -
            </button>
            <ErrorMessage
              errors={errors}
              name={`inventorychangeSet[${index}].value`}
              render={({ message }) => (
                <p style={{ color: 'red' }}>{message}</p>
              )}
            />
          </div>
        );
      })}
      <button
        type="button"
        onClick={() =>
          append({
            productId: undefined,
            value: 1,
          })
        }
      >
        Append
      </button>
      <button type="submit">Submit</button>
    </form>
  );
};

export default CreateEvent;
