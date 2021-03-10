import React from 'react';
import { useParams } from 'react-router-dom';
import { gql, useQuery } from '@apollo/client';
import { Product } from '../utils/types';

const PRODUCT_DETAIL = gql`
  query productDetail($id: Int!) {
    product(id: $id) {
      name
      barcode
      count
      materials {
        id
        name
      }
      categories {
        id
        name
      }
      storeproductSet {
        id
        store {
          id
          name
        }
        count
      }
    }
  }
`;

const ProductDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const { loading, error, data } = useQuery<{
    product: Product;
  }>(PRODUCT_DETAIL, { variables: { id: +id } });

  if (loading || error || !data) {
    return <div>Loading...</div>;
  }

  const {
    product: {
      name,
      barcode,
      description,
      count,
      materials,
      categories,
      storeproductSet,
    },
  } = data;

  return (
    <div>
      <h3>Product Detail</h3>
      <hr />
      <div>
        <span>name: </span>
        <span>{name}</span>
      </div>
      <div>
        <span>count: </span>
        <span>{count}</span>
      </div>
      {barcode && (
        <div>
          <span>barcode: </span>
          <span>{barcode}</span>
        </div>
      )}
      {description && (
        <div>
          <span>description: </span>
          <span>{description}</span>
        </div>
      )}
      {materials && (
        <div>
          {materials.map((material) => (
            <span key={material.id}>{material.name}</span>
          ))}
        </div>
      )}
      {categories && (
        <div>
          {categories.map((category) => (
            <span key={category.id}>{category.name}</span>
          ))}
        </div>
      )}
      {storeproductSet && (
        <ul>
          {storeproductSet.map((storeProduct) => (
            <li key={storeProduct.id}>
              <span>{storeProduct.store.name}</span>
              <span>{storeProduct.count}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ProductDetail;
