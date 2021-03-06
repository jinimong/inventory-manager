import { gql, useQuery } from '@apollo/client';
import React, { useState } from 'react';
import Select from 'react-select';
import { Controller, useFieldArray, UseFormMethods } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';
import { OptionType, Store } from '../../utils/types';
import { EventInput, InventoryChangeInput } from './types';

const STORE_DETAIL = gql`
  query storeDetail($id: Int!) {
    store(id: $id) {
      name
      description
      storeProducts {
        id
        product {
          id
          name
        }
        count
      }
      events {
        id
        eventType
        createdAt
      }
    }
  }
`;

const InventoryChangeFromStoreFields: React.FC<{
  storeId?: number;
  form: UseFormMethods<EventInput>;
}> = ({ storeId, form: { control, register, errors } }) => {
  const [products, setProducts] = useState<(string | number)[]>([]);
  const { loading, error, data } = useQuery<{
    store: Store;
  }>(STORE_DETAIL, { variables: { id: storeId } });

  const { fields, remove, append } = useFieldArray<InventoryChangeInput>({
    name: 'inventoryChanges',
    control,
  });

  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  const { store } = data;
  const validProducts = store.storeProducts.filter(
    (storeProduct) => storeProduct.count > 0,
  );
  const productCountMap = new Map(
    validProducts.map((storeProduct) => [
      storeProduct.product.id.toString(),
      storeProduct.count,
    ]),
  );

  return (
    <>
      <button
        type="button"
        onClick={() =>
          append({
            productId: undefined,
            value: 1,
          })
        }
        disabled={fields.length === validProducts.length}
      >
        Append
      </button>
      {fields.map((field, index) => {
        const otherFieldSelect = products.filter(
          (value, fieldIndex) => index !== fieldIndex,
        );
        const options = validProducts
          .filter(
            (storeProduct) =>
              !otherFieldSelect.includes(storeProduct.product.id),
          )
          .map((storeProduct) => ({
            label: `${storeProduct.product.name}`,
            value: storeProduct.product.id,
          }));
        const selectProduct = products[index];
        const max = selectProduct
          ? productCountMap.get(selectProduct.toString())
          : 1;
        return (
          <div key={field.id} style={{ padding: '20px' }}>
            <Controller
              name={`inventoryChanges[${index}].productId`}
              style={{ width: '100%' }}
              control={control}
              render={({ onChange, ref }) => (
                <Select
                  isLoading={loading}
                  onChange={(value, actionMeta) => {
                    const productId = (value as OptionType).value;
                    onChange(productId, actionMeta);
                    const newProducts = [...products];
                    newProducts[index] = productId;
                    setProducts(newProducts);
                  }}
                  inputRef={ref}
                  options={options}
                  required
                />
              )}
            />
            {selectProduct && (
              <>
                <span>변화수량</span>
                <input
                  type="number"
                  name={`inventoryChanges[${index}].value`}
                  ref={register}
                  defaultValue={field.value}
                  min={1}
                  max={max}
                  required
                />
              </>
            )}
            {fields.length > 1 && (
              <button type="button" onClick={() => remove(index)}>
                -
              </button>
            )}
            <ErrorMessage
              errors={errors}
              name={`inventoryChanges[${index}].value`}
              render={({ message }) => (
                <p style={{ color: 'red' }}>{message}</p>
              )}
            />
          </div>
        );
      })}
    </>
  );
};

export default InventoryChangeFromStoreFields;
