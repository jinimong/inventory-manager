import { gql, useQuery } from '@apollo/client';
import React from 'react';
import { OptionTypeBase } from 'react-select';
import CreatableSelect, { Props } from 'react-select/creatable';
import { ProductMaterial } from '../utils/types';

const MATERIALS = gql`
  query {
    allMaterials {
      id
      name
    }
  }
`;

type OptionType = {
  label: string;
  value: string | number;
};

const ProductMaterialSelect: React.FC<Props<OptionTypeBase>> = ({
  onChange,
  ...rest
}) => {
  const { loading, error, data } = useQuery<{
    allMaterials: ProductMaterial[];
  }>(MATERIALS);
  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  if (!onChange) {
    return <div>...</div>;
  }
  const { allMaterials } = data;
  const options: OptionType[] = allMaterials.map((material) => ({
    label: material.name,
    value: material.id,
  }));

  return (
    <CreatableSelect
      options={options}
      placeholder="재질을 선택하세요"
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

export default ProductMaterialSelect;
