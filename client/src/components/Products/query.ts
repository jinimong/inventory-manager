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
      images {
        photoThumbnail
      }
    }
  }
`;

export default PRODUCTS;
