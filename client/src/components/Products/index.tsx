import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useQuery } from '@apollo/client';
import { Product } from '../../utils/types';
import query from './query';
import { serverURL } from '../../graphql/apollo';

const Products: React.FC = () => {
  const { loading, error, data } = useQuery<{
    allProducts: Product[];
  }>(query);
  const { pathname } = useLocation();
  if (loading || error || !data) {
    return <div>Loading...</div>;
  }
  return (
    <div>
      <h3>Products</h3>
      <hr />
      <Link to={`${pathname}/new`}>Create Product</Link>
      <hr />
      <ul>
        {data.allProducts.map((product) => (
          <li key={product.id}>
            <Link to={`${pathname}/${product.id}`}>
              {product.images.length && (
                <img
                  src={`${serverURL}${product.images[0].photoThumbnail}`}
                  alt=""
                />
              )}
              <span>{product.name}</span>
              <span>{product.count}</span>
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
