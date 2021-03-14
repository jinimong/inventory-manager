import { gql } from '@apollo/client';

const CREATE_CATEGORY = gql`
  mutation CreateProductCategory($name: String!) {
    createCategory(name: $name) {
      category {
        id
      }
    }
  }
`;

export default CREATE_CATEGORY;
