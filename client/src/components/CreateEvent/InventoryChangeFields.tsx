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
      count
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
  const validProducts = allProducts.filter((product) => product.count > 0);
  const productCountMap = new Map(
    validProducts.map((product) => [product.id.toString(), product.count]),
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
          .filter((product) => !otherFieldSelect.includes(product.id))
          .map((product) => ({
            label: `${product.name} (${product.count}개 보유)`,
            value: product.id,
          }));
        const selectProduct = products[index];
        const max = selectProduct
          ? productCountMap.get(selectProduct.toString())
          : 1;
        return (
          <div key={field.id} style={{ padding: '20px' }}>
            <Controller
              name={`inventorychangeSet[${index}].productId`}
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
                  name={`inventorychangeSet[${index}].value`}
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
