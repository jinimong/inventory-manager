import { gql, useQuery } from '@apollo/client';
import React from 'react';
import { OptionTypeBase } from 'react-select';
import CreatableSelect, { Props } from 'react-select/creatable';
import { ProductCategory } from '../utils/types';

const CATEGORIES = gql`
  query {
    allCategories {
      id
      name
    }
  }
`;

type OptionType = {
  label: string;
  value: string | number;
};

const ProductCategorySelect: React.FC<Props<OptionTypeBase>> = ({
  onChange,
  ...rest
}) => {
  const { loading, error, data } = useQuery<{
    allCategories: ProductCategory[];
  }>(CATEGORIES);
  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  if (!onChange) {
    return <div>...</div>;
  }
  const { allCategories } = data;
  const options: OptionType[] = allCategories.map((category) => ({
    label: category.name,
    value: category.id,
  }));

  return (
    <CreatableSelect
      options={options}
      placeholder="카테고리을 선택하세요"
      onChange={(newValue, actionMeta) => {
        const handleChange = () =>
          onChange(
            newValue && (newValue as OptionType[]).map((opt) => opt.value),
            actionMeta,
          );
        if (actionMeta.action === 'create-option') {
          // TO CREATE
          handleChange();
        } else {
          handleChange();
        }
      }}
      {...rest}
    />
  );
};

export default ProductCategorySelect;
