import React from 'react';
import { gql, useMutation } from '@apollo/client';
import { Controller, useForm } from 'react-hook-form';
import query from './Products/query';
import ProductMaterialSelect from './ProductMaterialSelect';
import ProductCategorySelect from './ProductCategorySelect';

type ProductInput = {
  name: string;
  barcode: string;
  description: string;
  materials: number[];
  categories: number[];
  price: number;
  priceWithPees: number;
};

const CREATE_PRODUCT = gql`
  mutation CreateProduct($productInput: ProductInput) {
    createProduct(productInput: $productInput) {
      product {
        id
      }
    }
  }
`;

const CreateProduct: React.FC = () => {
  const defaultValues = {
    name: '',
    barcode: '',
    description: '',
    materials: [],
    categories: [],
    price: 2000,
    priceWithPees: 2500,
  };
  const [createProduct] = useMutation(CREATE_PRODUCT);

  // eslint-disable-next-line @typescript-eslint/unbound-method
  const { control, register, handleSubmit, reset } = useForm<ProductInput>({
    defaultValues,
  });
  const onSubmit = (productInput: ProductInput) =>
    createProduct({
      variables: { productInput },
      refetchQueries: [{ query }],
    }).then(() => reset());
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input placeholder="제품 이름" name="name" ref={register} required />
      <input placeholder="바코드" name="barcode" ref={register} />
      <textarea placeholder="제품 설명" name="description" ref={register} />
      <Controller
        name="materials"
        control={control}
        render={({ onChange, ref }) => (
          <ProductMaterialSelect onChange={onChange} inputRef={ref} isMulti />
        )}
      />
      <Controller
        name="categories"
        control={control}
        render={({ onChange, ref }) => (
          <ProductCategorySelect onChange={onChange} inputRef={ref} isMulti />
        )}
      />
      <input placeholder="가격" type="number" name="price" ref={register} />
      <input
        placeholder="수수료 포함 가격"
        type="number"
        name="priceWithPees"
        ref={register}
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default CreateProduct;
