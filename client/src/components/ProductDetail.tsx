import React from 'react';
import { useParams } from 'react-router-dom';

const ProductDetail = () => {
  const { id } = useParams<{ id: string }>();
  return <div>Product Detail : {id}</div>;
};

export default ProductDetail;
