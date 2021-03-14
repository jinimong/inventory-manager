import { useMutation, useQuery } from '@apollo/client';
import React, { useEffect, useState } from 'react';
import { OptionTypeBase } from 'react-select';
import CreatableSelect, { Props } from 'react-select/creatable';
import { OptionType, ProductCategory } from '../../utils/types';
import CREATE_CATEGORY from './mutation';
import query from './query';

const ProductCategorySelect: React.FC<Props<OptionTypeBase>> = ({
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
  const [createCategory] = useMutation(CREATE_CATEGORY, {
    refetchQueries: [{ query }],
  });
  const { loading, error, data } = useQuery<{
    allCategories: ProductCategory[];
  }>(query);

  useEffect(() => {
    if (data) {
      const { allCategories } = data;
      const options: OptionType[] = allCategories.map((category) => ({
        label: category.name,
        value: category.id,
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
      placeholder="카테고리를 선택하세요"
      isDisabled={isLoading}
      isLoading={isLoading}
      formatCreateLabel={(inputValue: string) =>
        `${inputValue} 카테고리 생성하기`
      }
      onChange={async (newValue, actionMeta) => {
        let newOptions = (newValue as OptionType[]) || [];
        if (actionMeta.action === 'create-option') {
          try {
            const optionsLength = newOptions.length;
            const newOption = newOptions[optionsLength - 1];
            if (newOption && newOption.__isNew__) {
              const name = newOption.label;
              const response = await createCategory({ variables: { name } });
              newOptions = newOptions.slice(0, optionsLength - 1).concat({
                label: name,
                value: (response as {
                  data: {
                    createCategory: {
                      category: ProductCategory;
                    };
                  };
                }).data.createCategory.category.id,
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

export default ProductCategorySelect;
