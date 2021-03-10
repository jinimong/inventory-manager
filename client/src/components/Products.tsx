import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { gql, useQuery } from '@apollo/client';
import { Product } from '../utils/types';

const PRODUCTS = gql`
  query {
    allProducts {
      id
      name
      barcode
      count
      materials {
        name
      }
      categories {
        name
      }
    }
  }
`;

const Products: React.FC = () => {
  const { loading, error, data } = useQuery<{
    allProducts: Product[];
  }>(PRODUCTS);
  const { pathname } = useLocation();
  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  return (
    <div>
      <h3>Products</h3>
      <hr />
      <ul>
        {data.allProducts.map((product) => (
          <li key={product.id}>
            <Link to={`${pathname}/${product.id}`}>
              <span>{product.name}</span>
              <span>
                ({product.materials.map((material) => material.name).join('/')})
              </span>
              <span>
                ({product.categories.map((category) => category.name).join('/')}
                )
              </span>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Products;
