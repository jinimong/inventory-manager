import { useMutation, useQuery } from '@apollo/client';
import React, { useState, useEffect } from 'react';
import { OptionTypeBase } from 'react-select';
import CreatableSelect, { Props } from 'react-select/creatable';
import { ProductMaterial } from '../../utils/types';
import CREATE_MATERIAL from './mutation';
import query from './query';

type OptionType = {
  label: string;
  value: string | number;
  __isNew__?: boolean;
};

const ProductMaterialSelect: React.FC<Props<OptionTypeBase>> = ({
  onChange,
  ...rest
}) => {
  const [state, setState] = useState<{
    isLoading: boolean;
    options: OptionType[];
  }>({
    isLoading: true,
    options: [],
  });
  const [createMaterial] = useMutation(CREATE_MATERIAL, {
    refetchQueries: [{ query }],
  });
  const { loading, error, data } = useQuery<{
    allMaterials: ProductMaterial[];
  }>(query);

  useEffect(() => {
    if (data) {
      const { allMaterials } = data;
      const options: OptionType[] = allMaterials.map((material) => ({
        label: material.name,
        value: material.id,
      }));
      setState((prevState) => ({
        ...prevState,
        isLoading: false,
        options,
      }));
    }
  }, [data]);

  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  if (!onChange) {
    return <div>...</div>;
  }

  const { isLoading, options } = state;

  return (
    <CreatableSelect
      options={options}
      placeholder="재질을 선택하세요"
      isDisabled={isLoading}
      isLoading={isLoading}
      formatCreateLabel={(inputValue: string) => `${inputValue} 재질 생성하기`}
      onChange={async (newValue, actionMeta) => {
        let newOptions = (newValue as OptionType[]) || [];
        if (actionMeta.action === 'create-option') {
          try {
            const optionsLength = newOptions.length;
            const newOption = newOptions[optionsLength - 1];
            if (newOption && newOption.__isNew__) {
              const name = newOption.label;
              const response = await createMaterial({ variables: { name } });
              newOptions = newOptions.slice(0, optionsLength - 1).concat({
                label: name,
                value: (response as {
                  data: {
                    createMaterial: {
                      material: ProductMaterial;
                    };
                  };
                }).data.createMaterial.material.id,
              });
            }
          } catch (err) {
            console.log('error', err);
          }
        }
        onChange(
          newOptions.map((option) => option.value),
          actionMeta,
        );
      }}
      {...rest}
    />
  );
};

export default ProductMaterialSelect;
