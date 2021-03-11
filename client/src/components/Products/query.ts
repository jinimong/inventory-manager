import { gql } from '@apollo/client';

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

export default PRODUCTS;
