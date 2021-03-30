import { gql, useLazyQuery } from '@apollo/client';
import React from 'react';
import { UseFormMethods, Controller } from 'react-hook-form';
import Select from 'react-select';
import { OptionType, Store } from '../../utils/types';
import { EventInput } from './types';

const STORES = gql`
  query {
    allStores {
      id
      name
    }
  }
`;

const StoreIdField: React.FC<{ form: UseFormMethods<EventInput> }> = ({
  form: { control },
}) => {
  const [loadAllStores, { called, loading, data }] = useLazyQuery<{
    allStores: Store[];
  }>(STORES);
  const options = data
    ? data.allStores.map((store) => ({
        label: store.name,
        value: store.id,
      }))
    : [];
  return (
    <Controller
      name="storeId"
      control={control}
      render={({ onChange, ref }) => (
        <Select
          isLoading={called && loading}
          onMenuOpen={() => {
            if (!called) {
              loadAllStores();
            }
          }}
          onChange={(value, actionMeta) => {
            const storeId = (value as OptionType).value;
            onChange(storeId, actionMeta);
          }}
          inputRef={ref}
          options={options}
        />
      )}
    />
  );
};

export default StoreIdField;
