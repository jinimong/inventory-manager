import { gql, useQuery } from '@apollo/client';
import React, { useState } from 'react';
import Select from 'react-select';
import { Controller, useFieldArray, UseFormMethods } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';
import { Product, OptionType } from '../../utils/types';
import { EventInput, InventoryChangeInput } from './types';

const PRODUCTS = gql`
  query {
    allProducts {
      id
      name
    }
  }
`;

const InventoryChangeFields: React.FC<UseFormMethods<EventInput>> = ({
  control,
  register,
  errors,
}) => {
  const [products, setProducts] = useState<(string | number)[]>([]);
  const { loading, error, data } = useQuery<{
    allProducts: Product[];
  }>(PRODUCTS);

  const { fields, remove, append } = useFieldArray<InventoryChangeInput>({
    name: 'inventorychangeSet',
    control,
  });

  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  const { allProducts } = data;

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
        disabled={fields.length === allProducts.length}
      >
        Append
      </button>
      {fields.map((field, index) => {
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
            {fields.length > 1 && (
              <button type="button" onClick={() => remove(index)}>
                -
              </button>
            )}
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
    </>
  );
};

export default InventoryChangeFields;
