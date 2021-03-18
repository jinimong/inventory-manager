import React, { useState } from 'react';
import { gql, useMutation, useQuery } from '@apollo/client';
import { Controller, useFieldArray, useForm } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';
import Select from 'react-select';
import {
  EventType,
  Product,
  EventTypeMap,
  eventTypesAboutStore,
  OptionType,
} from '../utils/types';

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

const PRODUCTS = gql`
  query {
    allProducts {
      id
      name
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
  const { loading, error, data } = useQuery<{
    allProducts: Product[];
  }>(PRODUCTS);

  const [products, setProducts] = useState<(string | number)[]>([]);

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

  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  const { allProducts } = data;

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
        const otherFieldSelect = products.filter(
          (value, fieldIndex) => index !== fieldIndex,
        );
        const options = allProducts
          .filter((product) => !otherFieldSelect.includes(product.id))
          .map((product) => ({
            label: product.name,
            value: product.id,
          }));
        return (
          <div key={field.id}>
            <Controller
              name={`inventorychangeSet[${index}].productId`}
              control={control}
              render={({ onChange, ref }) => (
                <Select
                  onChange={(value, actionMeta) => {
                    const productId = (value as OptionType).value;
                    onChange(productId, actionMeta);
                    const newProducts = [...products];
                    newProducts[index] = productId;
                    setProducts(newProducts);
                  }}
                  inputRef={ref}
                  options={options}
                />
              )}
              options={options}
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
        disabled={inventoryChangeFields.length === allProducts.length}
      >
        Append
      </button>
      <button type="submit">Submit</button>
    </form>
  );
};

export default CreateEvent;
